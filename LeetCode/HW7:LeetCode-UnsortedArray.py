#Problem: Given an unsorted integer array, find the smallest missing positive integer.

#Q: Negatives?
#Q: What happens if theyre all the same number
#Q:What should it return in a list of all negatives


def firstMissingPositive(nums):
        nums = sorted(nums)
        smallest = 1 
        for x in range(len(nums)):
            if nums[x] > 0:
                if nums[x]<=smallest:
                    if len(nums)>1 and nums[x] == nums[x-1] and x!=0:
                        continue
                    smallest+=1
        return smallest
                

print(firstMissingPositive([1,1]))
#Var table:
#nums       | [1,2,0], [0,1,2]
#smallest   | 1, 2
#x          | 0, 1
#nums[x]    | 0, 1