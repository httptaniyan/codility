# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    tmp = set(A)
    counter = 0
    unpair_num = 0
    for i in tmp:
        counter = A.count(i)
        if counter % 2 != 0:
            unpair_num = i
    return unpair_num

P = [9, 3, 9, 3, 9, 7, 9]
print(solution(P))