#https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

import re

def dart_game(scores):
    k = []
    c=0
    scores = re.findall(re.compile('\d\d?|[SDT]|[#*]'), scores)

    for i in range(len(scores)):
        try:
            n = int(scores[i])
        except ValueError:
            if scores[i] == 'S':
                k.append(pow(n, 1))


            elif scores[i] == 'D':
                k.append(pow(n, 2))      

            elif scores[i] == 'T':
                k.append(pow(n, 3))

            elif scores[i] == '*':
                c+=1
                l = len(k)-1
                if c==2:
                    k[l] *= 2
                    k[l-1] *= 1
                    c=0
                else:                    
                    k[l] *= 2
                    k[l-1] *= 2


            elif scores[i] == '#':
                l = len(k)-1
                k[l] *= -1

    return k, sum(k)

print('1.',dart_game('1S2D*3T'))
print('2.',dart_game('1D2S#10S'))
print('3.',dart_game('1D2S0T'))
print('4.',dart_game('1S*2T*3S'))
print('5.',dart_game('1D#2S*3S'))
print('6.',dart_game('1T2D3D#'))
print('7.',dart_game('1D2S3T*'))
print('8.',dart_game('1S*2T*3S*'))