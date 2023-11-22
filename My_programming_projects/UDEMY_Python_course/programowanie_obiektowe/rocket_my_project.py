import random

# Chose the random rocket and travel the 100km. Print the name of this rocket.

# The class of rockets


class Rockets:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def print_rockets_names(self):
        print("Rocket name is:", self.name)

# Creating rockets names - we will have 10 rockets


def create_rockets_names():
    list_of_rockets_names = []
    for i in range(1, 11):
        rocket_name = "rocket" + str(i)
        list_of_rockets_names.append(rocket_name)
    return list_of_rockets_names

# The function which is choosing the random rocket


def choose_random_rocket(rocket_names):
    the_random_number = random.randint(0, len(rocket_names) - 1)
    return rocket_names[the_random_number]

# The random distance of random rocket


def random_distance_the_rocket_travel(random_rocket):
    random_rocket.position += random.randint(0, 20)


rocket_names = create_rockets_names()

for i in range(0, 10):
    rocket_names[i] = Rockets(rocket_names[i], 0)
    rocket_names[i].print_rockets_names()

position = 0

# Checking which rocket first reach 100km or more
while position < 100:
    random_rocket = choose_random_rocket(rocket_names)
    random_distance_the_rocket_travel(random_rocket)
    if random_rocket.position >= 100:
        print("The rocket which first traveled 100km is:", random_rocket.name)
        break
