#single inheritance
# class Grandfather:
#     def __init__(self,color,name):
#         self.name=name
#         self.color=color
#     def info_grad(self):
#         print( "This shits granddad")
    
# class Father(Grandfather):
#     def __init__(self,hobby,color,name):
#         super().__init__(color,name)
#         self.hobby=hobby
       

# f=Father("wow","gg","Red")
# print(f.name,f.color)


#multiple inheritance

# class Grandfather:
#     def __init__(self,color,name):
#         self.name=name
#         self.color=color
#     def info_grad(self):
#         print( "This shits granddad")
    
# class Father(Grandfather):
#     def __init__(self,hobby):
#         self.hobby=hobby
#     def info_fat(self):
#         return "This is dad"
# class Children(Father,Grandfather):
#     def __init__(self,style,color,name,hobby):
#         Grandfather.__init__(self,color,name)
#         Father.__init__(self,hobby)
#         self.style=style
# c=Children("NIGGA","rED","ANY","BAD")
# print(c.style,c.hobby,c.color,c.name, c.info_grad(),c.info_fat())


# multilevel inheritance
class Grandfather:
    def __init__(self,color,name):
        self.name=name
        self.color=color
    def info_grad(self):
        print( "This shits granddad")
    
class Father(Grandfather):
    def __init__(self,hobby,color,name):
        super().__init__(color,name)
        self.hobby=hobby
    def info_fat(self):
        return "This is dad"
class Children(Father,Grandfather):
    def __init__(self,style,color,name,hobby):
        super().__init__(color,name,hobby)
        
        self.style=style
c=Children("NIGGA","rED","ANY","BAD")
print(c.style,c.hobby,c.color,c.name, c.info_grad(),c.info_fat())

#Hierarchical inheritance

# class car():
#     def engine(self):
#         print("This is a car")
        
# class Truck(car):
#     def horn(self):
#         print("this horn is bad")
# class bike(car):
#     def tires(self):
#         print("tHIS HAS 4 WHEELS")
        
# TR=Truck()
# TR.horn()
# TR.engine()                
# BK=bike()
# BK.engine()
# BK.tires()
    

#Hybrid inheritance

class diffshape():
    def moreshape(self):
        print("onek gula shape") 
        
class polygon(diffshape):
    def shape(self):
        print("FIVE SHAPES")
class Rect(polygon):
    def __init__(self,h,w):
        self.h=h
        self.w=w
    def calc(self):
        
        return self.h*self.w
    
oo=Rect(10,20)
print(oo.calc())    
oo.shape()
oo.moreshape()

  