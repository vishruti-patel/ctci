"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

"""
Notes:
we need to add digit by digit. There could be possibility of carry. for eg, 7 +7 = 14. So in digit variable we need to keep 4
and 1 will be placed in carry variable. Now how do we do that in python. 
for that we use modulo (%) and we use integration divider/floor dividor (//)
% -> remainder
//  -> quotient.

so if in [3,7] and [6,7], I will start by adding 7, 7 as the list is in reverse order. 
so let's say ADD = l1 + l2  which is (7 + 7)
now, carry = ADD // 10 which is (14 // 10)= 1
and, digit = ADD % 10 which is (14 % 10 = 4). So this digit will be then linked as the new node in the list. 

"""


class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

class List:
      def addNumber(l1, l2):
        #we need this pointer to create a fake starter node. Basically to waive out any edge cases for an empty list
        dummy = Node()

        #When we build a linked list, we always need to append new nodes at the end. If we only had a reference to the head (like dummy), then every time we want to add a new node we have to start from the head and traverse to the tail — that would be O(n) per addition.
        curr = dummy

        carry = 0


        #we will run while loop until none of these are null
        while l1 or l2 or carry:
            if l1:
                  v1 = l1.val
            else:
                 v1 = 0

            if l2:
                 v2 = l2.val
            else:
                 v2 = 0

            
            sum = v1 + v2 + carry
            carry = sum//10
            new_val = sum % 10
            #adding this new_val to the end of the list
            curr.next = Node(new_val)


            #update all the pointers
            curr = curr.next
            if l1:
                 l1 = l1.next
            if l2:
                 l2 = l2.next

        return dummy.next