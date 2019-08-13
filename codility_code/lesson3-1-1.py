# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, Y, D):
    count = 0
    sum_dis = 0
    while True:
        count += 1
        sum_dis = X + D * count
        if X == Y:
            return 0
        elif Y <= sum_dis:
            return count
