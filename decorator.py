def decorator(fun):
    def wraper():
        fun()
    return wraper
@decorator
def x():
    print("Hello")
x()