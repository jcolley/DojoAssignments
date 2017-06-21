class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def walk(self, num):
        while num != 0:
            self.health -= 1
            num -= 1
        return self

    def run(self, num):
        while num != 0:
            self.health -= 5
            num -= 1
        return self

    def displayHealth(self):
        print self.name, self.health
        return self

animal1 = Animal("Bob Marley").walk(3).run(2).displayHealth()


class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)

dog1 = Dog("Ruff").walk(3).run(2).displayHealth()


class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"
        return self

dragon1 = Dragon("Swooper").fly().displayHealth()