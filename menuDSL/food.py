class Food:
    def __init__(self, id, name, food_type, price):
        self.id = id
        self.name = name
        self.food_type = food_type
        self.price = price
        self.ingredients=[]

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getFoodType(self):
        return self.food_type

    def getPrice(self):
        return self.price

    def add_ingredient(self,newIngredient):
        self.ingredients.append(newIngredient)