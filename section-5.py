## COMBINED

## GROUP ELEMENT BY FREQUENCY
# num=[1,1,2,2,2,3,3]
# res={}
# for n in num:
#     if n in res:
#         res[n].append(n)
#     else:
#         res[n]=[n]
# print(res)

## FIND FIRST NON-REPEATING ELEMENT
# num=[4,5,1,2,0,4]
# for n in num:
#     if num.count(n)==1:
#         print(n)
#         break

## FLATTEN NESTES LIST

num=[[1,2],[3,4],[5]]
res=[]
for s in num:
    for i in s:
        res.append(i)
print(res)