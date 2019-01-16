# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Solution 1 
        dump = l3 = ListNode(0)
        extra = 0
        while l1 != None or l2 != None or extra != 0:
            v1 = 0 if l1 == None else l1.val
            v2 = 0 if l2 == None else l2.val
            if v1 + v2 + extra > 9:
                v3 = v1 + v2 + extra -10
                extra = 1
            else:
                v3 = v1 + v2 + extra
                extra = 0
            # print(v1,v2,v3)
            l3.next = ListNode(v3)        
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            l3 = l3.next

        # Solution 1 modified
        dump = l3 = ListNode(0)
        extra = 0
        while l1 or l2 or extra :
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            if v1 + v2 + extra > 9:
                v3 = v1 + v2 + extra - 10
                extra = 1
            else:
                v3 = v1 + v2 + extra
                extra = 0

            # print(v1,v2,v3)
            l3.next = ListNode(v3)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3 = l3.next

        return dump.next