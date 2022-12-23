class ParkingGarage():

    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    currentTicket = {}

    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpaces.pop()
        print(self.tickets)
        print(self.parkingSpaces)

    
    def payForParking(self):
        pass



    def leaveGarage(self):
        self.tickets.append(self.tickets[-1] + 1)
        print(self.tickets)


    def run(self):
        while True:
            self.car = input('What would you like to do?  Buy, Pay, or Leave?')
            if self.car.lower() == 'buy':
                self.takeTicket()
            elif self.car.lower() == 'leave':
                self.leaveGarage()
            else:
                break


x = ParkingGarage()
x.run()
        
