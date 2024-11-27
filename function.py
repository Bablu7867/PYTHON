'''
def Palindrome(val,rev=0):
    while val!=0:
        rem=val%10
        rev=rev*10+rem
        val//=10
    return rev
def Prime(x):
    for den in range(2,x//2+1):
        if x%den==0:
            return False
    return True
def Palyprime(num):
    if Prime(num) and Palindrome(num)==num:
        return 'Palyprime'
    return 'Not Palyprime'
num=22
print(Palyprime(num))
'''
'''
def sq(num,res=0):
    while num!=0:
        rem=num%10
        res=res+rem**2
        num//=10
    return res
def val(x):
    while x > 9:
        x = sq(x)
    return x==1 or x==7
n=7
print('Happy' if val(n) else 'Not Happy')
'''
'''
def reverse(num,res=0):
    while num!=0:
        rem=num%10
        res=res*10 + rem
        num//=10
    return res
def prime(val):
    for dig in range(2,val//2+1):
        if val%dig==0:
            return False
    return True
f=13
hi=reverse(f)
print(hi)
print('EMIRP' if ((hi!=f) and prime(f) and prime(hi)) else 'Not EMIRP')
'''
num=134
val=str(num*1)+str(num*2)+str(num*3)
print(val)
for dig in range(1,10):
    if str(dig) not in val:
        print('Not a fascinating number')
        break
else:
    print('Fascinating number')
