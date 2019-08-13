# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") answer 100%


def solution(A):
    length = len(A)
    sum_num = (length) * (length + 1) / 2
    
    tmp = 0
    for i in A:
        tmp += i
    
    if sum_num == tmp and ( length == len(set(A))):
        return 1
    else:
        return 0  