import heapq

class Solution(object):
    def mergeKLists(self, lists):
       
    
        if not lists or len(lists) == 0:
            return None

        
        min_heap = []

        
        for i, head in enumerate(lists):
            if head:
                # Adiciona ao heap o valor do nó
                heapq.heappush(min_heap, (head.val, i, head))

        
        dummy = ListNode(0)
        current = dummy

       
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            # Conecta o nó extraído à lista mesclada
            current.next = node
            current = current.next

            # Se o nó extraído tiver um próximo nó, adiciona-o ao heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        
        return dummy.next