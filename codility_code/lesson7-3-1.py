# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") #answer 100% another


def solution(S):
    leftBrackets = 0
     
    for symbol in S:
        if symbol == '(':
            leftBrackets += 1
        else:
            if leftBrackets == 0:
                return 0
            leftBrackets -= 1 
     
    if leftBrackets != 0:
        return 0
     
    return 1