class Ingredient:
    def __init__(self, id, name, fasting):
        self.id = id
        self.name = name
        self.fasting = fasting
        self.food=[]

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getFasting(self):
        return self.fasting