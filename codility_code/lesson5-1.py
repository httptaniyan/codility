# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    sum_count = 0
    list_0 = [i for i, x in enumerate(A) if x == 0]
    for i in list_0:
        sum_count += sum(A[i:])
    return sum_count