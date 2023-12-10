#Length of A string
#We can find the lenth  of string using len() fumction
name="Aniket Lahanu Nehe"
print(len(name))

#slicimng of string
city="Sangmner"
citylen=len(city)
print(citylen)

#syntax
#print(variable_name[start:end:step])
print(city[1:])
print(city[:1])
print(city[1:5])
print(city[-1:])
print(city[:-1])
print(city[-3:-1])
print(city[-8:-6])

#Quiz:
nm="harry"
print(nm[-4:-2])

#print reverse String
village="Sawargaon tal"
print(village[::-1], end="\n")# Step is -1 so it will print string  in reverse

#print even index characther
str1="Aniket Nehe"
print(str1[0::2], end="\n")

#print odd index characther
str2="Aditya Nehe"
print(str2[1::2], end="\n")

