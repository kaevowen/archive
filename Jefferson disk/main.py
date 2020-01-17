def rotate(cipher, char) :
	new_cipher = []

	for c in cipher :
		new_cipher.append(c)

	count = 26 - new_cipher.index(char)

	for i in range(count) :
		new_cipher.insert(0, new_cipher.pop())

	return ''.join(new_cipher)

disk = [
	'ZWAXJGDLUBVIQHKYPNTCRMOSFE', # 1
	'KPBELNACZDTRXMJQOYHGVSFUWI', # 2
	'BDMAIZVRNSJUWFHTEQGYXPLOCK', # 3
	'RPLNDVHGFCUKTEBSXQYIZMJWAO', # 4
	'IHFRLABEUOTSGJVDKCPMNZQWXY', # 5
	'AMKGHIWPNYCJBFZDRUSLOQXVET', # 6
	'GWTHSPYBXIZULVKMRAFDCEONJQ', # 7
	'NOZUTWDCVRJLXKISEFAPMYGHBQ', # 8
	'XPLTDSRFHENYVUBMCQWAOIKZGJ', # 9
	'UDNAJFBOWTGVRSCZQKELMXYIHP'  # 10
] # 보내고 싶은 메세지에 따라서 크기가 바뀔수도?
  # 하지만 너무 길어지면 뚫릴지도 모름

key = [7,9,5,10,1,6,3,8,2,4] # 숫자지정가능

new_disk = [] # 따로 선언안하고 원래 있던곳에서 처리하고싶은데

for i in range(len(key)) :
	new_disk.append(disk[key[i] - 1])

word = 'HELLOTHERE' # 이것도 지정가능. 아니면 지정한 단어에 맞춰서 랜덤한 디스크를 생성해야할듯

for j in range(len(new_disk)) :
	new_disk[j] = new_disk[j].replace(new_disk[j], rotate(new_disk[j], word[j]))
	# 돌린다음에 다시 저장

for k in new_disk :
	print(k[0], end = '') # 숫자지정가능
print()

