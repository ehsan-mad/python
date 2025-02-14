# no input no return
def no_input():
    print("gg")
no_input()   
# input no return

def inp(a):
    print(a,"ggs")
inp(a="hello")    

#input return

def inpret(a,b=9):
    return a+b
a=inpret(5,7)
b=inpret(5)
print(a,b)

# no input return

def noinpret():
    return "wow"
i=noinpret()
print(i)