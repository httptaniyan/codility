# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    li = []

    for i in range(1, N+1):
        if N % i == 0:
            li.append(i)
    return len(li)