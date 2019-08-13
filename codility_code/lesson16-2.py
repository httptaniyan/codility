# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") answer 100%


def solution(A, B):
    if len(A) < 1:
        return 0
     
    cnt = 1
    prev_end = B[0]
     
    for idx in range(1, len(A)):
        if A[idx] > prev_end:
            cnt += 1
            prev_end = B[idx]
     
    return cnt