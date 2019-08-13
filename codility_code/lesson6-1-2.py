# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    length = len(A)
    thr_list = []
    for _ in range(length):
        num = A.pop()
        
        if len(thr_list) < 3:
            thr_list.append(num)
            if len(thr_list) == 3:
                sorted(thr_list, reverse=True)
            continue
        
        if thr_list[-1] < num:
            thr_list.pop()
            thr_list.append(num)
            sorted(thr_list, reverse=True)
            
    return thr_list[0] * thr_list[1] * thr_list[2]