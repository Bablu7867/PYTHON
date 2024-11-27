'''

num=int(input())
spaces=num-1
for den in range(1,num*2,2):
    for spa in range(spaces):
        print(' ',end=' ')
    for st in range(den):
        print('*',end=' ')
    print()
    spaces-=1
    
'''
'''
num=int(input())
spaces=0
for den in range(num*2-1,0,-2):
    for spa in range(spaces):
        print(' ',end=' ')
    for st in range(den):
        print('*',end=' ')
    print()
    spaces+=1
    
'''
'''
num=int(input())
for den in range(num):
    for line in range(num):
        print(2,end=' ')
    print()

'''
'''
num=int(input())
for den in range(1,num+1):
    for line in range(1,num+1):
        print(den,end=' ')
    print()
'''
'''
num=int(input())
for den in range(1,num+1):
    for line in range(1,den+1):
        print(den,end=' ')
    print()
'''
'''
num=int(input())
for den in range(num,0,-1):
    for line in range(1,den+1):
        print(den,end=' ')
    print()
'''
'''
num=int(input())
for den in range(num,0,-1):
    for line in range(num-den+1):
        print(den,end=' ')
    print()
'''
num=int(input())
for den in range(1,num+1):
    for line in range(num-den+1):
        print(den,end=' ')
    print()
