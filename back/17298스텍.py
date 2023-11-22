n = int(input())
stack = []
answer = [-1] * n
arr = list(map(int, input().split()))
for i, x in enumerate(arr):
    if len(stack) ==0 or stack[-1][0] >= x:
        stack.append((x, i))
    else:
        while stack:
            pre, index = stack.pop()
            if pre >= x:
               stack.append((pre, index))
               break
            else:
                answer[index] = x
        stack.append((x,i))

for x in answer:
    print(x, end = ' ')