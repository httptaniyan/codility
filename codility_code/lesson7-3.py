# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") #answer 100%


def solution(S):
    stack = []
    length = len(S)
    if length == 0:
        return 1
    else:
        if S[0] == "(" and S[-1] == ")":
            for i in S:
                if i == "(":
                    stack.append(i)
                elif i == ")":
                    try:
                        stack.pop()
                    except:
                        return 0
            if len(stack) > 0:
                return 0
            else:
                return 1
        else:
            return 0