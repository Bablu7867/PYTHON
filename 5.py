'''
num=5
for line in range(2,num+2):
    for dev in range(1,line):
        print(dev,end=' ')
    print()
'''
'''
nu=6
for line in range(nu+1,1,-1):
    for dev in range(1,line):
        print(dev,end=' ')
    print()
'''
'''
nu=6
for line in range(nu,0,-1):
    for dev in range(nu-line+1):
        print(nu-dev,end=' ')
    print()
'''
'''nu=6
for line in range(nu,-1,-1):
    for dev in range(nu,line,-1):
        print(dev,end=' ')
    print()
'''
'''
num=5
for i in range (1,num+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
'''
'''
num=5
for line in range(num,0,-1):
    for dev in range(line,num+1):
        print(dev,end=' ')
    print()
'''
''''
num=5
space=num-1
for line in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for dig in range(1,line+1):
        print(dig,end=' ')
    print()
    space-=1
'''
'''
num=5
space=0
for line in range(num,0,-1):
    for sp in range(space):
        print(' ',end=' ')
    for dig in range(1,line+1):
        print(dig,end=' ')
    print()
    space+=1
'''
'''
num=5
space=num-1
for line in range(num,0,-1):
    for sp in range(space):
        print(' ',end=' ')
    for dig in range(line,num+1):
        print(dig,end=' ')
    print()
    space-=1
'''
'''
num=7
space=num-1
for line in range(num,0,-1):
    for sp in range(space):
        print(' ',end=' ')
    for dig in range(num,line-1,-1):
        print(dig,end=' ')
    print()
    space-=1
'''
'''
num=5
space=num-1
for line in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for dig in range(line,0,-1):
        print(dig,end=' ')
    print()
    space-=1
''''''
num=4
spaces=num-1
for line in range(1,num*2,2):
    for den in range(spaces):
        print(' ',end=' ')
    for n in range(line,0,-1):
        print(line,end=' ')
    print()
    spaces-=1
'''
'''
num=4
spaces=0
for line in range(num*2-1,0,-2):
    for den in range(spaces):
        print(' ',end=' ')
    for n in range(1,line+1):
        print(n,end=' ')
    print()
    spaces+=1
'''
'''
num=4
spaces=num-1
for line in range(1,num*2,2):
    for sp in range(spaces):
        print(' ',end=' ')
    for n in range(1,line+1):
        print(n,end=' ')
    print()
    spaces-=1
'''
num=4
spaces=0
for line in range(num+1,0,-1):
    for sp in range(spaces):
        print(' ',end=' ')
    for n in range(line,0,-1):
        print(n,end=' ')
    print()
    spaces+=1
