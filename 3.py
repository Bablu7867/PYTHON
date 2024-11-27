'''
            LCM

num1=7
num2=12
if num1>num2:
    lcm=num1
else:
    lcm=num2
while True:
    if lcm%num1==0 and lcm%num2==0:
        print(lcm)
        break
    else:
        lcm+=1


'''

'''
                GCD

s=8
d=11
if s<d:
    gcd=s
else:
    gcd=d
while True:
    if s%gcd==0 and d%gcd==0:
        print(gcd)
        break
    else:
        gcd-=1


'''

'''
        PALYPRIME NUMBER

num=11
car=num
for den in range(2,num//2+1):
    if num%den==0:
        print('not a palyprime number')
        break
else:
    rev=0
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    if car==rev:
        print('palyprime number')
    else:
        print('not a palyprime number')

'''

'''
        #EMIRP NUMBER (NOT A PALINDROME AND NUMBER IS PRIME NUMBER AND REVERSE OF THAT NUMBER IS ALSO PRIME NUMBER

num=int(input())
tec=num
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num//=10
if tec==rev:
    print('palindrome')
else:
    fac=0
    for i in range(1,tec+1):
        if tec%i==0:
            fac=fac+1
    if fac==2:
        print(f'{tec} is a prime number')
        g=0
        gro=tec
        while gro > 0:
            re=gro%10
            g=g*10+re
            gro=gro//10
        print(f'{g} is reverse of {tec}')
        hi=0
        for jar in range (1,g+1):
            if g%jar==0:
                hi+=1
        if hi==2:
            print(f'{g} is a prime number AND EMIRP')
        else:
            print(f'{g} IS NOT EMIRP')
    else:
        print(f'{tec} is not EMIRP')

'''
'''
        strong number

num=145
copy=num
ans=0
while num!=0:
    rem=num%10
    num=num//10
    fact=1
    for dev in range(1,rem+1):
        fact=fact*dev
    ans+=fact
if ans==copy:
    print('strong number')
else:
    print('not a strong number')

'''
''''
num=7
for i in range(1,num+1):
    print('*')'''

'''
num=7
for i in range(1,num+1):
    print('*',end=' ')

'''
'''
num=7
for i in range(1,num+1):
    for j in range(1,num+1):
        print('MAHI',end=' ')
    print()
    
'''
'''
num=5
for i in range(1,num+1):
    print('*'*num)

'''

'''

num=7
for i in range(1,num+1):
    for j in range(1,i+1):
        print('MAHI',end=' ')
    print()

'''

'''

num=7
for i in range(1,num+1):
    print('* '*i)

'''

'''

num=7
for i in range(num,0,-1):
    for j in range(i):
        print('MAHI',end=' ')
    print()

'''

num=4
spaces=num-1
for den in range(1,num+1):
    for spa in range(spaces):
        print(' ',end=' ')
    for st in range(den):
        print('*',end=' ')
    print()
    spaces-=1
