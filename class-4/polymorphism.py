# method overriding
class Grand:
    def greet(self):
        print("this is grand")
        
class Father(Grand):
    def greet(self):    #SAME METHOD CALLING
        print("this is father")
class son(Father):
    def greet(self):  #SAME METHOD CALLING
        print("This is son")
        
G=Grand()
F=Father()
S=son()
G.greet()                
F.greet()
S.greet()

#method overloading

class shape:
    def change(self,a,b=10):
        return a*b
    
s=shape()
print(s.change(10,200))
print(s.change(10))
        
