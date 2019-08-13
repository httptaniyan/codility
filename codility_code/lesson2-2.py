# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K):
    count = 0
    while True:
        if A == [0] * K:
            return A
            
        get_num = A.pop()
        A.insert(0,get_num)
        if count == K-1:
            break
        count += 1
    return A

print(solution([3, 8, 9, 7, 6], 3))