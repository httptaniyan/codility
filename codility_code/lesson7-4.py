# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") #atodeyaru

def solution(H):
    count = 0
    tmp = 0
    for idx, num in enumerate(H):
        if idx == 0:
           tmp = num
           continue
        
        if tmp != num:
            count += 1
            tmp = num
    return count