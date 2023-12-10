# Tuple

# Manipulating Tuples
#tuple are immutable,hence if you want to add,remove or change tuple items ,then first you must convert the tuple to a list.then perform opetation on that list and convert it back to tuple
print("-------------Manipulating Tuples---------------")

countries=("Spain","Italy","India","England","Germany")
temp=list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Japan"
countries=tuple(temp)
print(countries)
print()

#tuple Methods
#tuple is immutable type of collection of element it have limited built in Methods

#Count()
#the count method of tuple return the number of times the given element appers in the tuple
print("---------------- Count() ---------------")
print()
tup=(1,2,3,2,4,1,5,4,3,2)
res=tup.count(2)
print(res)
print()

#Index()
#The index() method the first occurrence of the given element from the tuple
print("---------------- index() ---------------")
print()
tup=(1,2,3,2,4,1,5,4,3,2)
res=tup.index(1)
print(res)
print()
#tuple scliing
print("---------------- tuple scliing ---------------")
print()
tup=(1,2,3,2,4,1,5,4,3,2)
res=tup.index(1,4,8) #tuple.index(element,start,end)
print(res)
print()
#value Error
#this method rises a ValueError if the element is not found in the tuple
print("---------------- value error ---------------")
'''print()
tup=(1,2,3,2,4,1,5,4,3,2)
res=tup.index(11) #tuple.index(element,start,end)
print(res)
'''
print()
#len
#len of tuple
print("----------------Len()---------------")
print()
tup=(1,2,3,2,4,1,5,4,3,2)
res=len(tup)
print(res)
print()