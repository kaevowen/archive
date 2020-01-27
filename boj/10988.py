def check_palindrome(copy):
	cat = ''
	for i in reversed(copy):
		cat += i
	if copy==cat:
		return 1
	return 0

print(check_palindrome(input()))