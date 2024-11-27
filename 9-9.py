'''

ms='MaHi >7 @f$ _3?'
res=''
for g in ms:
    if g.isalnum():
        pass
    else:
        res+=g
print(res)

'''
'''

ms='MaHi>7@f$_3?'
print(ms)
res = ""
for ch in ms:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z' or '0' <= ch <= '9':
        pass
    else:
        res += ch

print(res)

'''
'''

ms='MaHi>7@f$_3?'
res = ""
for ch in range(len(ms)):
    if 'A' <= ms[ch] <= 'Z' or 'a' <= ms[ch] <= 'z' or '0' <= ms[ch] <= '9':
        pass
    else:
        res += ms[ch]

print(res)

'''
'''

s='MahIbabLU'
res=''
for ch in s:
    if 'a'<=ch<='z':
        res+=chr(ord(ch)-32)
    else:
        res+=ch
print(res)

'''
'''

s='MahIbabLU'
res=''
for ch in s:
    if 'a'<=ch<='z':
        res+=chr(ord(ch)-32)
    else:
        res+=chr(ord(ch)+32)
print(res)

'''
'''

s='MahIbabLU'
res=''
for ch in s:
    if 'A'<=ch<='Z':
        res+=chr(ord(ch)+32)
    else:
        res+=ch
print(res)

'''
n=int(input())
sp=len(n)
for line in range (0,n):
    for n in range(
