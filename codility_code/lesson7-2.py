# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, B):
    count = 0
    tmp = 0
    try:
        idx = B.index(1)
    except:
        return 0
    if A[-1] < A[idx]:
        for i, num in enumerate(A[idx:]):
            if num < A[idx]:
                count += 1
            if i < idx and A[idx] > A[i]:
                tmp += 1
        return count + tmp
    else:
        for i, num in enumerate(A[idx:]):
            if num < A[idx]:
                count += 1
        return count