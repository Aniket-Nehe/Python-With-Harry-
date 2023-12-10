# Map, Filter and Reduce
# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.


# map
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following 
# syntax:
# map(function, iterable)

# The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

#map function:
#Doubal of list items
numbers = [1, 2, 3, 4, 5]
numbers2= [6, 7, 8, 9, 10]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))
print()

#Addition of two numbers
add=map(lambda x,y:x+y,numbers,numbers2)
print(list(add))

#cube of list numbers
li=[3,6,11,8,3,4,5,3,7,0]
cube=map(lambda x:x**3,li)
print(list(cube))

# filter
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following 
# syntax:
# filter(predicate, iterable)

# The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# filter function:


numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)# Get only the even numbers using the filter function
print(list(evens))

#Greather tahn 4 number is list
li=[3,6,11,8,3,4,5,3,7,0]
greater=filter(lambda x: x > 4 , li)
print(list(greater))

#odd numbers
print(list(filter(lambda x: x%2 !=0 ,li)))



# reduce
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following 
# syntax:
# reduce(function, iterable)

# The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.
# The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.

# reduce function:

from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)# Calculate the sum of the numbers using the reduce function
print(sum)# Print the sum

print(reduce(lambda x,y: x*y ,numbers))


# It is important to note that the reduce function requires the functools module to be imported in order to use it.