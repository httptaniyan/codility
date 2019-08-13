# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    if len(S) < 4:
        return 0
        
    tmp = list(S)
    if tmp[0] == '{' and tmp[-1] == '}':
        return 1
    elif tmp[0] == '[' and tmp[-1] == ']':
        return 1
    elif tmp[0] == '(' and tmp[-1] == ')':
        return 1
    else:
        return 0