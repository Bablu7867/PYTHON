'''

am=list(map(int,input().split()))
pm=list(map(int,input().split()))
print(list(map(lambda a,b: a+b,am,pm)))


'''
'''

def add(am,pm):
    return int(am+pm)
print(list(map(add,[10,12,3],[-3,-5,4])))

'''
'''

def even(val):
    if val%2==0:
        return 'Even'
print(list(filter(even,range(1,10))))

'''
'''

def even(val):
    for ele in range(2,val//2+1):
        if val%ele==0:
            return 
    return True
print(list(filter(even,range(10,20))))

'''
'''

def arm(val,res=0):
    num=val
    count=len(str(val))
    while val>0:
        rem=val%10
        res=res+rem**count
        val//=10
    if num==res:
        return True
print(list(filter(arm,range(1,50))))

'''
'''

def happy(num):
    while num>9:
        res=0
        while num!=0:
            rem=num%10
            res=res+rem**2
            num//=10
        num = res
    if res==1 or res==7:
        return True
print(list(filter(happy,range(100,200))))

'''
def strong(val):
    hi=val
    ans = 0
    while val!=0:
        rem=val%10
        fact = 1
        for den in range(1,rem+1):
            fact*=den
        ans+=fact
        val//=10
    return hi==ans
print(list(filter(strong,range(0,100))))
