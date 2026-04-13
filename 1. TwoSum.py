class Solution(object):
    def twoSum(self, nums, target):
        op=[]
        l=len(nums)
        for i in range(0,l):
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    op.append(i)
                    op.append(j)
                    return op
                    exit(0)
                else:
                    pass
        
s=Solution()
nums=[2,3,11,15]
target=9
print(s.twoSum(nums,target))
