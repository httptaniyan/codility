# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def is_pair(a, b):
    if a == "{" and b == "}":
        return 1
    elif a == "(" and b == ")":
        return 1
    elif a == "[" and b == "]":
        return 1
    else:
        return 0
    

def solution(S):
    if len(S) == 0:
        return 1
    if len(S) == 1:
        return 0
    
    check_list = ["{", "(", "["]
    stack = []
    for char in S:
        if char in check_list:
            stack.append(char)
        else:
            if len(stack) == 0:
                return 0
            tmp = stack.pop()
            if is_pair(tmp, char) == 0:
                return 0
    if len(stack) != 0:
        return 0
    return 1