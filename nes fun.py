def access():
    return"hi welcome to python"
print(access())

def outer(func):
    def inner(x):
        a=func(x)
        return a.split()
    return inner
@outer
def access(msg):
    return msg
print(access("welcome to python"))