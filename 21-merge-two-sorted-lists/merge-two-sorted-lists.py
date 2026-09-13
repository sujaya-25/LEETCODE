class Solution(object):
    def mergeTwoLists(self,list1,list2):
        a=ListNode(0)
        p=a

        while list1 and list2:
            if list1.val<list2.val:
                p.next=list1
                list1=list1.next
            else:
                p.next=list2
                list2=list2.next
            p=p.next

        if list1:
            p.next=list1
        else:
            p.next=list2

        return a.next