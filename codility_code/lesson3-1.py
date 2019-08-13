# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, Y, D):
    jump_count = int( abs(Y - X) / D )
    if Y - ( X * jump_count ) == 0 or jump_count == 0:
        return jump_count
    else:
        return jump_count + 1
