words = input().upper()
d = {}
for w in words:
	d[w] = 0

for w in words:
	d[w] = d[w]+1

max_keys = []
max_value = None
for key, value, in d.items():
	if max_value is None or value>max_value:
		max_keys = [key]
		max_value = value
	elif value == max_value:
		max_keys.append(key)

if len(max_keys) >= 2:
	print("?")
else:
	print(max_keys[0])