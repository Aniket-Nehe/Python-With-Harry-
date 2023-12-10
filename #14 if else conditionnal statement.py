# if else
'''
age=int(input("Enter your age : "))
print("Your age is = ",age,"Years")

if(age>=18):
    print("You can drive")
else:
    print("You can't drive")
    '''
    
#if elif else

num=int(input("Enter The Number : "))

if num < 0:
    print("Number is Negitive")

elif num == 0:
    print("Number is Zero")
    
else:
    print("Number Is Positive")
    
# Nested if else:

num=int(input("Enter The Number"))
if num < 0:
    print("Number Is Negitive")
elif num >0:
    if num>0 and num<=10:
        print("number is between 0-10")
    elif num>10 and num<=20:
        print("number between 11-20")
    elif num>20 and num<=30:
        print("number between 21-30")
    elif num>30 and num<=20:
        print("number between 31-40")
    else:
        print("number is grether than 50")
else:
    print("Number is Zero")