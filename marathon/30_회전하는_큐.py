# https://www.acmicpc.net/problem/1021

from collections import deque

n, m = map(int, input().split())
p = list(map(int, input().split()))
queue = deque(range(1, n+1))
count = 0
for i in range(m):
    q_len = len(queue)
    q_idx = queue.index(p[i])
    if q_idx > q_len // 2:
        queue.rotate(q_len - q_idx) # 양수일 경우 맨 뒤의 값을 맨 앞으로 이동
        count += (q_len - q_idx)
    else:
        queue.rotate(-q_idx) # 음수일 경우 맨 앞의 값을 맨 뒤로 이동
        count += q_idx
    queue.popleft()

print(count)

