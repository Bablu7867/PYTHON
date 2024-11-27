'''

def SingleTon(arg):
    L=[]
    def inner():
        if len(L)==0:
            L.append(arg())
        return L[0]
    return inner
@SingleTon
class Movie1():
    def __init__(self):
        self.totaltic=200
    def Booking(self):
        reqtic=int(input('enter the number of ticket:'))
        if reqtic<=self.totaltic:
            print('Tickets are booked successfully..')
            self.totaltic-=reqtic
            print(f'Remaining tickets are : {self.totaltic}')
        else:
            print('Tickets out of range')
@SingleTon
class Movie2():
    def __init__(self):
        self.totaltic=200
    def Booking(self):
        reqtic=int(input('enter the number of ticket:'))
        if reqtic<=self.totaltic:
            print('Tickets are booked successfully..')
            self.totaltic-=reqtic
            print(f'Remaining tickets are : {self.totaltic}')
        else:
            print('Tickets out of range')
@SingleTon
class Movie3():
    def __init__(self):
        self.totaltic=200
    def Booking(self):
        reqtic=int(input('enter the number of ticket:'))
        if reqtic<=self.totaltic:
            print('Tickets are booked successfully..')
            self.totaltic-=reqtic
            print(f'Remaining tickets are : {self.totaltic}')
        else:
            print('Tickets out of range')
def BMyShow():
    print('1)Movie1 \n2)Movie2 \n3)Movie3')
    choice=int(input('Enter the movie Choice:'))
    if choice==1:
        user=Movie1()
        user.Booking()
    elif choice==2:
        user=Movie2()
        user.Booking()
    elif choice==3:
        user=Movie3()
        user.Booking()
    else:
        print('check your eyes and book correct movie')
user1=BMyShow()
print('-'*30)
user2=BMyShow()
print('-'*30)
user3=BMyShow()
print('-'*30)
user4=BMyShow()
print('-'*30)
user5=BMyShow()
print('-'*30)
user6=BMyShow()
print('-'*30)
user7=BMyShow()

'''

def SingleTon(arg):
    L=[]
    def inner():
        if len(L)==0:
            L.append(arg())
        return L[0]
    return inner
@SingleTon
class Vettayan():
    
    def __init__(self):
        self.totaltic=200
    def Booking(self):
        reqtic=int(input('enter the number of ticket:'))
        if reqtic<=self.totaltic:
            print('Tickets are booked successfully..')
            self.totaltic-=reqtic
            print(f'Remaining tickets are : {self.totaltic}')
        else:
            print('Tickets out of range')
def BMyShow():
    user=Vettayan()
    user.Booking()
def PhonePay():
    user=Vettayan()
    user.Booking()
def GooglePay():
    user=Vettayan()
    user.Booking()
def PayTM():
    user=Vettayan()
    user.Booking()
user1=BMyShow()
print('-'*30)
user2=PayTM()
print('-'*30)
user3=GooglePay()
print('-'*30)
user4=BMyShow()
print('-'*30)
user5=PhonePay()
print('-'*30)
user6=PayTM()
