'''
            HAPPY NUMBER

num=int(input())
ms=num
while num>9:
    res=0
    while num !=0:
        rem=num%10
        res=res+rem**2
        num=num//10
    num=res
if num==1 or num==7:
    print(f'{ms} is a happy number')
else:
    print(f'{ms} is not a happy number')

'''


            #TECH NUMBER

num = 2025
if len(str(num))%2==0:
    fp = num // (10**(len(str(num))//2))
    sp = num % (10**(len(str(num))//2))
    if num == ((fp+sp)**2):
        print('is a tech number')
    else:
        print('is not a tech number')
else:
    print('not possible to check')
