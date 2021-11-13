tup=(1,2,3,4,5)
tup=tup+(6,)
print(tup)
tup=tup[:5]+(9,)+tup[:5]
print(tup)
tmp=list(tup)
tmp.append(10)
tup=tuple(tmp)
print(tup)

