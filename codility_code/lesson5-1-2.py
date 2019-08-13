# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") answer 100%


def solution(A):
    sum_count = 0
    length = len(A)
    count_1 = 0
    
    for i in range(length - 1, -1, -1):
        num = A[i]
        if sum_count > 1000000000:
            return -1
        if num == 0:
            sum_count += count_1
        else:
            count_1 += 1
            
    return sum_count