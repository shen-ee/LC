# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head

        cur  = head  # pointer of current node
        processed_tail = None
        processed_head = None
        length = 0
        tmp = head
        while tmp != None:
            length += 1
            tmp = tmp.next

        if length < k:
            return head

        rounds = length//k
        for j in range (rounds):
            new_tail = None
            new_head = None
            for i in range (k):  # form a reversed link nodes in k size named "new"
                tmp = ListNode(cur.val)  # copy of current node    
                if i == 0:
                    new_head = new_tail = tmp
                else:
                    tmp.next = new_head
                    new_head = tmp
                cur = cur.next # move pointer

            if j == 0:  # connect "new" with "processed" and leave "processed" alone
                processed_head = new_head
                processed_tail = new_tail
            else:
                processed_tail.next = new_head
                processed_tail = new_tail
        
        processed_tail.next = cur  # connect the tail(the rest part of original linked nodes) with "processed"

        return processed_head
        


        
            