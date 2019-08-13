# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    A.sort()
    tmp = 1
    for i in A:
        if i - tmp != 0:
            return i - 1
            
        tmp += 1