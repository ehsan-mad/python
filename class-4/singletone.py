class singletone:
    _instance=None
    def __new__(cls):
        if cls._instance==None:
            print("1st ob is created")
            cls._instance=super(singletone,cls).__new__(cls)
            
        return cls._instance
ob=singletone()
ob2=singletone()
print(ob is ob2)

#just object 1 barei create hbe 2nd time create hbe na
