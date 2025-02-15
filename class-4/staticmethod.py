class school:
    school_name="BBschool"
    
    @staticmethod  #static method cannot access the class variable and the instance self or variable
    def grade(marks):
        if marks>10:
            return "A+"
        else:
            return "FAIL"
        
OBJ1=school()
print(OBJ1.grade(11))
