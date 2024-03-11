"""Mamy wejście złożone z 4 liczb digit = list[int], sprawdź jaką największą godzinę da się swtorzyć z tych liczb i zwróć w formacie HH::MM"""


def largest_time_from_digits(digits):
    max_time = -1

    # itearting from the lowest to the highest - slower
    # for h1 in range(0, 3):
    #     for h2 in range(0, 10):
    #         for m1 in range(0, 6):
    #             for m2 in range(0, 10):
    #                 if sorted([h1, h2, m1, m2]) == sorted(digits):
    #                     hour = h1 * 10 + h2
    #                     minute = m1 * 10 + m2
    #                     if hour < 24 and minute < 60:
    #                         max_time = max(max_time, hour * 60 + minute)

    # itearting from the highest to the lowest - faster
    for h1 in range(2, -1, -1):
        for h2 in range(9, -1, -1):
            for m1 in range(5, -1, -1):
                for m2 in range(9, -1, -1):
                    if sorted([h1, h2, m1, m2]) == sorted(digits):
                        hour = h1 * 10 + h2
                        minute = m1 * 10 + m2
                        if hour < 24 and minute < 60:
                            max_time = max(max_time, hour * 60 + minute)
    if max_time == -1:
        return ""

    hour = max_time // 60
    minute = max_time % 60
    return "{:02d}:{:02d}".format(hour, minute)


digits = [5, 9, 3, 2]
print(largest_time_from_digits(digits))
