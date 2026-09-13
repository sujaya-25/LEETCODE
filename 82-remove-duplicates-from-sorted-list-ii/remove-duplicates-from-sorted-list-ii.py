class Solution(object):
    def deleteDuplicates(self,head):
        dummy=ListNode(0)
        dummy.next=head
        p=dummy

        while head:
            if head.next and head.val==head.next.val:
                x=head.val
                while head and head.val==x:
                    head=head.next
                p.next=head
            else:
                p=p.next
                head=head.next

        return dummy.next