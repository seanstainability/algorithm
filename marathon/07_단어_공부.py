# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

word = input().upper()

occurrence_array = [0] * 26

for char in word:
    idx = ord(char) - ord('A')
    occurrence_array[idx] += 1

max_occurrence = 0
max_idx = None
is_repeat = False
for idx, occurrence in enumerate(occurrence_array):
    if max_occurrence < occurrence:
        max_occurrence = occurrence
        max_idx = idx
        is_repeat = False
    elif max_occurrence == occurrence:
        is_repeat = True
    else:
        is_repeat = False

if is_repeat is True:
    print('?')
else:
    print(chr(max_idx + ord('A')))