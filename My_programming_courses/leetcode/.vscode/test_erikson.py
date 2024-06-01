def solution(s):
    c = s[0]
    if c.isupper():    # please fix condition
        return "upper"
    elif c.islower():  # please fix condition
        return "lower"
    elif c.isnumeric():  # please fix condition
        return "digit"
    else:
        return "other"
