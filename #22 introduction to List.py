#List
# list are orderd collection of  data items.
#They store multiple items in single variable
#List items are separated by commas and enclosed within square Breakets [].
#list are changeable meaning we can alter them after creation.

l=[3,5,6,"Anii",True]
print(l)
print(type(l))
print(l[0]) #it will show elemennt of index 0 (i.e 3)
print(l[1])#5
print(l[2])#6
print(l[3])#Anii
print(l[4])#True


#List Index
#Each item/element in a list has its own index .this index can be used to accses any particular item from the list.The first item has index [0],second item has index [1],third item has index[2] and so  on.
# colors=["Red", "Green", "Blue", "Yellow", "Green"]
# print ("  [0]     [1]      [2]      [3]      [4]")

#Accesing list item
#positive indexing
print("--------------Positive indexing--------------")
print()
colors=["Red", "Green", "Blue", "Yellow", "Green"]
print(colors)
print ("  [0]     [1]      [2]      [3]      [4]")
print("Element in 1 position is : ",colors[1]) #green
print("Element in 3 position is : ",colors[3]) #Yellow
print("Element in 2 position is : ",colors[2]) #blue
print()
#Negitive indexing
print("--------------Negitive indexing--------------")
print()
color=["Red", "Green", "Blue", "Yellow", "Green"]
print(color)
print(" [-5]    [-4]     [-3]     [-2]     [-1]"  )
print("Element in -1 position is : ",color[-1])
print("Element in -3 position is : ",color[-3])
print("Element in -2 position is : ",color[-2])
print()
#Check wether an item in present in the list?
#We  can check if a given item is presen in the list .this is done using the " in " keyword
print("------------item in present in the list--------")
print()
colors=["Red", "Green", "Blue", "Yellow", "Green"]
if 'Green' in colors:
    print("Green is present")
else:
    print("Green is absent")
print()
#list Comprehention:
#List comprehention are usd for  creating new lists from other iterables like lists,tuples,dictionaries,set,and even in array and string
print("------------List Comprehention---------------")
print()
name=["Milo","Sarah","Bruno","Anastasia","Rosa"]
name_with_o=[item for item in name if "o" in item]
print(name_with_o)
print("---EG2---")
#eg2
num=[i for  i  in range(10)]
print(num)







