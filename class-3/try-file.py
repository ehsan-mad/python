

# with open("try-file.txt", "w") as rp:
#      print(rp.writelines(" Hello, \n"))
# with open("try-file.txt", "a") as rp:
    #  print(rp.writelines("\n Hello, damn \n"))

# with open("try-file.txt", "r") as rp:
#      print(rp.read())


try:
    with open("try.txt", "r") as rp:
        print(rp.read())
except FileNotFoundError:
    print("File not found")  
else:
    print("File found")
finally:
    print("Done")

def checkfile(filename):
    if not filename.endswith(".txt"):
        raise ValueError("Invalid file name")
    print("Valid file name")
try:
    checkfile("try.png")    
except Exception as e:
    print(e)