#List Methods
# 1. l.sort will sort it in ascending order.
print("--------------------'Sort'-----------------------")
print()
list=[8,7,9,4,3,0,1,2,5,6]
list.sort()
print(list)

list2=["voilet","inddigo","blue","green"]
list2.sort()
print(list2)
print()

# 2. l.sort(reverse=True) will sort it in descending order
print("----------------'Sort-descending'-----------------")
print()
list=[8,7,9,4,3,0,1,2,5,6]
list.sort(reverse=True)
print(list)

list2=["voilet","inddigo","blue","green"]
list2.sort(reverse=True)
print(list2)
print()

# 3. l.reverse() reverses the list
print("------------------'Revers()'---------------------")
print()
list=[8,7,9,4,3,0,1,2,5,6]
list.reverse()
print(list)

list2=["voilet","inddigo","blue","green"]
list2.reverse()
print(list2)
print()

# 4. l.index( ) gives the first index of an instance present in a list
print("------------------'Index()'----------------------")
print()
list=[8,7,9,4,3,0,1,2,5,6,4]
print(list)
print(list.index(4))

list2=["voilet","inddigo","blue","green"]
print(list2)
print(list2.index("inddigo"))
print()

# 5. l.count() gives the total number of a particular instances present in a list.
print("-------------------'Count()'---------------------")
print()
list=[8,7,9,4,3,0,1,2,5,6,4]
print(list)
print(list.count(4))

list2=["voilet","inddigo","blue","green"]
print(list2)
print(list2.count("inddigo"))
print()

# 6. l.copy() copies the list
#this can be done to perform operations on the list without modifying orignal list
print("-------------------'copy()'-----------------------")
print()
list=[8,7,9,4,3,0,1,2,5,6,4]
copy_list=list.copy()
print(list)
print(copy_list)

list2=["voilet","inddigo","blue","green"]
copy_list2=list2.copy()
print(list2)
print(copy_list2)
print()

# 7. l.append() adds the given argument to the end of the list.
print("-------------------'append()'---------------------")
print()
list=[8,7,9,4,3,0,1,2,5,6]
print(list)
list.append(100)
print(list)
print()

list2=["voilet","inddigo","blue","green"]
print(list2)
list2.append("Red")
print(list2)
print()

# 8. l.insert() adds the given argument at the given index position
#this method insert item at the given index .user has to specify index index and the item to be inserted within the insert() method
print("-----------------insert()---------------------")
print()
list=[8,7,9,4,3,0,1,2,5,6]
print(list)
list.insert(2,999)#add 999 after 7
print(list)
print()
list2=["voilet","inddigo","blue","green"]
print(list2)
list2.insert(0,"black")
print(list2)
print()

# 9. l.extend() adds the provided list to the existing list.
#this method adds an entire list or any other datatype(set,tuple,dictionary)to  the existing list
print("------------------'extend()'---------------------")
print()
list=[8,7,9,4,3,0,1,2,5,6]
list2=["voilet","inddigo","blue","green"]
print(list)
print(list2)
list.extend(list2)
print(list)#extended list
print()

# 10.you can concatonate two lists by simply a+b
print("----------'concatination list (+)'------------")
print()
list=[8,7,9,4,3,0,1,2,5,6]
list2=["voilet","inddigo","blue","green"]
print(list)
print(list2)
concat=list+list2
print(concat)#combine list
print()

#11.Use the clear() method to remove all items from the list
print("------------------'clear()'---------------------")
print()
list=[8,7,9,4,3,0,1,2,5,6]
print(list)
list.clear()
print(list)
print()

#12.Assign an empty list to the original list
print('--------Slicing [:] To Clear A List --------')
print()
list2 = ["voilet","inddigo","blue","green"]
print(list2)
list2[:] = [] 
print(list2)  # Output: []
print()

#13. pop([i]): Removes and returns the element at index `i`. If `i` is not
#specified, it removes and returns the last element.

print("-------------------'pop()'---------------------")
print()
list=[8,7,9,4,3,0,1,2,5,6]
print(list)
pop_item=list.pop(3)
print(pop_item)
print(list)
print()
list2=["voilet","inddigo","blue","green"]
print(list2)
pop_item2=list2.pop(2)
print(pop_item2)
print(list2)
print()

#14. len(): Returns the number of elements in the list
print("--------------------'Len()'-----------------------")
print()
len_list=[8,7,9,4,3,0,1,2,5,6]
list=len(list)
print(list)

list2=["voilet","inddigo","blue","green"]
len_list2=len(list2)
print(len_list2)
print()

#This is list methods