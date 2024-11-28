'''

H=[8,3,4,7,1,6,7,18]
target=int(input())
for jar in range(len(H)):
    if H[jar]==target:
        print(jar)
        break
else:
    print(-1)

'''
'''

H=[8,3,4,7,1,6,7,18]
target=int(input())
jar=0
while len(H)!=jar:
    if H[jar]==target:
        print(jar)
        break
    else:
        jar+=1
else:
    print(-1)

'''
