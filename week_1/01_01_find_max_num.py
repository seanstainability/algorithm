# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

def find_max_num(array):
    # 나의 풀이 : 2N + 1만큼의 시간이 걸림 → O(n)
    max_num = 0 # 연산 1번 실행
    for num in array: # array 의 길이만큼 아래 연산이 실행
        if num > max_num: # 비교 연산 1번 실행
            max_num = num # 대입 연산 1번 실행

    return max_num

    # 남의 풀이 : N**2만큼의 시간이 걸림 → O(n**2)
    # for num in array: # array 의 길이만큼 아래 연산이 실행
    #     for compare_num in array: # array 의 길이만큼 아래 연산이 실행
    #         if num < compare_num: # 비교 연산 1번 실행
    #             break
    #     else:
    #         return num

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))
