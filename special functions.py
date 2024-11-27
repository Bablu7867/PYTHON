'''

def mul(v):
    return v*2
#print(list(map(mul,'acg')))
#   or
obj=map(mul,'acg')
for ele in obj:
    print(ele)

'''
'''

def ele(n):
    if n%2==0:
        return 'EVEN'
    return 'ODD'
print(list(map(ele,[11,12,13,14,15])))
    
'''
'''

print(list(map(lambda ch : ch * 3 ,'abcd')))

'''
'''

print(list(map(lambda num:('EVEN' if num%2==0 else 'ODD'),[11,12,13,14])))

'''
'''

def con(c1,c2):
    return c1+c2
print(list(map(con,'abcd','msd7')))

'''
'''

print(list(map(lambda m1,m2:m1+m2,'mnop','pqrs')))

'''
'''

def ram(n):
    for ele in range(2,n//2+1):
        if n%ele==0:
            return 'NOT PRIME'
    return 'PRIME'
print(list(map(ram,[14,7,19,21,5])))

'''
'''

print('\n'.join(list(map(lambda val:'* '*val,range(1,5)))))

'''
'''

print('\n'.join(list(map(lambda val:'* '*val,range(5,0,-1)))))

'''
