# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") answer 100%


def solution(X, Y, D):
    jump_count = ( Y - X ) // D
    if Y - ( X + D * jump_count ) < 0:
        return jump_count
    elif Y - ( X + D * jump_count ) > 0:
        return jump_count + 1
    else:
        return jump_count