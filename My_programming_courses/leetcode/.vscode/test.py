# import random

# moved_elem = set()
# lst = [1, 2, 5, 6, 8]

# for i in range(3):
#     random_index = random.randint(0, 4)
#     random_element = lst[random_index]

#     while random_element in moved_elem:
#         random_index = random.randint(0, 4)
#         random_element = lst[random_index]

#     moved_elem.add(random_element)
#     print('moved_elem: ', moved_elem)
lst = [20, 80, 15, 66, 23, 78, 44, 32]
szukana_liczba = 110
for i in range(len(lst)):
    for j in range(i+1, len(lst)):  # Rozpoczynamy od i+1, aby uniknąć podwójnego zliczania
        if lst[i] + lst[j] == szukana_liczba:
            print("Liczba 1 to:", lst[i])
            print("Liczba 2 to:", lst[j])