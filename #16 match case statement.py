#match case statement same as a switch case in c,c++,java
#in python match case statement  dont required breack keyword

num1=int(input("Enter the first nummber"))
num2=int(input("Enter the first number"))
print("---------------------------------------------------------------------------------")
print("For Addition enter 1")
print("For Subtraction enter 2")
print("For multiplication enter 3")
print("For division enter 4")
print("--------------------------------------------------------------------------------")
operation=int(input("Enter the number to perform operations : "))
match operation:
    case 1 if operation==1 :
        print("Addition is = ",num1+num2)
    case 2 if operation==2:
        print("substraction is = ",num1-num2)
    case 3 if  operation==3 :
        print("Multiplication is  = ",num1*num2)
    case 4 if operation==4 :
        print("Division is = ",num1/num2)
    case _ :
        print("Enter the valid operation")