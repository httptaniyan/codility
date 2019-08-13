# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    sum_num = 0
    max_sum_num = 0
    pre_idx = 0
    counter_P = 0
    counter_N = 0

    if len(A) == 1:
        return A[0]
    
    for idx, num in enumerate(A):
        if num > 0:
            counter_P += 1
            counter_N = 0
            continue
        elif num < 0:
            counter_N += 1
            counter_P = 0
            sum_num = sum(A[pre_idx:idx])
            pre_idx = idx + 1
            if sum_num > max_sum_num:
                max_sum_num = sum_num
    if counter_P > 0 and max_sum_num == 0:
        return sum(A)
    elif counter_N > 0 and max_sum_num == 0:
        return A[0]

    return max_sum_num 