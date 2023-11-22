import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

LIS = [arr[0]]

def fi(e):
    start = 0
    end = len(LIS) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
            
    return start

for item in arr:
    if LIS[-1] < item:
        LIS.append(item)
    else:
        idx = fi(item)
        LIS[idx] = item

print(len(LIS))