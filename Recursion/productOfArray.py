def productOfArray(nums):
        if(len(nums)==0):return 1
        return nums[0]*productOfArray(nums[1:])

print(productOfArray([1]))