# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(A):
    tmp = collections.Counter(A)
    tmp2 = tmp.most_common()
    return tmp2[-1][0]

P = [9, 3, 9, 3, 9, 7, 9]
print(solution(P))