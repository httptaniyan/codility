# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") answer 100%


def solution(K, A):
    sum_num = 0
    count = 0
    for num in A:
        sum_num += num
        if sum_num >= K:
            count += 1
            sum_num = 0
            continue
    return count