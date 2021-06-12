# Q. 다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.

def find_max_occurred_alphabet(string):
    # 나의 풀이 : N * (1 + 2) + 2 + 26 * 3 → 3N + 80만큼의 시간이 걸림
    alphabet_occurrence_array = [0] * 26
    for char in string: # string 의 길이만큼 아래 연산이 실행
        if not char.isalpha(): # 비교 연산 1번 실행
            continue
        arr_index = ord(char) - ord('a') # 대입 연산 1번 실행
        alphabet_occurrence_array[arr_index] += 1 # 대입 연산 1번 실행
    print(alphabet_occurrence_array)

    max_occurrence = 0 # 대입 연산 1번 실행
    max_alphabet_index = None # 대입 연산 1번 실행
    for alphabet_index, occurrence in enumerate(alphabet_occurrence_array): # alphabet_occurrence_array 의 길이(26)만큼 아래 연산이 실행
        if occurrence > max_occurrence: # 비교 연산 1번 실행
            max_occurrence = occurrence # 대입 연산 1번 실행
            max_alphabet_index = alphabet_index # 대입 연산 1번 실행
    return chr(max_alphabet_index + ord('a'))

    # 남의 풀이 1 : N * (1 + 2) + 2 + 26 * (1 + 3) → 3N+106만큼의 시간이 걸림
    # alphabet_occurrence_array = [0] * 26
    #
    # for char in string: # string 의 길이만큼 아래 연산이 실행
    #     if not char.isalpha(): # 비교 연산 1번 실행
    #         continue
    #     arr_index = ord(char) - ord('a') # 대입 연산 1번 실행
    #     alphabet_occurrence_array[arr_index] += 1 # 대입 연산 1번 실행
    #
    # max_occurrence = 0 # 대입 연산 1번 실행
    # max_alphabet_index = 0 # 대입 연산 1번 실행
    # for index in range(len(alphabet_occurrence_array)): # alphabet_array 의 길이(26)만큼 아래 연산이 실행
    #     alphabet_occurrence = alphabet_occurrence_array[index] # 대입 연산 1번 실행
    #     if alphabet_occurrence > max_occurrence: # 비교 연산 1번 실행
    #         max_occurrence = alphabet_occurrence # 대입 연산 1번 실행
    #         max_alphabet_index = index # 대입 연산 1번 실행
    #
    # return chr(max_alphabet_index + ord('a'))

    # 남의 풀이 2 : 26*(1 + 2*N + 3) → 52N + 104만큼의 시간이 걸림
    # alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    # max_occurrence = 0
    # max_alphabet = alphabet_array[0]
    #
    # for alphabet in alphabet_array: # alphabet_array 의 길이(26)만큼 아래 연산이 실행
    #     occurrence = 0 # 대입 연산 1번 실행
    #     for char in string: # string 의 길이만큼 아래 연산이 실행
    #         if char == alphabet: # 비교 연산 1번 실행
    #             occurrence += 1 # 대입 연산 1번 실행
    #
    #     if occurrence > max_occurrence: # 비교 연산 1번 실행
    #         max_alphabet = alphabet # 대입 연산 1번 실행
    #         max_occurrence = occurrence # 대입 연산 1번 실행
    #
    # return max_alphabet


result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))
