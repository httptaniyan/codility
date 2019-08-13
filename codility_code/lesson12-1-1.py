# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


count = 0

def gcd(a, b, tmp):
    global count
    if a % b == 0:
        count += 1
        return count
    else:
        count += 1
        return gcd(a % b + tmp, b, tmp)

def solution(N, M):
    tmp = M
    return gcd(M, N, tmp)
