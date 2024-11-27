'''

num1=6
num2=17
num3=9
if num1>num2:
    if num1>num3:
        print('num1 is highest')
    else:
        print('num3 is highest')
else:
    if num2>num3:
        print('num2 is highest')
    else:
        print('num3 is highest')
    
'''
'''

n1=3
n2=4
n3=8
n4=7
if n1>n2:
    if n1>n3:
        if n1>n4:
            print('n1 is high')
        else:
            print('n4 is highest')
    else:
        if n3>n4:
            print('n3 is high')
        else:
            print('n4 is high')
else:
    if n2>n3:
        if n2>n4:
            print('n2 is high')
        else:
            print('n4 is high')
    else:
        if n3>n4:
            print('n3 is high')
        else:
            print('n4 is high')

'''
'''

n='1234'
for ch in n:
    for ele in n:
        print(ele)

'''
'''
n=1
while n!=11:
    print(n)
    n+=1

'''
'''

n=10
while n>0:
    print(n)
    n-=1

'''
'''

n=-1
while n!=-11:
    print(n)
    n-=1

'''
'''

n=20
while n!=41:
    if n%2==0:
        print(n)
    n+=1

'''
'''

n='Mahi'
ind=0
while ind!=len(n):
    print(n[ind])
    ind+=1

'''
'''

n=100
while n!=94:
    print(n)
    n-=1
else:
    print("MAHI")

'''
'''

num=7
c=0
for i in range(1,num+1):
    if num%i==0:
        c+=1
if c==2:
    print('Prime')
else:
    print('NOT')
    
'''
'''

num=5
res=1
for i in range(1,num+1):
    res=res*i
print(res)

'''
'''

num=9876
res=0
while num!=0:
    rem=num%10
    res=rem+res
    num//=10
print(res)

'''
'''

num=7896
res=0
while num!=0:
    rem=num%10
    if rem%2!=0:
        res=rem+res
    num//=10
print(res)

'''
'''

num=7865
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num//=10
print(rev)

'''
'''

num=9099
rev=num
res=0
while num!=0:
    rem=num%10
    res=res*10+rem
    num//=10
if rev==res:
    print("PALIN")
else:
    print("NOT")

'''
'''

num=12
count=0
for i in range(1,num+1):
    if num%i==0:
       count+=1
if count!=2:
    print("COMPOSITE")
else:
    print("PRIME")

'''
'''

num=370
res=0
rev=num
l=len(str(num))
while num!=0:
    rem=num%10
    res=res**l+rem
    num//=10
if rev==rev:
    print("ARM")
else:
    print("NOT")

'''
'''

num=135
l=len(str(num))
rev=num
res=0
while num!=0:
    rem=num%10
    res=rem**l+res
    num//=10
    l-=1
if rev==res:
    print("DISARN")
else:
    print("NOT")

'''
'''

num=8
ans=0
pos=1
while num!=0:
    rem=num%2
    ans=ans+rem*pos
    pos=pos*10
    num//=2
print(ans)

'''
'''

num=10101
ans=0
pow=0
while num!=0:
    rem=num%10
    ans=ans+(2**(pow))*rem
    pow+=1
    num//=10
print(ans)

'''
'''

num=1010
ans=0
pos=1
while num!=0:
    rem=num%10
    ans=ans+rem*pos
    pos*=2
    num//=10
print(ans)

'''
'''

num=1908
num1=num
while num>9:
    ans=0
    while num!=0:
        rem=num%10
        ans=ans+rem**2
        num//=10
    num=ans
print(ans)
if ans==1 or ans==7:
    print('happy')
else:
    print('not happy')

'''
'''

num=2024
l=len(str(num))
if l%2==0:
    fp=num//(10**(l//2))
    gp=num%(10**(l//2))
    if (fp+gp)**2==num:
        print('Tech')
    else:
        print('NOT')
else:
    print('not possible')

'''
'''

num=21
cou=0
while num!=0:
    rem=num%2
    if rem==1:
        cou+=1
    num//=2
if cou==2:
    print("EVIL")
else:
    print("NOT")

'''
'''

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

num1=8
num2=11
if num1>num2:
    gcd=num1
else:
    gcd=num2
while True:
    if num1%gcd==0 and num2%gcd==0:
        print(gcd)
        break
    else:
        gcd-=1

'''
'''

num=11
rum=num
for i in range(2,num//2+1):
    if num%i==0:
        print("NOT A POLYPRIME")
        break
else:
    ans=0
    while num!=0:
        rem=num%10
        ans=ans*10+rem
        num//=10
    if ans==rum:
        print('polyprime')
    else:
        print('NOT')

'''
