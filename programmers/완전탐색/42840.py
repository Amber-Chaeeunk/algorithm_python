def solution(answers):
    cnt = {}
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(1, 4):
        cnt[i] = 0
    for idx, num in enumerate(answers):
        if num == one[idx%5]:
            cnt[1] += 1
        if num == two[idx%8]:
            cnt[2] += 1
        if num == three[idx%10]:
            cnt[3] += 1

    sorted_cnt = dict(sorted(cnt.items(), key = lambda x: cnt[1], reverse=True))
    max_num = max(sorted_cnt.values())
    answer = [key for key, value in sorted_cnt.items() if value == max_num]

    return answer