def walking():
    print("getup")
    print("freshup")
    print("tieshoe")
    print("waterbottle")
walking()  

def sleep(a):
    print("hi")
    print("bye")
sleep(1)

def addition(a,b):
    print(a+b)
    addition(10,20)

def Amazon():
    print("cloth")
    print("shoe")
    print("cometic")
Amazon()

def Amazon():
    return 'cloth','shoe','cometic'
    return'apple'
print(Amazon())  
print(Amazon())

def number(a,b):
    return a+b,a-b,a*b,a/b
print(number(10,20))

a=10
def access():
    global a
    a=a+1
print(a)
access()
