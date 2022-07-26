def productOfArray(nums,i):
        if(i==len(nums)):return 1
        return nums[i]*productOfArray(nums,i+1)

print(productOfArray([1,2,3,4],0))