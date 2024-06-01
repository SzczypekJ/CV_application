def solution(A):
    # Implement your solution here
    A_sorted = sorted(A)

    for i in range(len(A_sorted) - 1):
        if (A_sorted[i + 1] - A_sorted[i]) == 1:
            return True
        else:
            return False


A = [11, 1, 8, 12, 14]
print(solution(A))
