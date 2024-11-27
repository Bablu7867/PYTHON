num=int(input())
spaces=0
for den in range(num,0,-1):
    for spa in range(spaces):
        print(' ',end=' ')
    for st in range(den):
        print('*',end=' ')
    print()
    spaces+=1
    
