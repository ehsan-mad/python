class Computer:
    def __init__(self,cpu,storage,ram):
        self.cpu=cpu
        self.storage=storage
        self.ram=ram
        
    def __str__(self):
      return f"{self.cpu}, {self.storage}, {self.ram}"
        
class Builder:
    def __init__(self):
        self.cpu=None
        self.storage=None
        self.ram=None
        
    def set_cpu(self,cpu):
        self.cpu=cpu
        return self
    def set_ram(self,ram):
        self.ram=ram
        return self
    def set_storage(self,storage):
        self.storage=storage
        return self       
    def build(self):
        return Computer(self.cpu,self.ram,self.storage)
obj=Builder().set_cpu("Intel").set_ram("8gb").set_storage("500gb").build()
#set=obj    
print(obj)