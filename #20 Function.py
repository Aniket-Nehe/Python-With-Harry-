#Function:
#-function is a block of code that performs a specific task whenever it is called.we can call function multiple time

# Creating function
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
calculateGmean(5,7)#a=5,b=7
calculateGmean(10,5)#we can call function Multiple time
calculateGmean(20,10)

#check greather number using  function

def isgreter(a,b):
    if a>b:
        print("First number is greather")
    else:
        print("Second number is greather")
isgreter(10,9)

#pass
def isprime(a,b):
    pass #pass keyword can skip this function 


#There is 2 Types of function
# 1.Built-in Function
# 2.User-Defined Function

#Built-in Function:
#this function are defined and pre-coded in python
#e.g
#min() ,max() ,len() ,sum() ,type() ,range() ,dict() ,list() ,tuple() ,set() ,print() ,etc.

#User-Defined Function
#we can create function to perform specific task as per our needs.such function are called  user-defined function

#Syntax:
#def function_name(parameters):
#   code and statement

# -create  a function using the "def" keyword,followed by the function name,followed by a paranthesis(()) and (:)
# -any parameters and arguments should be placed within the parentheses

#Calling a Function:
# we call a funnction by giving the function name,followed by parameters(if any) in the parenthesis.

def name(fname,lname):
    print("Hello",fname,lname)
name("Aniket","Nehe") #calling function

