nums=[2,3,4,5,6]
target=10
dict={}
for i in range(len(nums)):
    rem=target-nums[i]
    if rem in dict:
        print([dict[rem],i])
    dict[nums[i]]=i
    print(dict)