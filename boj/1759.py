from random import sample

#l = int(input())
l = 4
#c = int(input())
c = 4
pw=[]
#sample_words = input().split(' ')
sample_words = 'a t c i'.split(' ')

for _ in range(l**l):
	pw.append("".join(sample(sample_words, l)))

pw.sort()
for pw in pw:
	print(pw)