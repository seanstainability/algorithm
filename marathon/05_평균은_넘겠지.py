# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

case_count = int(input())
for case in range(case_count):
    students = input().split()
    students_count = int(students.pop(0))
    students_score = 0
    for score in students:
        students_score += int(score)
    avg = students_score / students_count
    over_avg_count = 0
    for score in students:
        if int(score) > int(avg):
            over_avg_count += 1
    result = str("%.3f" %round(100 * over_avg_count / students_count, 3)) + '%'
    print(result)