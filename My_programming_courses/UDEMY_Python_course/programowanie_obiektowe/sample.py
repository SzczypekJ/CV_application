class User:
    def __init__(self, age, name):
        print("I am an initializer that is always performed during the construction of an object")

        self.age = age
        self.name = name

    def print_age(self):
        print("age: ", self.age, "\name: ", self.name)


user1 = User(30, "Mike")
user2 = User(24, "Ares")


user1.print_age()
user2.print_age()
