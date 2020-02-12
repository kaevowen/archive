import socket
import select

HEADER_LENGTH = 10
IP = '127.0.0.1'
PORT = 5054

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]
clients = {}


def recv_msg(client_socket):
	try:
		message_header = client_socket.recv(HEADER_LENGTH)

		if not len(message_header):
			return False

		message_lenth = int(message_header.decode("utf-8").strip())
		return {"header": message_header, 
				"data":client_socket.recv(message_lenth)}

	except:
		return False

while 1:
	read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

	for notified_socket in read_sockets:
		if notified_socket == server_socket:
			client_socket, client_address = server_socket.accept()

			user = recv_msg(client_socket)
			if user is False:
				continue

			socket_list.append(client_socket)
			clients[client_socket] = user
			print(f"Accpted new connection from" +
				  f"{client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")

		else:
			msg = recv_msg(notified_socket)

			if msg is False:
				print(f"Closed connection from " +
					  f"{clients[notified_socket]['data'].decode('utf-8')}")

				socket_list.remove(notified_socket)
				del clients[notified_socket]
				continue

			user = clients[notified_socket]
			print(f"Received message from {user['data'].decode('utf-8')} : {msg['data'].decode('utf-8')}")


			for client_socket in clients:
				if client_socket != notified_socket:
					client_socket.send(user['header'] + user['data'] + message['header']+ msg['data'])

	for notified_socket in exception_sockets:
		socket_list.remove(notified_socket)
		del clients[notified_socket]