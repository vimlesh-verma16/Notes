class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        summ= 0 
        cur = head
        hashmap = dict()
        while (cur!= None):
            summ += cur.val
            if summ in hashmap:
                start_node = hashmap[summ]
                node = start_node.next
                nodesum = summ
                while (node != cur):
                    nodesum += node.val
                    del hashmap[nodesum]
                    node = node.next
                start_node.next  = cur.next
            else:
                hashmap[summ] = cur 
            cur = cur.next
        return head