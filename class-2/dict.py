# no indexing
# keys immutable
a={1:"rahim",2:"karim",3:"rifat",4:[1,2,3],5:{1,2,3,4,5,6,56}}

for i in a.items():
    print(i)
    
aa=[1,2,3,4,5,6,7,8]
bb=["Rahim ","karim","ivsss","nn","nuts,","ball","hhhhh","lol"]

gg=dict(zip(bb,aa))

for k,v in a.items():
    print(f"key {k} : value {v}")
    
for k in gg.values():
    print(k)
    
for k in gg.keys():
    print(k)
    
print(gg["Rahim "])
print(a[1])