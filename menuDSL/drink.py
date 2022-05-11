class Drink:
    def __init__(self, id, name, drink_type, price):
        self.id = id
        self.name = name
        self.drink_type = drink_type
        self.price = price

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getDrinkType(self):
        return self.drink_type

    def getPrice(self):
        return self.price