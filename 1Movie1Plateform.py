def singleTonclass(arg):
    L=[]
    def Inner():
        if len(L)==0:
            obj=arg()
            L.append(obj)
        return L[0]
    return Inner

@singleTonclass
class Movie1():
    def __init__(self):
        self.maxtic=100
        #print(self.maxtic)

    def Booking(self):
        print(f'Available ticket is {self.maxtic}')
        reqtic=int(input('enter the number of ticket'))

        if reqtic<=self.maxtic:
            print('Ticket booked successfully..')
            self.maxtic-=reqtic
        else:
            print('Ticket not available')


def BookMyShow():
    user=Movie1()
    user.Booking()


BookMyShow()
print('-------------')
BookMyShow()
print('-------------')
BookMyShow()
print('-------------')
BookMyShow()
