# https://www.acmicpc.net/problem/1874

import sys
case_cnt = sys.stdin.readline()
n = int(case_cnt)
stack = []
result = []
pointer = 1
for i in range(n):
    num = int(input())
    while pointer <= num:
        stack.append(pointer)
        result.append('+')
        pointer += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

for i in result:
    print(i)

