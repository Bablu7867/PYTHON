'''
n=9
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print('prime')
else:
    print('not prime')
'''
'''
n=5
f=1
for i in range(1,n+1):
    f=f*i
print(f)
'''
'''
n=4324
num=0
while n!=0:
    rem=n%10
    num+=rem
    n//=10
print(num)
'''
'''
n=564328
num=0
while n!=0:
    rem=n%10
    if rem%2==0:
        num+=rem
    n//=10
print(num)
'''
'''
n=7656
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)
'''
'''
n=833800
b=n
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n//=10
if rev==b:
    print('Palindrome')
else:
    print('Not Palindrome')
'''
'''
n=153
b=n
c=len(str(n))
res=0
while n!=0:
    rem=n%10
    res=res+rem**c
    n//=10
if b==res:
    print('Armstrong')
else:
    print('Not Armstrong')
'''
'''
n=135
b=n
c=len(str(n))
res=0
while n!=0:
    rem=n%10
    res=res+rem**c
    n//=10
    c-=1
if res==b:
    print('Disarm')
else:
    print('not Disarm')
'''
'''
n=7
ans=0
pos=1
while n!=0:
    rem=n%2
    ans=ans+rem*pos
    pos*=10
    n//=2
print(ans)
'''
'''
n=19
b=n
while n>9:
    res=0
    while n!=0:
        rem=n%10
        res=res+rem**2
        n//=10
    n=res
if n==1 or n==7:
    print('Happy number')
else:
    print('Not Happy')
'''
'''
n=202
if (len(str(n)))%2==0 :
    fc=n//(10**(len(str(n))//2))
    fp=n%(10**(len(str(n))//2))
    if n==(fp+fc)**2:
        print('Tech Number')
    else:
        print('Not Tech Number')
else:
    print('Not possible')
'''
'''
n=5
for val in range(n):
    print('*')
'''
'''
n=5
for h in range(n,0,-1):
    for k in range(h):
        print('*',end=' ')
    print()
'''
'''
n=4
s=n-1
for j in range(1,n*2,2):
    for sp in range(s):
        print(' ',end=' ')
    for v in range(j,0,-1):
        print(v,end=' ')
    print()
    s-=1
'''
'''
n=5
s=n-1
for l in range(1,n+1):
    for sp in range(s):
        print(' ',end=' ')
    for k in range(l,0,-1):
        print(k,end=' ')
    print()
    s-=1
'''
'''
n=4
s=0
for l in range(n*2-1,0,-2):
    for sp in range(s):
        print(' ',end=' ')
    for k in range(1,l+1):
        print(k,end=' ')
    print()
    s+=1
'''
