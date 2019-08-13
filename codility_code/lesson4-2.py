# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, A):
    TF_list = [False] * X
    for indx in range(len(A)):
        if TF_list[A[indx] - 1]:
            continue
        else:
            TF_list[A[indx] - 1] = True
            X -= 1
            if X == 0:
                return indx

    return -1