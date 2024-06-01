class Second:
    def __init__(self):
        # print("???")
        pass

    def __del__(self):
        print("!!!")


class Third:
    def __init__(self, bcd):
        print("???")

    def __init__(self, text="###"):
        fifth = Second()
        print(text)


class Fourth(Third):
    @staticmethod
    def third():
        fifth = Second()
        Third()

    def __init__(self):
        print()
        super().__init__()


class First:
    @staticmethod
    def fire():
        Fourth()

    @staticmethod
    def fire_char(l):
        pass


if __name__ == "__main__":
    i = [None] * 50
    first = First()
    first.fire()

    del i
    First.fire()
