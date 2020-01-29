def palindrome(s):
	q = []
	st = []

	for x in s:
		if x.isalpha():
			q.append(x.lower())
			st.append(x.lower())

	while q:
		if q.pop(0) != st.pop():
			return False

	return True

print(palindrome('Wow'))