def solution(S):
    i = 0
    while i < len(S) - 1:
        if S[i:i+2] in {'AB', 'BA', 'CD', 'DC'}:
            S = S[:i] + S[i+2:]
            i = max(0, i - 1)  # W razie potrzeby cofamy się o jeden indeks
        else:
            i += 1
    return S


S = 'CBACD'
S1 = 'ACBDACBD'
S2 = 'CABABD'
print(solution(S))
print(solution(S1))
print(solution(S2))
