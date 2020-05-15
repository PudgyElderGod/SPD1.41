#Problem: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

#Q: Sorted or unsorted?
#Q: Can numbers repeat more than once?

#A: Unsorted
#A: Each number only repeats once.

def find_single(numbers):
    numbers = sorted(numbers)    #1 loop, O(n)
    for x in range(0, len(numbers), 2):
        if x == len(numbers)-1:
            return numbers[x]
        elif numbers[x] != numbers[x+1]:
            return numbers[x]

    return None

print(find_single([4,1,2,2,1]))


#Var table
# numbers   | [4,1,2,2,], [1,1,2,2,4]
# x         | 0,2,4
# numbers[x]| 1,2,4