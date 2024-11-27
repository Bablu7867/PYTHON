'''


l=[1,3,4]
r=[2,4,6,6]
K=[0]*((len(l)+len(r)))
ind,li,ri=0,0,0
while li<len(l) and ri<len(r):
    if l[li]>r[ri]:
        K[ind]=r[ri]
        ind+=1
        ri+=1
    else:
        K[ind]=l[li]
        ind+=1
        li+=1
while ri<len(r):
    K[ind]=r[ri]
    ind+=1
    ri+=1
while li<len(l):
    K[ind]=l[li]
    ind+=1
    li+=1
print(K)


'''
L=[1,420,3,4,100,7,18,8]
def divide(L):
    if len(L)>1:
        av=len(L)//2
        left=L[:av]
        right=L[av:]
        divide(left)
        divide(right)
        merge(L,left,right)
def merge(L,left,right):
    ind,li,ri=0,0,0
    while li<len(left) and ri<len(right):
        if left[li]>right[ri]:
            L[ind]=right[ri]
            ind+=1
            ri+=1
        else:
            L[ind]=left[li]
            ind+=1
            li+=1
    while li<len(left):
        L[ind]=left[li]
        ind+=1
        li+=1
    while ri<len(right):
        L[ind]=right[ri]
        ind+=1
        ri+=1
divide(L)
print(L)
