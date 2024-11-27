'''
n=1
while n!=11:
    print(n)
    n+=1
n=10
while n!=0:
    print(n)
    n-=1
n=20
while n!=41:
    if n%2==0:
        print(n)
    n+=1
n='mahi'
ind=0
while ind!=len(n):
    print(n[ind])
    ind+=1
'''
'''
n=12
c=0
for j in range(1,n+1):
    if n%j==0:
        c+=1
if c==2:
    print('prime')
else:
    print('not')
'''
'''
n=5
fac=1
for j in range(1,n+1):
    fac*=j
print(fac)
'''
'''
n=78672
res=0
while n!=0:
    res+=n%10
    n//=10
print(res)
'''
'''
n=87847
res=0
while n!=0:
    rem=n%10
    if rem%2==0:
        res+=rem
    n//=10
print(res)
'''
'''
n=6756
res=0
while n!=0:
    rem=n%10
    res=res*10+rem
    n//=10
print(res)
'''
'''
n=83386
j=n
res=0
while n!=0:
    rem=n%10
    res=res*10+rem
    n//=10
if j==res:
    print('palindrome')
else:
    print('not')
'''
'''
n=158
k=len(str(n))
res=0
l=n
while n!=0:
    rem=n%10
    res=res+rem**k
    n//=10
if l==res:
    print('armstrong')
else:
    print('not')
'''
'''
n=135
k=len(str(n))
res=0
l=n
while n!=0:
    rem=n%10
    res=res+rem**k
    n//=10
    k-=1
if l==res:
    print('disarum')
else:
    print('not')
'''
'''
n=14
ans=0
pos=1
while n!=0:
    rem=n%2
    ans=ans+pos*rem
    pos*=10
    n//=2
print(ans)
'''
'''
n=1010
ans=0
pow=0
while n!=0:
    rem=n%10
    ans=rem*(2**(pow))+ans
    pow+=1
    n//=10
print(ans)
'''
'''
n=100
h=n
while n>9:
   res=0
   while n!=0:
       rem=n%10
       res=res+rem**2
       n//=10
if res==1 or res==7:
    print('happy')
else:
    print('not')
'''
'''
n=2025
if len(str(n))%2==0:
    f=n//(10**(len(str(n))//2))
    g=n%(10**(len(str(n))//2))
if n==(f+g)**2:
    print('tech')
else:
    print('not')
'''
'''
n=10
c=0
while n!=0:
    rem=n%2
    if rem==1:
        c+=1
    n//=2
if c==2:
    print('evil')
else:
    print('odeous')
'''
'''
n=7
p=12
if n>p:
    lcm=n
else:
    lcm=p
while True:
    if lcm%n==0 and lcm%p==0:
        print(lcm)
        break
    else:
        lcm+=1
'''
'''
n=8
p=11
if n>p:
    lcm=n
else:
    lcm=p
while True:
    if lcm%n==0 and lcm%p==0:
        print(lcm)
        break
    else:
        lcm-=1
'''
'''
n=11
for j in range(2,n//2+1):
    if n%j==0:
        print('not polyprime')
        break
else:
    ans=0
    m=n
    while n!=0:
        rem=n%10
        ans=ans*10+rem
        n//=10
    if m==ans:
        print('polyprime')
    else:
        print('not polyprime')
'''
'''
n=31
ans=1
m=n
while n!=0:
    rem=n%10
    ans=ans*10+rem
    n//=10
    print(ans)
if m==ans:
    print('not possible for emirp')
else:
    c=0
    for j in range(2,n//2+1):
        if m%j==0:
            print('not a emirp')
        else:
            l=1
            p=m
            while m!=0:
                res=m%10
                l=l*10+res
                l//=10
                print(l)
            for q in range(2,p//2+1):
                if p%q==0:
                    print('not a emirp')
                else:
                    print(f'{l} is emirp number')
'''
'''
n=145
copy=n
ans=0
while n!=0:
    rem=n%10
    fac=1
    for j in range(1,rem+1):
        fac=fac*j
    ans+=fac
    n//=10
if copy==ans:
    print('strong')
else:
    print('not')
'''
'''
n=7
for k in range(1,n+1):
    print('*')
'''
'''
n=5
for j in range(1,n+1):
    for k in range(1,n+1):
        print('*',end= ' ')
    print()
'''
'''
n=3
for j in range(1,n+1):
    print('* ' * j)
print()
'''
'''
n=5
for k in range(n,0,-1):
    for l in range(k):
        print('*',end=' ')
    print( )
'''
'''
n=4
s=n-1
for den in range(1,n+1):
    for k in range(s):
        print(' ',end=' ')
    for l in range(den):
        print('*',end=' ')
    print()
    s-=1
'''
'''
n=4
s=0
for den in range(n,0,-1):
    for k in range(s):
        print(' ',end=' ')
    for l in range(den):
        print('*',end=' ')
    print()
    s+=1
'''
'''
n=4
s=n-1
for den in range(1,n*2,2):
    for k in range(s):
        print(' ',end=' ')
    for j in range(den):
        print('*',end=' ')
    print()
    s-=1
'''
'''
n=3
for j in range(n):
    for i in range(n):
        print('2',end=' ')
    print()
'''
'''
n=5
for k in range(n,0,-1):
    for l in range(1,k+1):
        print(l,end=' ')
    print()
'''
'''
n=4
s=n-1
for k in range(1,n*2,2):
    for l in range(s):
        print(' ',end=' ')
    for p in range(1,k+1):
        print(p,end=' ')
    print()
    s-=1
'''
