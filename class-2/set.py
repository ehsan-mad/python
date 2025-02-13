# no indexing unordered
# no update value
# no duplicates

a=[1,1,3,2,2,6,5,5,9,10]
s=set(a)
b=[2,33,44,5,66,66,43,33,5,3,5,67]
g=set(b)
c=s.union(g)
d=s.intersection(g)
print(c)
print(d)