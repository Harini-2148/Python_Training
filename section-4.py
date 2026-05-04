# ## DICTIONARIES
#
# ## COUNT FREQUENCY OF ELEMENTS
# num=[1,2,2,3,3,3]
# f={}
# for n in num:
#     if n in f:
#         f[n]+=1
#     else:
#         f[n]=1
# print(f)

# FIND KEY WITH MAXIMUM VALUE
# d={"a":10,"b":25,"c":15}
# max=max(d,key=d.get)
# print(max)


# MERGE TWO DICTIOARIES
# d1 = {"a": 1, "b": 2}
# d2 = {"b" : 3, "c" : 4}
#
# d1.update(d2)
# print(d1)

# INVERT A DICTIONARY
d={"a":1,"b":2}
invt={}
for key,value in d.items():
    invt[value]=key
print(invt)

