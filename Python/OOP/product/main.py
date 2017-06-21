class Product(object):
    def __init__(self, price, name, weight, brand, cost, status="for sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, num):
        self.total = self.price + self.price * num
        return self.total

    def Return(self, reason):
        if reason == "defective":
            self.status = reason
        if reason == "unopened":
            self.status = "for sale"
        if reason == "opened":
            self.status = "used"
            self.price += self.price * .20
        return self

    def displayInfo(self):
        print "Name: ", self.name
        print "Brand: ", self.brand
        print "Price: ", self.price
        print "Weight: ", self.weight
        print "Cost: ", self.cost
        print "Status: ", self.status
        print "Total: ", self.total
        print "=" * 40 + "\n"
        return self

product1 = Product(30.0, "Shirt", 15, "Froot", 12.0)

product1.addTax(.09)
product1.displayInfo()
