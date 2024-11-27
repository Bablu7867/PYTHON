'''
            'SELECTION SORT'

L=[9,6,-6,-1,7,11]
for ind1 in range(len(L)-1):
    
    val=ind1
    for ind2 in range(ind1+1,len(L)):
        if L[val]>L[ind2]:
            val=ind2

    L[val],L[ind1]=L[ind1],L[val]
print(L)

'''
