#break and continnue statement

#break Statement
#Eg.1
for i in range(1,15):
    if(i==10):
        break 
    print(i)

#Eg.2
s="Aniket Lahanu Nehe"
for i in s:
    if i=="a":
        break
    print(i)
    
#Eg.3
i=0
while  True:
    print(i)
    i=i+1
    if(i%100==0):
        break
    
#continue statement
print("---------------continue statementt---------------")

#Eg.1
for i in range(1,15):
    if(i==10):
        continue
    print(i)

#Eg.2
s="Aniket Lahanu Nehe"
for i in s:
    if i=="a":
        continue
    print(i)
    
#Eg.3
i=0
while  True:
    print(i)
    i=i+1
    if(i%100==0):
        continue #this will skip 100 and print  infinite
    