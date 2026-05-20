# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = []

        while head:
            if head and head.next:
                if head.next.val not in arr:
                    arr.append(head.next.val)
                else:
                    return True
            head = head.next
        return False
