
# find second largest number
# num=[10,20,4,45,99]
# num.sort()
# l=num[-2]
# print(l)


#rotate to left to right by k steps
# num=[1,2,3,4,5]
# k=2
# k=k%len(num)
# r=num[-k:]+num[:-k]
# print(r)


# find missing num(1 to n)
# num=[1,2,4,5]
# n=len(num)+1
# total=n*(n+1)//2
# miss=total-sum(num)
# print(miss)

# move all zeros to end
# num=[0,1,0,3,12]
# res=[]
# for i in num:
#     if i!=0:
#         res.append(i)
#
# z=num.count(0)
# res.extend([0]*z)
#
# print(res)

# find pairs with given sum

num=[2,4,3,5,7,8]
target=7

pairs=[]

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==target:
            pairs.append((num[i],num[j]))

print(pairs)