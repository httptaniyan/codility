# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N, M):
    count = 1
    tmp = 0
    while ( tmp + M ) % N != 0:
        tmp = ( tmp + M ) % N
        count += 1
    return count