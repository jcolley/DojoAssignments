class Car(object):
    def __init__(self, price=0, speed=0, fuel="Empty", mileage=0):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0
        self.display_all()

    def setTax(self, tax):
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        info = "Price: "+str(self.price)+"\n"
        info += "Speed: "+str(self.speed)+"mph\n"
        info += "Fuel: "+str(self.fuel)+"\n"
        info += "Mileage: "+str(self.mileage)+"mpg\n"
        info += "Tax: "+str(self.tax) + "\n"

        print info

car1 = Car(2000, 35, "Full", 15)
car2 = Car(4000, 5, "1/2 Tank", 200)
car3 = Car(11000, 60, "1/4 Tank", 3000)
car4 = Car(5000, 30, "1/16 Tank", 1)
car5 = Car(1200, 10, "Empty", 400)
car6 = Car(41308, 90, "1/2 Tank", 40000)
