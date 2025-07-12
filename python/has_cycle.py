# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        my_track = set()
        pos = 0
        maxx = 10 ** 4
        curr = head
        while pos < maxx:
            try: 
                if curr.next: 
                    curr = curr.next
                    if curr not in my_track:
                        my_track.add(curr)
                    else: 
                        break
                else: 
                    return False
                pos += 1
            except: 
                return False
        return True