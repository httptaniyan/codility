# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") answer 100%


def solution(A):
    length = len(A)
    total =  int((length + 1) * ( length + 2 ) / 2)
    if length != 0:
        sum_num = 0
        for i in A:
            sum_num += i
        return total - sum_num
    else:
        return 1