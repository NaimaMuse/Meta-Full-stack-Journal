class Recipe:
    def __init__(self,dish,item,time)->None:
        self.dish = dish
        self.item = item
        self.time = time 
    def consents(self):
        print(self.dish + str(self.item) + str(self.time))
pizza = Recipe('pizza',['cheese','bread',],45)
pasta = Recipe('pasta',['peane','sauce',],55)
print(pizza.item)
print(pizza.consents())
