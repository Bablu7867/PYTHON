'''

from functools import reduce
print(reduce(lambda v1,v2:v1+v2,range(1,6)))

'''
'''

from functools import reduce
n=6
print(reduce(lambda v1,v2:v1*v2,range(1,n+1)))

'''
'''

from functools import reduce
n=0
print(reduce(lambda v1,v2:v1+v2,range(1,n+1),1))

'''
'''

val='Mahi77'
ret=''
for ch in range(-1,-(len(val)+1),-1):
    ret+=val[ch]
print(ret)

'''
'''

val='Mahi77'
ret=''
for ch in range((len(val)-1),-1,-1):
    ret+=val[ch]
print(ret)

'''
'''

M='MAHI'
rev=''
for l in M:
    rev=l+rev
print(rev)

'''
'''

a,b=20,30
c=a
a=b
b=c
print(a,b)

'''
'''

a,b=20,30
a,b=b,a
print(a,b)

'''
'''

a,b=30,7
a=a+b
b=a-b
a=a-b
print(a,b)

'''
'''

a,b=3,7
a=a*b
b=a//b
a=a//b
print(a,b)

'''
'''

if bin(7)[-1]==1:
    print('EVEN')
else:
    print('ODD')

'''
'''

num=77
if num==(num//2)*2:
    print("EVEN")
else:
    print("ODD")

'''
'''

num=9
for j in range(1,11):
    print(f'{num} * {j} = {num*j}')

'''
