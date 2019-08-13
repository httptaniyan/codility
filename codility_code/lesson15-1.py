# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(M, A):
    if len(A) > 1000000000:
        return 1000000000
        
    tmp = 0
    count = 0
    sum_num = 0
    for idx, num in enumerate(A):
        if num == tmp:
            sum_num += count * 2
            count = 0
        else:
            tmp = num
            count += 1
        if len(A) == idx + 1:
            sum_num += count * 2
            return sum_num + 1