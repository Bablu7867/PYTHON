'''def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
def strong(val):
    if val==0:
        return 0
    return fact(val%10)+strong(val//10)
num=145
print('Strong number' if strong(num)==num else 'Not Strong')

'''
'''
def Happy(val):
    if val==0:
        return 0
    return (val%10)**2 + Happy(val//10)
def var(n):
    if n<=9:
        return n==1 or n==7
    return var(Happy(n))

num=13
print('Happy number' if var(num) else 'Not Happy')# (or)var(num)==True

'''


def rev(n):
    if n==0:
        return 0
    return (n%10) * (10 ** (len(str(n))-1))+rev(n//10)
num=675
print(rev(num))
print('Palindrome' if rev(num)==num else 'Not Palindrome')
# (val%10) * pos + Rev(val//10,pos//10)
# print(Rev(num,10**(len(str(num))-1


