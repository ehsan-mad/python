class car:
    # def __init__(self):
    #     self.model = ""
    #     self.brand = ""
        
    # default constructor
    # def __init__(self,model,brand):
    #     self.model=model
    #     self.brand=brand
    
    # default parameterized constructor
    
    milage=100  #class variable
    
    def __init__(self,model="gwagon",brand="mercedes"):
        self.brand=brand  #instance variable
        self.model=model
    
        
# car1= car()
# car1.model = "corolla"  # Corrected assignment
# car1.brand = "Toyota"   # Corrected assignment
# print(car1.brand)  # Print both brand and model
# # print(car1.model)
# car2=car("x-trail","Nissan")
# print(car2.model,car2.brand)

car3=car()
print(car3.brand,car3.model,car3.milage)