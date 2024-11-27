L=['hi','lets','start','discussion']
l=' '.join(L)
print(l)
s={}
for k in l:
    if k not in s:
        s[k]=1
    else:
        s[k]+=1
for o,p in s.items():
    print(f'{o}={p}')
