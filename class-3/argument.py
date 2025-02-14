def add(*args):
    print(args)
    return sum(args)
r=add(12,23,34,56,75,34,312,1231234,44)
print(r)


# keywords arguments

def keyword(fname,lname,age):
    print(f"i am {fname} {lname}.And the age of mine is {age}")
    
keyword(age=10,fname="jainga",lname="liu")    

# infinite keyword
def keys(**kwargs):
    print(kwargs)
    print(f"{kwargs['fname']} , {kwargs['lname']} , {kwargs['fol']} ")
keys(age=10,fname="jainga",lname="liu", fol="mangio")   