from collections import deque
N = int(input())
arr = deque(range(1, 1+N))
ans = []
while len(arr) > 1:
    ans.append(arr.popleft())
    arr.append(arr.popleft())
ans.append(arr[0])
print(*ans)
