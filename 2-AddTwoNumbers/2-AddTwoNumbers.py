# Last updated: 2/27/2026, 3:48:07 PM
1#Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def addTwoNumbers(self, l1, l2):
8        """
9        :type l1: Optional[ListNode]
10        :type l2: Optional[ListNode]
11        :rtype: Optional[ListNode]
12        """
13        
14        dummy = ListNode()
15        res = dummy
16
17        total = carry = 0
18
19        while l1 or l2 or carry:
20            total = carry
21
22            if l1:
23                total += l1.val
24                l1 = l1.next
25            if l2:
26                total += l2.val
27                l2 = l2.next
28            
29            num = total %10 # if total is 14 num is 4
30            carry = total // 10 #it total is 14 carry is 1
31
32            dummy.next = ListNode(num)
33            dummy  = dummy.next
34        return res.next
35