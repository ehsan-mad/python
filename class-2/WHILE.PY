a=[-1,2,-3,4,-5,6]
result=0
i=0
while i<len(a):
    if a[i]<0:
       a[i]=0
    i+=1
print(a)      