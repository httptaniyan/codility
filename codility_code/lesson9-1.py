# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    length = len(A)
    if length == 0:
        return 0
    buy_num = 0
    sell_mum = 0
    for idx, num in enumerate(A):
        if idx == 0:
            buy_num = num
            sell_num = A.pop()
            continue
        
        if buy_num > num and int( length / 2 ) > idx:
            buy_num = num
        
        sell_num_tmp = A.pop()
        if sell_num < sell_num_tmp:
            if int( length / 2 ) == idx:
                sell_num = sell_num_tmp
                break
            else:
                sell_num = sell_num_tmp
                continue
                
    sum_num = sell_num - buy_num
    if sum_num > 0:        
        return sum_num 
    else:
        return 0
 
