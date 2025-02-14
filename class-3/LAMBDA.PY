def mul(x):
    return x*x

print(mul(2))

square=lambda a : a*a
print(square(12))

# map
l=[1,2,3,4,5,6,6,7,7,8,7]
gg=tuple(map(lambda x: x*x, l)) #tuple list 2 tai convert kra jai

print(gg)

# filter
ff=tuple(filter(lambda y : y%2==0  , l)) #tuple list 2tai convert kra jai
print(ff)