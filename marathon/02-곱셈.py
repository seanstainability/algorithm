# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

# 1차
# a = int(input())
# b = int(input())
#
# print(a * (b % 10))
# print(a * ((b // 10) % 10))
# print(a * (b // 100))
# print(a * b)

# 2차
a = int(input())
b = input() # 쪼개기 좋게 문자열 형태로 남겨둠

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))
