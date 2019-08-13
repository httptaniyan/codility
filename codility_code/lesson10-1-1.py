# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") answer 100%


def solution(N):
    count = 0
    itr = 1
    while itr * itr <= N:
        if N % itr == 0:
            if itr * itr == N:
                count += 1
            else:
                count += 2
        itr += 1
    return count