class Food:
    def __init__(self, id, name, food_type, price, image):
        self.id = id
        self.name = name
        self.food_type = food_type
        self.price = price
        self.ingredients=[]
        self.image = image

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

    def get_image(self):
        return self.image