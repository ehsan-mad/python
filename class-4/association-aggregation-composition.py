# association

class Tech:
    def __init__(self,name):
        self.brand=name
class user:        
    def __init__(self,user,name):
        self.user=user
        self.name=name
    def info(self):    
        print(f"User:{self.user}\nBrand:{self.name.brand}")
        
obj=Tech("Asus")
obj1=user("bal",obj)
obj1.info()
        
#aggregation

class dept:
    def __init__(self,name):
        self.name=name
        
class uni:
    def __init__(self,name):
        self.name=name
        self.dpts=[]
    def adddept(self,dpt):
        self.dpts.append(dpt)
    def show_dep(self):
        return [dpt.name for dpt in self.dpts]
    
un1=uni("Abc")
dep=dept("nigga")
dep2=dept("gigga")
un1.adddept(dep)
un1.adddept(dep2)
print(un1.show_dep())


#composition
class Engine:
    def __init__(self,name):
        
        self.name=name

class car:
    def __init__(self,name,type):
        self.name=name
        self.type=Engine(type)
    def show_details(self):
        print(f"Name:{self.name} Type:{self.type.name}")
        
ob=car("NISSAN","VVTI")
ob.show_details()        
        