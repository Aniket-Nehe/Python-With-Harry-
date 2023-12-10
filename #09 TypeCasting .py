#Type casting

#typecasting :-The conversion of ond datatype to  another datatype is Known as "Type Casting"

a="1"
b="2"
print(int(a)+int(b)) #converting string to int

#TYPE OF TYPECASTING
#Explicit conversion :-Explicit typecasting done via developer or programer intravention or manually as per the requiremt ,is known as explicit typecasting

#E.g
string="10"
num=5
#print(string+num) #it geve an error we can  not add string and integer
str_num=int(string) #convert str into int
print(str_num+num)

#implicit typecasting :- one datatype is converted into other by the python interpriter itself(automatically).this is called implecit typecasting

#e.g
a=1.9
b=8
print(type(a))
print(type(b))
c=a+b
print(c,type(c)) #python automatically convert c to flote and as it is flote addition
