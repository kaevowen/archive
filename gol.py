def switch(b):
	if b == '1':
		return '0'
	else:
		return '1'

def compute(li, s):
	try:
		return li[s+1] == li[s-1]
	except IndexError:
		return li[0] == li[s-1]


from time import sleep

line = '010001101101010'

while 1:
	line_after = ''
	for n in range(len(line)):
		condition = compute(line, n)

		if condition is False:
			line_after += switch(line[n])
		else:
			line_after += line[n]

	print(line_after)
	sleep(1)
	line = line_after