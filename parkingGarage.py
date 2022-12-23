class ParkingGarage():

    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    currentTicket = {}

    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()
        self.currentTicket[self.tickets[-1]+1] = 'Unpaid'
        print(self.tickets)
        print(self.parkingSpaces)
        print(self.currentTicket)
    
    def payForParking(self):
        while True:
            payment =  input ("Your ticket was $5. Please type 5 to pay")
            if payment != str (5):
                print("Please proceed with payment")
            else:
                self.currentTicket[self.tickets[-1]+1] = 'Paid'
                print(self.currentTicket)
                print("Thank you! Your ticket has been paid.  You have fifteen to leave the garage.  Have a nice day!")
                break
  
    def leaveGarage(self):
        while True:
            if self.currentTicket[self.tickets[-1]+1] == 'Paid':
                self.tickets.append(self.tickets[-1] + 1)
                self.currentTicket.popitem()
                print('The garage door is opening.  You are free to leave.  ')
                print(self.currentTicket)
                print(self.tickets)
                break
            else:
                while True:
                    payment =  input ("Your ticket was $5. Please type 5 to pay")
                    if payment != str (5):
                        print("Please proceed with payment")
                    else:
                        self.currentTicket[self.tickets[-1]+1] = 'Paid'
                        print(self.currentTicket)
                        print("Thank you! Your ticket has been paid.  You have fifteen minutes to leave the garage.  Have a nice day!")
                        break


    def run(self):
        while True:
            self.car = input('What would you like to do?  Buy, Pay,Leave or Quit?')
            if self.car.lower() == 'buy':
                self.takeTicket()
            elif self.car.lower() == 'leave':
                self.leaveGarage()
            elif self.car.lower() == "pay":
                self.payForParking()
            elif self.car.lower() == "quit":
                print("Thank you for using our Garage!")
                break
            else:
                print("Invalid entry.  Please Try Again.")


x = ParkingGarage()
x.run()
        
