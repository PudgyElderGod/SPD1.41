#Problem: You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order and each of their nodes contain a single digit. 
#Add the two numbers and return it as a linked list.

#Q: Is the data type integers only?
#Q: Does the returned linked list have to be reversed as well?

#A: All postive integers
#A: Answer also has to be reversed

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Run time - O(n)
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    a = convertToNum(l1)
    b = convertToNum(l2) 
    sum = a+b
    convert = str(sum)
    temp = None
    head = None
    for x in range(len(convert)-1, -1, -1):
        if temp == None:
            temp = ListNode(int(convert[x]))
            head = temp
        else:
            temp.next = ListNode(int(convert[x]))
            temp = temp.next

    return head

#Run Time - O(n)
def convertToNum(node):
    temp = ""
    while node:
        temp = str(node.val) + temp
        node = node.next
    return int(temp)

