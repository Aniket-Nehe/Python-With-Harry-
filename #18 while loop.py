#print 1-10 using while loop
# Eg.1
#initilize variable
i=1
#while(condition)
while i<11:
    print(i)
#increment/decrement
    i=i+1

# Eg.2
#print number reverse 5-0
count=5
while(count>0 ):
    print(count)
    count=count-1
print()

#Eg.3
# while else
#if while condition is false then else is excuted
count=5
while(count>0 ):
    print(count)
    count=count-1
else:
    print("This is else")

#imulate do while loop
i=0
while  True:
    print(i)
    i=i+1
    if(i%100==0):
        break
