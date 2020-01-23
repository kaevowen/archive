def palindrome(s):
	w = ''
	for x in s:
		if x.isalpha():
			w+=x.lower()

	count = 0
	l = len(w) - 1 
	
	for i in range(len(w)):
		if w[i]==w[l]:
			count+=1

		l-=1

	if count==len(w):
		return True
	else:
		return False


print(palindrome("Madam, I'm Adam"))