# Q. 다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.

def find_max_occurred_alphabet(string):
    # 나의 풀이 : 29만큼의 공간이 사용되었다.
    alphabet_occurrence_array = [0] * 26 # -> 26 개의 공간을 사용합니다
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a') # 1개의 공간을 사용합니다
        alphabet_occurrence_array[arr_index] += 1
    print(alphabet_occurrence_array)

    max_occurrence = 0 # 1개의 공간을 사용합니다
    max_alphabet_index = None # 1개의 공간을 사용합니다
    for alphabet_index, occurrence in enumerate(alphabet_occurrence_array):
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet_index = alphabet_index
    return chr(max_alphabet_index + ord('a'))

    # 남의 풀이 1 : 30만큼의 공간이 사용되었다.
    # alphabet_occurrence_array = [0] * 26 # -> 26 개의 공간을 사용합니다
    #
    # for char in string:
    #     if not char.isalpha():
    #         continue
    #     arr_index = ord(char) - ord('a') # 1개의 공간을 사용합니다
    #     alphabet_occurrence_array[arr_index] += 1
    #
    # max_occurrence = 0 # 1개의 공간을 사용합니다
    # max_alphabet_index = 0 # 1개의 공간을 사용합니다
    # for index in range(len(alphabet_occurrence_array)):
    #     alphabet_occurrence = alphabet_occurrence_array[index] # 1개의 공간을 사용합니다
    #     if alphabet_occurrence > max_occurrence:
    #         max_occurrence = alphabet_occurrence
    #         max_alphabet_index = index
    #
    # return chr(max_alphabet_index + ord('a'))

    # 남의 풀이 2 : 29만큼의 공간이 사용되었다.
    # alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"] # -> 26 개의 공간을 사용합니다
    # max_occurrence = 0 # 1개의 공간을 사용합니다
    # max_alphabet = alphabet_array[0] # 1개의 공간을 사용합니다
    #
    # for alphabet in alphabet_array:
    #     occurrence = 0 # 1개의 공간을 사용합니다
    #     for char in string:
    #         if char == alphabet:
    #             occurrence += 1
    #
    #     if occurrence > max_occurrence:
    #         max_alphabet = alphabet
    #         max_occurrence = occurrence
    #
    # return max_alphabet


result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))
