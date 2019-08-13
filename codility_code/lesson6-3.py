# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    length = len(A)
    thr_list = []
    TF_list = [False] * length

    for i in range(length):
        if len(thr_list) != 3:
            thr_list.append(A[i])
            continue
        
        if thr_list[0] + thr_list[1] < thr_list[2]:
            thr_list[2] = A[i]
        elif thr_list[0] + thr_list[2] < thr_list[1]:
            thr_list[1] = A[i]
        elif thr_list[1] + thr_list[2] < thr_list[0]:
            thr_list[0] = A[i]

        if thr_list[0] + thr_list[1] > thr_list[2]:
            TF_list[2] = True
        elif thr_list[0] + thr_list[2] > thr_list[1]:
            TF_list[1] = True
        elif thr_list[1] + thr_list[2] > thr_list[0]:
            TF_list[0] = True
        
        if TF_list.count(True) == 3:
            return 1
    print(thr_list)        
    return 0

print(solution([10, 2, 5, 1, 8, 20]))