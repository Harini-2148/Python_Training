### SETS

# ## FIND UNIQUE ELEMENTS FROM TWO LISTS
# l1=[1,2,3,4]
# l2=[3,4,5,6]
# res=set(l1)  | set(l2)
# print(res)

## CHECK IF TWO LISTS HAVE COMMON ELEMENTS
l1=[1,2,3]
l2=[4,5,6]
common=set(l1)&set(l2)
if common:
    print("yes")
else:
    print("no")

