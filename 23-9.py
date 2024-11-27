'''
S='abcdef'
print({ch:ch*(len(S)) for ch in S})
'''
'''
s='abcd'
print({s[ind]:s[ind]*(ind+1) for ind in range(len(s))})
'''
'''
s='engineering'
print({ch : s.count(ch) for ch in s if ch in 'aeiouAEIOU'})
'''
'''
print({ch : 'even' if ch%2==0 else  'odd' for ch in range(1,6)})
'''
'''
s='helLo'
print({s[ind]:s[:len(s)-ind] for ind in range(len(s))})
'''
