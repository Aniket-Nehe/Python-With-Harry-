# Decoretor in python
'''Decoretor is a function that take other function as an argument and return  a new function that modifies the behavior of the orignal function. the new function is often referrd to as a  " decorator" function '''

#Eg.1
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this funnction")
    return mfx()
@greet
def hello():
    print("Hello Decorator")
# def add(a,b):
#     print(a+b)
# add(3,3)

print("---*---*---*---*---*---*---*---*---*---*---*---*---*---*")
#Eg.2
def myfun(mf):
    def my():
        name=input("Enter your name : ")
        print("My Name is ",name)
        mf()
        print("thank you......!")
    return my()

@myfun
def hello():
    print("i'am an full stack developer")
    
print("---*---*---*---*---*---*---*---*---*---*---*---*---*---*")

def deco(decorator):
    def deco1():
        print("Statement 1")
        decorator()
        print("Statement 2")
    return deco1()
@deco
def dec():
    print("Statement 3")
    
print("---*---*---*---*---*---*---*---*---*---*---*---*---*---*")


    
