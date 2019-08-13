# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    sum_num = 0
    max_sum_num = 0
    pre_idx = 0

    if len(A) == 1:
        return A[0]
    
    for idx, num in enumerate(A):
        if num > 0:
            continue
        elif num < 0:
            sum_num = sum(A[pre_idx:idx])
            pre_idx = idx + 1
            if sum_num > max_sum_num:
                max_sum_num = sum_num
    return max_sum_num 