from collections import defaultdict
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Solution 1 80ms
        # dic = dict()
        # m = n = head
        # while m is not None:
        #     dic[m] = RandomListNode(m.label)
        #     m = m.next
        # while n :
        #     dic[n].next = dic.get(n.next)
        #     dic[n].random = dic.get(n.random)
        #     n = n.next
        # return dic.get(head)

        # Solution 2 72ms
        # dic = dict()
        # m = head
        # while m:
        #     if m not in dic:
        #         dic[m] = RandomListNode(m.label)
        #     if m.next:
        #         if m.next not in dic:
        #             dic[m.next] = RandomListNode(m.next.label)
        #         dic[m].next = dic.get(m.next)
        #     if m.random:
        #         if m.random not in dic:
        #             dic[m.random] = RandomListNode(m.random.label)
        #         dic[m].random = dic.get(m.random)
        #     m = m.next
        #
        # return dic.get(head)

        # Solution 2+ 72ms
        # dic = dict()
        # dic[None] = None
        # m = head
        # while m:
        #     if m not in dic:
        #         dic[m] = RandomListNode(m.label)
        #     if m.next not in dic:
        #         dic[m.next] = RandomListNode(m.next.label)
        #     if m.random not in dic:
        #         dic[m.random] = RandomListNode(m.random.label)
        #     dic[m].next = dic.get(m.next)
        #     dic[m].random = dic.get(m.random)
        #     m = m.next
        #
        # return dic.get(head)


        # Solution 3 72ms
        dic = defaultdict(lambda: RandomListNode(0))
        dic[None] = None
        n = head
        while n:
            dic[n].label = n.label
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]
