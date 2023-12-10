#String formatting in Python
#string formatting can be done in python using the format method
print("--------------Format String---------------")
#1
latter="Hey my name is {1} and I am from {0}"
country="India"
name="Anii"
print(latter.format(country,name))
print()
#2
txt="For only {price:.2f} dollars!"
print(txt.format(price=49.0999))

#f-string in Python
print("----------------f-String Methods for int--------------------")
print(f"{0}") # No Space is Allowed in brace bracket and it cannot be blank as we saw previously in format method
print(f"Power of {'Captain America'} is {'1000 HP'}.")

name, age= 'Roger',32
print(f"My name is {name} and my age is {age}") # Representing  with key

print(f"Multiplying 10x5={10*5}")

print()

print('----------Integer Datatype-----------')  # Bydefault Numbers are align to the left
x=100
print(f"13: {x:d}") #Repsenting value with Int Datatype 'd' 
print(f"14: {x:6d}") # Having width 6
print(f"15: {x:06d}") # Having width 6 and padding with zero from Left side
print(f"16: {x:+6d}") # + sign added to number 
print(f"17: {x:+06d}") # + sign added at starting of the number after that zero added as a padding, but overall width will be of 6 only...Only zero can be used in place of padding.
print(f"18: {x:<+06d}") # By default padding is from the left side as we saw in line 17 ... In this case we are using right align so padding will be apply to the right of the number
print(f"19: {x:<6d}")   # By default number are align to the right, but still we align to the left 
print(f"20: {x:#<6d}") # Aligning Number to the right
print(f"21: {x:*>6d}") # First number will align to the right after that it will be fill with star
print(f"22: {x:*<6d}") #First number will align to the right after that it will be fill with star
print(f"23: {x:^7d}") # Number will align at the center but from the right side
print(f"24: {x:*^7d}") # Number will align at the center from the right side and remaining part will be fill with *

print()

# Thousand seperator
print("-------------- Thousand Seperator-----------------")
print(f"Thousand Seperator using ','  : {1234567890:,}")
print(f"Thousand Seperator using  '_' : {1234567890:_}")

print()

print('------------- First Assigning Value and then Passing Value -------------')
name='Captain America'
power='1000 HP'
print(f'Power of {name} is {power} .')

print()
print('----------- Passing Tuple value -------------')
tup1=(100,200,300)
tup2=(500,600,700)
print(f'Tuple 1 value: {tup1[0]} {tup1[1]} -- Tuple 2 Value: {tup2[0]} {tup2[2]}')

print()

print('-------- Passing Dictionaries Value through Index and Also Specifying datatype -------------')
dict1 ={'Captain America':1000 ,'Iron Man':2000}
dict2 ={'Thor':3000 ,'Spider-Man':4000}
print(f'Dictionary 1 value: {dict1["Captain America"]} {dict1["Iron Man"]} -- Dictionary 2 Value: {dict2["Thor"]} {dict2["Spider-Man"]}')
print(f'Dictionary 1 value with datatype: {dict1["Captain America"]:d} {dict1["Iron Man"]:d} -- Dictionary 2 Value with datatype: {dict2["Thor"]} {dict2["Spider-Man"]}')


print()
print('---------- Using the Function ----------------')
name ='avEngers'
print(f"Converting in Upper case : {name.upper()}")
print(f"Converting in Lower case : {name.lower()}")
print(f"Converting in Title  : {name.title()}")

print()

print(f'Showing curly bracket in output: {{10}}')
print()
print()
print("----------------f-String Methods for float--------------------")
print()


print(f"{5}") # No datatype is Defined It wil be consider as a Stirng


print()


x=100.12
print('----------Float Datatype-----------')  # Bydefault Numbers are align to the left
print(f"11: {x:f}  If we provide precission by defaut it wi take 6 digit after point ") #Repsenting value with Int Datatype 'f' 
print(f"12: {x:7f}  Giving output of 10 width becouse, by default it takes 6 digit after point ")  
print(f"14: {x:.3f} Giving output after 3 precision") 
print(f"15: {x:08.1f}") # Having width 8 and padding with zero from Left side
print(f"16: {x:+8.1f}") # + sign added to number 
print(f"17: {102:+08.1f}".format(x=102)) # + sign added at starting of the number after that zero added as a padding, but overall width will be of 8 only...Only zero can be used in place of padding.
print(f"18: {102:<+08.1f}".format(x=102)) # By default padding is from the left side as we saw in line 17 ... In this case we are using right align so padding will be apply to the right of the number
print(f"19: {x:<8.1f}")   # By default number are align to the right, but still we align to the left 
print(f"20: {x:#<8.1f}") # Aligning Number to the right
print(f"21: {x:*>8.1f}") # First number will align to the right after that it will be fill with star
print(f"22: {x:*<8.1f}") #First number will align to the right after that it will be fill with star
print(f"23: {x:^7.1f}") # Number will align at the center but from the right side
print(f"24: {x:*^7.1f}")
print(f"25: {1234567.89:,}")
print(f"25: {123456789.89:_}")

print()
print()
print("----------------f-String Methods for Strinng--------------------")
print()
print("--------- Formatting String --------")
x='Aven'
print(f"3: {x}")
print(f"4: {x:8}")
print(f"5: {x:<8}")
print(f"6: {x:>8}")
print(f"7: {x:#<8}")
print(f"8: {x:#>8}")
print(f"9: {x:#^8}")

print()

print('-------- Truncating String ------------')
print(f"14: {x}")
print(f"15: {x:8s}")
print(f"16: {x:<8.2s}")
print(f"17: {x:>8.2}")
print(f"18: {x:*<8.2}")
print(f"19: {x:*>8.2}")
print(f"20: {x:*^8.2}")
















