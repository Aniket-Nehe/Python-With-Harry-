#taking input from user
name=input("Enter your name")
print("My Name is",name)

#write a program to add 2 number,get number from user
x=input("Enter The First Number") #12
y=input("Enter The Second Number") #12
#it consider input as a string if we enter the number but it consider number as a string 
print(x+ y)  #it concat the string output is =1212

#1 using exlicit conversion
x=input("Enter The First Number") #12
y=input("Enter The Second Number") #12
#here it will accept num as string and then convert into string
print(int(x)+ int(y)) #now convert the string into int and it will display the adiition of x and y output is= 24

#2 Using int in input
#it directly accept only the int value if you want to input as a floot,bool,compex  replece into to another datatype
x=int(input("Enter The First Number")) #12
y=int(input("Enter The Second Number")) #12
print(x+ y) #output =24
