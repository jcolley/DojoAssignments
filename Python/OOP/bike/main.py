class Bike(object):
    def __init__(self, name, price=0, max_speed=0):
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.name
        print "Price: ", self.price
        print "Max Speed: ", self.max_speed
        print "Total Miles", self.miles
        print "=" * 40 + "\n"
        return self

    def ride(self, num):
        while num != 0:
            print self.name, "Riding"
            self.miles += 10
            num -= 1
            return self

    def reverse(self, num):
        while num != 0:
            print self.name, "Reversing"
            self.miles -= 5
            num -= 1
        if self.miles < 0:
            self.miles = 0
        return self


bike1 = Bike("Bike1", 200, 25)
bike2 = Bike("Bike2", 250, 35)
bike3 = Bike("Bike3", 350, 75)

bike1.ride(3).reverse(1).displayInfo()
bike2.ride(2).reverse(2).displayInfo()
bike3.reverse(3).displayInfo()