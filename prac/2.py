'''

n=3
m=4
for i in range(1,n+1):
    print('*'*m , end=' ')
    print()

'''
'''

n=4
m=5
spaces=1
for j in range(1,n):
    if (j == 2) or (j==3):
        print('*',end=' ')
        for spaces in range(1,spaces+1):
            print(' ', end = ' ')
        print('*',end=' ')
        print()
    print('*'*m,end= ' ' )
    print()

'''
'''

n=5
for j in range(1,n+1):
    for i in range(j):
        print('*' , end=' ')
    print()

'''
'''

n=5
for j in range(n,0,-1):
    for i in range(j):
        print('*' , end=' ')
    print()

'''
'''

n=5
spaces = 4
for i in range (1,n*2+1,2):
    for spaces in range(spaces):
        print(' ' ,end= ' ')
    for j in range(i):
        print('*',end=' ')
    print()
spaces-=1

'''
'''

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

'''
'''

n=5
for i in range (n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

'''
'''

n=5
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end = ' ')
        num+=1
    print()

'''
'''

n=4
spaces = 3
for j in range(1,n*2+1):
    for i in range(1,j+1):
        print('*',end=' ')
    for spa in range(spaces):
        print(' ',end= ' ')                         wrong pattern
    for i in range(1,j+1):
        print('*',end=' ')
    for spa in range(spaces):
        print(' ',end= ' ')
    spaces-=1
    print()
    spaces=0
    for p in range (j+1):
        print('*',end=' ')
    for spac in range(spaces):
        print(' ' ,end = ' ')

'''
'''

n=5
for i in range(1,n+1):
    print(('*'*(2*i-1)).center(2*n-1))
for i in range(n+1,0,-1):
    print(('*'*(2*i-1)).center(2*n-1))

'''
n=5
spaces=4
for i in range(1,n+1):
    for spa in range(spaces):
        print(' ',end=' ')
    for j in range(i,0,-1):
        print(j,end= ' ')
    if (i>=2):
        for dev in range(2,i+1):
            print(dev,end= ' ')
        
        print()
    print()
    spaces-=1
