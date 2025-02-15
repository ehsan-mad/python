class Employee:
    company_name="Bhalo company"  #class variable
    
    def __init__(self,name,salary): 
        self.name=name       #instance variable
        self.salary=salary
        
    def getinfo(self):  #instance method
        print(f"Employee name {self.name} and salary {self.salary}")
        
    @classmethod
    def change_company_name(cls,name): #class method
        cls.company_name = name
        
     
obj1=Employee("lal",1000)
obj1.getinfo()
Employee.change_company_name("balll")       
print(obj1.company_name)       