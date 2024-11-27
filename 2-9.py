'''

def Binary(num,pos=1,res=0):
    while num !=0:
        rem = num % 2
        res = res + rem * pos
        pos *= 10
        num //= 2
    return res

print(list(map(Binary,range(10,21))))

'''
'''

print('\n'.join(list(map(lambda sp,st: '  ' * sp + '* ' * st,range(0,4),range(4,0,-1)))))

'''
'''

print('\n'.join(list(map(lambda sp,st: '  ' * sp + '* ' * st,range(3,-1,-1),range(1,5)))))

'''
'''

print('\n'.join(list(map(lambda sp,st: '  ' * sp + '* ' * st,range(3,-1,-1),range(1,4*2,2)))))

'''
'''

num=int(input('ENTER VALUE:'))
print('\n'.join(list(map(lambda val: (str(val) + ' ') * val,range(1,num+1)))))

'''
'''

num1=int(input())
num2=int(input())
print(num1+num2)

'''
'''

L=[]
len=int(input())
for den in range(len):
    ele=int(input('Enter value:'))
    L.append(ele)
print(L)

'''
'''

def con(val):
    return int(val)
print(list(map(con,input().split())))

                            OR
                            
print(list(map(int,input().split())))

'''
