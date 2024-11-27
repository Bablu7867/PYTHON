'''

class V1():
    def __init__(self,name,mailID):
        self.name  = name
        self.mailID = mailID
    def details(self):
        print(f'{self.name}')
        print(f'{self.mailID}')
class V2(V1):
    def __init__(self,name,mailID,Aadhar,MobNo):
        V1.__init__(self,name,mailID)
        self.Aadhar = Aadhar
        self.MobNo  = MobNo
    def details(self):
        V1.details(self)
        print(f'{self.Aadhar}')
        print(f'{self.MobNo}')
class V3(V2):
    def __init__(self,name,mailID,Aadhar,MobNo,PAN,pin):
        V2.__init__(self,name,mailID,Aadhar,MobNo)
        self.PAN  = PAN
        self.pin  = pin
    def details(self):
        V2.details(self)
        print(f'{self.PAN}')
        print(f'{self.pin}')
user2=V2('mahi','bablumahi73@gmail.com',760520464460,7893769491)
user2.details()


'''
