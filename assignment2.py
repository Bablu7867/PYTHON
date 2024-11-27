'''
num=4
spaces=num-1
for den in range(1,num*2,2):
    for line in range(spaces):
        print(' ',end=' ')
    for n in range(den):
        print(den,end=' ')
    print()
    spaces-=1
'''
'''
num=4
spaces=0
for den in range(num*2-1,0,-2):
    for line in range(spaces):
        print(' ',end=' ')
    for n in range(den):
        print(den,end=' ')
    print()
    spaces+=1
'''

num=4
for line in range(num*2-1,0,-2):
    for den in range(line,0,-2):
        print(line,end=' ')
    print()
    line-=1
'''
num=int(input())
for line in range(1,num*2,2):
    for den in range(line,0,-2):
        print(line,end=' ')
    print()
'''
