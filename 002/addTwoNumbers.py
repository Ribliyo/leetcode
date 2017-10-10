# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = ListNode(0)
        p = r
        carry = 0
        while l1 or l2:
            p.next = ListNode(0)
            p = p.next
            val = carry
            if l1:
                val += l1.val                
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val / 10
            p.val = val % 10

        if carry:
            p.next = ListNode(carry)

        return r.next
    
    def toListNode(self, nums):       
        p = ListNode(0)
        r = p
        for num in nums:
            p.next = ListNode(0)
            p = p.next
            p.val = num

        return r.next
        

if __name__ == '__main__':
    s = Solution()    
    l1 = s.toListNode([2, 4, 3, 1])
    l2 = s.toListNode([5, 6, 4])
    # l1 = s.toListNode([5])
    # l2 = s.toListNode([5])
    result = s.addTwoNumbers(l1, l2)
    while result:
        print result.val, "->"
        result = result.next
    
    # while l1:
    #     print l1.val, "->"
    #     l1 = l1.next