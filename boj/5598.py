for n in input():
    # if n is A,B,C
    if ord(n) <= 67:
        print(chr(ord(n)+23) , end='')
    else:
        print(chr(ord(n)-3), end='')


# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
