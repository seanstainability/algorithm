# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

# 시간 초과
# A, B, V = map(int, input().split())
# count = 0
# while True:
#     count += 1
#     V = V - A
#     print(V)
#     if V <= 0:
#         break
#     else:
#         V = V + B
# print(count)

a,b,v = map(int,input().split())
k = 0	#올라가는 데 걸리는 일수
d = 0	#올라간 높이
while 1:
    k+=1
    if a*k-b*(k-1)>=v:
        break
print(k)

# 위의 if문을 이항 정리하여 다음과 같이 코드 개선
a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)	#삼항연산자
## 4.1일은 5일이다.

