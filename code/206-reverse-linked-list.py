# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Solution 1 iteratively
        # dummy = None
        # while head:
        #     tmp = ListNode(head.val)
        #     tmp.next = dummy         
        #     dummy = tmp         
        #     head = head.next
            
        # return dummy

        # Solution 2  recursively
        def helper(old, new):
            if old == None:
                return new
            tmp = Listnode(old.val)
            old = old.next
            tmp.next = new
            new = tmp
            return helper(old,new)
        
        return helper(head,None)
        