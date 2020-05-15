#Problem: Given an array numbers of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
#Find all unique triplets in the array which gives the sum of zero.

#questions:
#Q: Time compelxity limit?
#Q: Are they ordered?
#Q: What happens if none of the numbers add up to 0


#assumptions:
#A: All integers 
#A: No time complexity limit
#A: Not sorted

#Runtime should be O(n^2) 
def threeSum(nums):
    triples = []         
    nums = sorted(nums)
    
    x = 0
    while x<len(nums):
        right = len(nums)-1
        left = x+1
        while left<right:
            if left == x:
                left+=1
                continue
            elif right == x:
                right-=1
                continue

            if nums[x]+nums[left]+nums[right] == 0:
                temp = [nums[x], nums[left], nums[right]]
                temp.sort()
                triples.append(temp)     
                left+=1
                right-=1    
            elif nums[x]+nums[left]+nums[right] < 0:
                left+=1
            else:
                right-=1
        x+=1

    x = 0
    while x < len(triples):
        y=x+1
        while y < len(triples):
            if triples[y] == triples[x]:
                del triples[y]
            else:
                y+=1    
        x+=1

    return triples

print(threeSum([-1,0,1,2,-1,-4]))
