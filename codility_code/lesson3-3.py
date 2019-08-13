# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    tmp = 0
    tmp_update = 0
    for indx, num in enumerate(A):
        tmp = abs( sum(A[indx + 1:]) - sum(A[:indx+1]) )
        if indx == 0:
            tmp_update = tmp
            continue
        if tmp < tmp_update:
            tmp_update = tmp
            
    return tmp_update