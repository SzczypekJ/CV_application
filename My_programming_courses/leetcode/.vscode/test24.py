# def solution(S):
# # Implement your solution here
# sentences = [sentence.strip().split()
#              for sentence in S.split('.') if sentence.strip()]
# max_lenght = 0
# for sentence in sentences:
#     if len(sentence) > max_lenght:
#         max_lenght = len(sentence)

# return max_lenght
def solution(S):
    max_length = 0
    for sentence in S.split('.'):
        sentence = sentence.strip().split()
        if sentence:
            max_length = max(max_length, len(sentence))

    return max_length


S = "Forget  CVs..Save time . x x"
print(solution(S))
