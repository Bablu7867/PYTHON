'''

car='EYE'
bike=''
for jar in range(-1,-(len(car)+1),-1):
    bike=bike+car[jar]
if car==bike:
    print('PALINDROME')
else:
    print('NOT A PALINDROME')

'''
'''

s = 'malayalam'
for ind in range(0,len(s)//2):
    if s[ind] != s[-ind-1]:
        print('Not a palindrome')
        break
else:
    print('Palindrome')

'''
'''

var='racecar'
bike=''
hi=len(var)-1
s = 0
while hi>s:
    if var[s]!=var[hi]:
        print("NOT PALINDROME")
        break
    s += 1
    hi -= 1
else:
    print("PALINDROME")
    
'''
'''

var='racecar'
ind=0
while ind!=len(var)//2:
    if var[ind]!=var[-ind-1]:
        print('not')
        break
    ind+=1
else:
    print('Palindrome')

'''
'''

v = ('a','e','i','o','u')
s = 'developer'
for ch in s:
    if ch in v:
        print(ch, end=' ')

'''
'''

v = "aeiou"
s = 'FlASh is micro'
for ch in s:
    if ch.lower() in v:
        print(ch, end='')

'''
'''

v='developers'
s=''
for ind in range(0,len(v)):
    if v[ind] in 'aeiouAEIOU':
        s+=v[ind]
print(s)

'''
'''

s='deVeLoper'
j=''
for ch in s:
    if ch.isupper():
        j+=ch
print(j)

'''
'''

s='deVeLoper'
j=''
for ch in s:
    if ch.islower():
        j+=ch
print(j)

'''
'''
s='deVeLoper'
j=''
for ch in s:
    if ch>='a' and ch<='z':
        j+=ch
print(j)
'''
s = 'dEvElOpEr'
for ch in s:
    if 

