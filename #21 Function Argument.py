# Function Argumenta and return statement
#there are four of argument that we can provide in a function:
# -Default argument
# -Keyword Argument
# -Variable length arguments
# -required arguments

# -Default Argument
''' we can provide a Default value while creating a function. This Way The function assume a default  value even if a value is not provided in the funnction call for that argument'''
print("-------------------D-A Eg.1-----------------")
def multiplication(a=10,b=5):
    print('multiplication is = ',a*b)
# multiplication(5,5)# op25
multiplication(9) #a=9 and b=default value i.e 5
#multiplication() #50
print("-------------------D-A Eg.2-----------------")
def name(fname, mname="john",lname="singh"):
    print("Hello",fname,mname,lname)
name("anii")
name("ritesh","ram")
name("Anii","lahanu","Nehe")
print()
print()


# -keyword Argument
'''we can provide argument with key=value,this way the interpreter recognizes the argument by the parameters name .hence,the order in which the argument are passed does not matter'''

print("-------------------keyword-A Eg.1-----------------")
def multiplication(a,b):
    print('multiplication is = ',a*b)
# multiplication(a=5,b=5)# op25
multiplication(b=9 ,a=10) 

print("-------------------keyword-A Eg.2-----------------")
def name(fname, mname="john",lname="singh"):
    print("Hello",fname,mname,lname)

name(fname="Anii",lname="Nehe",mname="lahanu")#order does not mater
print()
print()

# -required Argument
'''in case we don't pass the argument with key=value syntax,then that it is necessary to pass the arguments in the correct positionl orders and the number of arguments passed should match with actual function definition'''

print("-------------------Req-A Eg.1-----------------")
def multiplication(a,b):
    print('multiplication is = ',a*b)
# multiplication(a=5,b=5)# op25
multiplication(5,60) #both argument are required if we pass only 1 parameter it will show error

print("-------------------req-A Eg.2-----------------")
def name(fname, mname,lname="singh"):
    print("Hello",fname,mname,lname)

name("anii","lahanu")#here the default value of lname is pass 
#if default value does not pass it will show error
print()
print()

# -Variable length  Argument
'''Some times we may need to pass more than one aggu than those defined in thw actual function .this  can be done using variable-length argument'''

#there is 2 way to achive this:
'''Arbitrary Argument:
        while creating a function ,pass a * before the parameter name while defining the functon accesses the argument by processing them in the form of tuple '''

print("------------variable len Eg.arbitarary argu(*) --------------")
def name(*name):
    print(name[0],name[3],name[2])
name("anii","adii","raj","Sham","Shubh")#o/p :anii sham raj
print()
print()

''' keyword Arbitrary Argument:
        while creating a function ,pass a ** before the parameter name while defining the functon accesses the argument by processing them in the form of Dictionary '''

print("------------variable len Eg.keyword arbitarary argu(**) --------------")
def name(**name):
    print("hello",name['fname'],name['mname'],name['lname'])
name(fname="rit" ,mname="Raj",lname="Roy")
print()
print()


