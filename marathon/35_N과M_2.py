# https://www.acmicpc.net/problem/15650


# 15649
# n, m = list(map(int, input().split()))
# s = [] # m개의 수열을 저장하기 위한 리스트
#
# def dfs():
#     if len(s) == m: # 수열이 m개가 되면 모든 숫자를 출력하고 리턴
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(1, n + 1): # 1부터 n까지의 숫자들을 모두 확인
#         if i not in s: # 중복이 아닐 경우에만 숫자 넣기
#             s.append(i)
#             dfs()
#             s.pop()
#
# dfs()


n, m = list(map(int, input().split()))
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            dfs(i + 1) # 재귀 호출 시에는 자기 다음 숫자를 불러오게 된다.
            s.pop()


dfs(1)