# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    #binary_str = bin(N)
    binary_num = format(N, 'b')

    idx_list = []
    for idx, tmp in enumerate(binary_num):
        if tmp == '1':
            idx_list.append(idx)

    diff_idx_list = []
    pre_num = 0
    for i, idx in enumerate(idx_list):
        if i == 0:
            pre_num = idx
            continue
        else:
            if idx - pre_num == 1:
                diff_idx_list.append(0)
            else:
                diff_idx_list.append(idx - pre_num - 1)
        pre_num = idx

    if len(diff_idx_list) == 0:
        return 0

    return max(diff_idx_list)