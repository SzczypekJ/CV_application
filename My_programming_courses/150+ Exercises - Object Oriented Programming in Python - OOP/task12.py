"""
Napraw poniższy kod:
x = 10
 

def func1():
    x = 5
    
    def inner_func():
        print(x)
    
    inner_func()
 

def func2():
    inner_func()"""


x = 10


def inner_func():
    print(x)


def func1():
    x = 5
    inner_func()


def func2():
    inner_func()


func1()
func2()
