import random

SAMPLE_ALPHABET = [
'A','B','C','D','E','F',
'G','H','I','J','K','L',
'M','N','O','P','Q','R',
'S','T','U','V','W','X',
'Y','Z'
]

def rotate(disk, word) :
    if disk[0] == word:
        return disk
    else:
        return rotate(disk[-1] + disk[:-1], word)


sel = int(input('1 == 암호화, 2 == 복호화 : '))
if sel == 1:
    word = input("영어단어입력(공백ㄴㄴ 대문자만)").upper()
    key = [_ for _ in range(1, len(word)+1)]
    disk = [
    'DBYLIXTVFKZGHASJREWPUNCQMO',
    'EUJVWYGSIHAFRBXODNTPZQMCKL',
    'HRFKVAMUQYNLECZBTOGXJSIPDW',
    'FRAHMTGPLIUKEQZCNSDOVBJWXY',
    'WREXDPJUSHCOYBLTMFNIVGQZKA',
    ]
    '''
    for i in range(len(word)):
        disk.append("".join(random.sample(SAMPLE_ALPHABET,26)))
    '''
    key = random.sample(key, len(disk))
    new_disk = []
    for i in range(len(disk)):
        new_disk.append(rotate(disk[i], word[i]))
        print(disk[i])
    print("위의 문자열을 밥에게 전해주세요.")
    print("===========================")
    print("")
    for i in range(len(disk)):
        print(new_disk[i])

if sel == 2:
    pass
        
'''
    print("암호화 완료. 텍스트파일을 밥에게 전해주세요.")

elif sel == 2:
    print("디스크를 입력해주세요")
    try:
        with open('disk', 'r') as f:
            pass
    except IOError:
        print()

    print(disk)
else:
    print("올바른 메뉴를 선택 해주세요.")
#암호화시 디스크 랜덤 생성. 복호화 과정에서는 미리 생성된 디스크로 해야함!

'''