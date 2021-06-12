# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.
# "abadabac" # 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!

def find_not_repeating_first_character(string):
    # 나의 풀이 : 시간 복잡도 → O(N)
    alphabet_occurrence_array = [0] * 26

    for char in string:  # string 의 길이만큼 아래 연산이 실행
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    print(alphabet_occurrence_array)

    answer = None
    for index in range(len(alphabet_occurrence_array)):  # alphabet_occurrence_array 의 길이(26)만큼 아래 연산이 실행
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            answer = chr(index + ord("a"))
            break

    if answer is not None:
        return answer
    else:
        return "_"

    # 남의 풀이 : 시간 복잡도 → O(N)
    alphabet_occurrence_array = [0] * 26

    for char in string:  # string 의 길이만큼 아래 연산이 실행
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):  # alphabet_occurrence_array 의 길이(26)만큼 아래 연산이 실행
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:  # string 의 길이만큼 아래 연산이 실행
        if char in not_repeating_character_array:
            return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
