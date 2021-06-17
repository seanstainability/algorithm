# https://www.acmicpc.net/problem/1011

case = int(input())
for i in range(case):
    count = 1 # 마지막 1광년을 미리 더해줌
    position = list(map(int, input().split()))
    start = 0
    end = position[1] - position[0] - 1
    while True:
        # print('end', end, 'start', start)
        if (end - start) - (start + 1) > 0:
            start = start + 1
            count += 1
        else:
            count += 1
            break

    print(count)


