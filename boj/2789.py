censoreship = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
words = input()
censored_words=''
for w in words:
	if w not in censoreship:
		censored_words+=w
	else:
		pass

print(censored_words)
