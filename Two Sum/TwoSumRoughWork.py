nums=[1,2,3,4,5]
target = 7

# Approach 1:
# print(type(nums)) #<class 'list'>

# print(len(nums)) # 5

# for i in range (6):     initialize with 0 range end with num-1
#     print(i)
# output : 0  1   2   3   4   5 

# for i in range (2,4):
#     print(i)
# output : 2   3

# for i in range (len(nums)):
#     print(i)
# output : 0  1   2   3   4  
 
# for i in range (len(nums)):
#     for j in range(i+1, len(nums)):           range(1,5)  range(2,5)  range(3,5)  range(4,5)
#         print(j)
# output : 1   2   3   4    2   3   4   3   4   4

# for i in range (len(nums)):
#     for j in range(i+1, len(nums)):   
        # print(nums[i]+nums[j])

        # print(nums[i])  
        # print(nums[j])        
# output:
# value of i : 1    1   1   1   2   2   2   3   3   4
# value of j : 2    3   4   5   3   4   5   4   5   5
# val of i+j : 3    4   5   6   5   6   7   7   8   9


# Approach 2:

# for i in range (len(nums)):             #  O(n)
#     need = target-nums[i]
#     print(need)

# output: 6   5   4   3   2 

# def twoSum(nums:list[int],target:int):
#     for i in range (len(nums)):                         #  O(n)
#         need = target-nums[i]
#         if(need in nums and nums.index(need)!=i):       #  O(n)
#             return(i, nums.index(need))

    
# print(twoSum(nums,target))
# Output : [0, 1]   TC: O(n^2) SC: (1)

# Approach 3:
# d= dict()
# for i in range (len(nums)):         
#     d[nums[i]]=i
    
# print(d)
# Output: {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}

