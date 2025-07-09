#Approach 1
nums = [6,4,7,2,3,4,8,6,3,5]
target = 10

# def twoSum(nums:list[int],target:int):
#     for i in range (len(nums)):             #  O(n)
#         for j in range(i+1, len(nums)):     #  O(n)
#             if(nums[i]+nums[j]==target):
#                 return[i,j]

# print(twoSum(nums,target))
# Output : [0, 1]   TC: O(n^2) SC: (1)

#Approach 2

#     for i in range (len(nums)):                       #  O(n)
#         need = target-nums[i]
#         if(need in nums and nums.index(need)!=i):     #  O(n) List Lookup
#             return(i, nums.index(need))
        
# print(twoSum(nums,target))
# Output : [0, 1]   TC: O(n^2) SC: (1)

# Approach 3: Hash Table / Dictionary

def twoSum(nums:list[int],target:int):
    d= dict()
    for i in range (len(nums)):             
        d[nums[i]]=i
    for i in range (len(nums)):                           #  O(n)
        need = target-nums[i]
        if(need in d.keys() and nums.index(need)!=i):     #  O(1) Dict Lookup
            return[i, nums.index(need)]

print(twoSum(nums,target))

# Output : [0, 1]   TC: O(n) SC: (n)
