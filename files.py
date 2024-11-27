fobj=open('file.txt','r')
#print(fobj.read())
count=0
res=' '
for line in fobj:
    l=line.strip('\n')
    for ch in l:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' :
            res+=ch
            count+=1
print(res)
print(count)
            
