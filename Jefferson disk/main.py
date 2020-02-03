import random

SAMPLE_ALPHABET = [
'A','B','C','D','E','F',
'G','H','I','J','K','L',
'M','N','O','P','Q','R',
'S','T','U','V','W','X',
'Y','Z'
]

def rotate(cipher, char) :
    new_cipher = []
    for c in cipher :
        new_cipher.append(c)

    count = 26 - new_cipher.index(char)

    for i in range(count) :
        new_cipher.insert(0, new_cipher.pop())

    return ''.join(new_cipher)


# 1 == 암호화 2 == 복호화 
sel = int(input('1 == 암호화, 2 == 복호화 : '))
if sel == 1:
    n = int(input('글자 몇개? '))

    key = [_ for _ in range(n)]
    disk = []
    for i in range(n):
        disk.append("".join(random.sample(SAMPLE_ALPHABET,26)))

    key = random.sample(key, len(disk))

    new_disk = [] # 따로 선언안하고 원래 있던곳에서 처리하고싶은데

    for i in range(len(key)) :
        new_disk.append(disk[key[i]-1])

    word = 'hellothere'.upper()

    for j in range(len(new_disk)) :
        new_disk[j] = new_disk[j].replace(new_disk[j], 
            rotate(new_disk[j], word[j]))
    with open('disk.txt','w') as f:
        for nd in new_disk:
            f.write(nd+'\n')
        print("key : ", *key)
        for k in key:
            f.write('%d ' % k)

    print("암호화 완료. 텍스트파일을 밥에게 전해주세요.")

elif sel == 2:
    print("디스크를 입력해주세요")
    try:
        with open('disk', 'r') as f:

    except IOError:
        print()

    print(disk)
else:
    print("올바른 메뉴를 선택 해주세요.")
#암호화시 디스크 랜덤 생성. 복호화 과정에서는 미리 생성된 디스크로 해야함!



