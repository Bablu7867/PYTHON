'''

s='happy'
h=len(s)
for j in range(0,h+1):
    for g in range(j+1,h+1):
        print(s[j:g])

'''
'''

s='happy'
h=len(s)
for j in range(0,h+1):
    for g in range(j+1,h+1):
        res = ""
        for k in range(j,g):
            res+=s[k]
        print(res)

'''
'''

s='happy'
h=len(s)
for j in range(0,h+1):
    for g in range(j+1,h+1):
        if s[j:g] == s[j:g][::-1]:
            print(s[j:g])

'''
'''

s='programming'
for ch in s:
    print(ch,s.count(ch))
    s.replace(ch,'')
    
'''
'''

s='programming'
s_d = ""
for ch in s:
    if ch not in s_d:
        s_d += ch
    

for ch in s_d:
    print(ch,":",s.count(ch))

'''

s = 'engineering'
dict = {}
for ch in s:
    if ch not in dict:
        dict[ch] = 1
    else:
        dict[ch] += 1
for j,v in dict.items():
    print(f'{j} = {v}')
    
