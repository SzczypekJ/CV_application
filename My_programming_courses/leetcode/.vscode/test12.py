def solution(words):
    count = 0
    n = len(words)

    for i in range(n):
        for j in range(i+1, n):
            if words[i] == words[j] or words[i].endswith(words[j]) or words[j].endswith(words[i]):
                count += 1

    return count


# Example usage:
words = ["back", "backdoor", "gammon",
         "backgammon", "comeback", "come", "door"]
print(solution(words))
