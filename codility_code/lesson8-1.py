# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") answer 100%

import collections


def solution(A):
    length = len(A)
    if length == 0:
        return -1
    elif length == 1:
        return 0
    else:    
        clist = collections.Counter(A)
        tmp = clist.most_common()[0]
        if tmp[1] > length / 2:
            for i, num in enumerate(A):
                if num == tmp[0]: # maekaratannsaku
                    return i
                ptmp = A.pop()
                length -= 1
                if num == ptmp: # ushirokaratannsaku
                    return length - 1
        else:
            return -1