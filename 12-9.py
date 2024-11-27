'''
ele=[17,99,87,56]
ele.reverse()
print(ele)
'''
'''
ele=[17,99,87,56]
res=[]
for j in range(-1,-len(ele)-1,-1):
    res.append(ele[j])
print(res)
'''
'''
ele=[17,99,87,56]
res=[]
for j in range(len(ele)-1,-1,-1):
    res.append(ele[j])
print(res)
'''
'''
ele=[17,99,87,56]
ele1=ele[::-1]
print(ele1)
'''
'''
ele=[17,99,87,56]
res=[]
for e in ele:
    res=[e]+res
print(res)
'''
'''
k=[12,34,56,78,90,88]
for j in range(0,(len(k)//2)):
    k[j],k[-j-1]=k[-j-1],k[j]
print(k)
'''
'''
l=[1,2,3,0,1]
for ind in range(len(l)//2):
    if l[ind]!=l[-ind-1]:
        print('Not palindrome')
        break
else:
    print('Palindrome')
'''
'''
l=[1,2,3,0,1]
s=0
e=len(l)-1
while s<e:
    if l[s]!=l[e]:
        print('NOT PALINDROME')
        break
    s+=1
    e-=1
else:
    print('PALINDROME')
'''
'''
l=[14,15,20,7,6,11]
g=[]
for ch in l:
    c=0
    for v in range(1,ch+1):
        if ch%v==0:
            c+=1
    g.append(c)
print(g)
'''
'''
n=7893769491
res=0
while n!=0:
    rem=n%10
    if rem>1:
        for h in range(2,rem//2+1):
           if rem%h==0:
               break
        else:
            print(rem)
    n//=10
'''
