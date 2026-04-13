def removeele(nums, val):
   for i in range(7):
      if nums[i]==val:
         nums[i]="_"
      else:
         continue
def push(num,sym):
   for i in range(7):
      if num[i]==0:
          num[i]=sym
      else:
          continue
nums = [1,2,3,4,3,2,1]
val=3
print(nums)
l=0
num=[0,0,0,0,0,0,0]
removeele(nums,val)
for i in range(7):
   if nums[i]=="_":
      pass
   else:
      num[l]=nums[i]
      l=l+1
push(num,"_")
print(num)
