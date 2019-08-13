# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    A = set(map(abs, A))
    return len(A)