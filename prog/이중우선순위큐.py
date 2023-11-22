# 1
def solution(operations):
    arr = []
    
    for op in operations:
        cmd, val = op.split()
        val = int(val)
        
        if cmd == 'I':
            arr.append(val)
        elif cmd == 'D' and arr:
            if val == 1:
                arr.remove(max(arr))
            elif val == -1:
                arr.remove(min(arr))
    
    if arr:
        return [max(arr), min(arr)]
    else:
        return [0, 0]
    

# 2
import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    
    for operation in operations:
        op, val = operation.split()
        val = int(val)
        
        if op == "I":
            heapq.heappush(max_heap, -val)
            heapq.heappush(min_heap, val)
        elif op == "D":
            if max_heap:
                if val == 1:
                    max_val = -heapq.heappop(max_heap)
                    min_heap.remove(max_val)
                elif val == -1:
                    min_val = heapq.heappop(min_heap)
                    max_heap.remove(-min_val)
                    
            if not max_heap:
                min_heap = []
    
    if max_heap:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]