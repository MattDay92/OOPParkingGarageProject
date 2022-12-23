class ParkingGarage():

    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    currentTicket = {}

    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()
        self.currentTicket[self.tickets[-1]+1] = False
        print(self.tickets)
        print(self.parkingSpaces)
        print(self.currentTicket)
    
    def payForParking(self):
        while True:
            payment =  input ("your ticket was $5. Please type 5 to pay")
            if payment != str (5):
                print("please proceed with payment")
           

            else :  
                print("Thank you! Have a nice day!")
                break
    



    def leaveGarage(self):
        self.tickets.append(self.tickets[-1] + 1)
        print(self.tickets)


    def run(self):
        while True:
            self.car = input('What would you like to do?  Buy, Pay,Leave or Quit?')
            if self.car.lower() == 'buy':
                self.takeTicket()
            elif self.car.lower() == 'leave':
                self.leaveGarage()
            elif self.car.lower() == "pay":
                self.payForParking()
            else:
                print("Thank you for using our Garage!")
                break


x = ParkingGarage()
x.run()
        
