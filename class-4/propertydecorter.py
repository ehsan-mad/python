class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary #private property
        
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,new):
        self._salary=new
        
obj=Employee("saad",1000)
print(obj.salary)
obj.salary=2000
print(obj._salary)