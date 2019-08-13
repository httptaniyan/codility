# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message") answer 100%


def solution(A, K):
    if len(A) == 0 or len(set(A)) == 1 or K == 0:
        return A
    
    if len(A) <= K:
        if len(A) % K == 0:
            return A
        else:
            loop_count = int(K/len(A))
            K = K - len(A)*loop_count
            B = A[:-K]
            A = A[len(A)-K:] + B
    elif len(A) > K:
        B = A[:-K]
        A = A[len(A)-K:] + B

    return A  

print(solution([3, 8, 9, 7, 6], 3))