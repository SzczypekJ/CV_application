# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    # count = 0
    # for index, char in enumerate(S):
    #     if char == 'X':
    #         count += 1
        
    # return (count // 3) + 1
    count = 0
    result = 0
    
    for i in range(0, len(S), 3):
        if 'X' in S[i:i+3]:
            result += 1
    
    return result

S = ".X..X"
S2 = 'X.XXXXX.X.'
print(solution(S2))
