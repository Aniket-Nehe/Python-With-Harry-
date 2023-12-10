#set Methods

# Joining Sets
# Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

# I. union() and update():
# The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

print('---- 1.Union (| or union()) ----')

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union_set = set1 | set2
union_set = set1.union(set2)

print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

print()



# II. intersection and intersection_update():
# The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

print('---- 2. Intersection (& or intersection())----')

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# intersection_set = set1 & set2
intersection_set = set1.intersection(set2)

print(intersection_set)  # Output: {4, 5}
print(set1)

print('---- 2.1 Intersetion Update ---')
set1.intersection_update(set2)
print(set1) 
print()

# III. symmetric_difference and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
print('---- 3. Symmetric Difference (^ or `symmetric_difference()`) ----')

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# symmetric_difference_set = set1 ^ set2
symmetric_difference_set = set1.symmetric_difference(set2)

print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

print()

print('---- 3.1 Symmetric diffrence Update ----')


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.symmetric_difference_update(set2)
s=set1.symmetric_difference_update(set2)

print(set1)
print(s)


# IV. difference() and difference_update():
# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

print('---- 4. Difference (- or difference())----')

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# difference_set = set1 - set2
difference_set = set1.difference(set2)

print(difference_set)  # Output: {1, 2, 3}

print(set1)

print()

print('----4.1 Difference Update ----')
# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Using difference_update to remove elements common to both sets from set1
set1.difference_update(set2)
s=set1.difference_update(set2)
print(set1)
print(s)



# Set Methods
# There are several in-built methods used for the manipulation of set.They are explained below

# isdisjoint():
# The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

print('----7. Disjoint Sets----')
set1 = {1, 2, 3}
set2 = {4, 5, 6}

are_disjoint = set1.isdisjoint(set2)
print(are_disjoint)  # Output: True

print()

# issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

print('----6. Superset (issuperset())----')

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

is_superset = set1.issuperset(set2)
print(is_superset)  # Output: True

print()

# issubset():
# The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

print('----5. Subset (issubset())----')

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

is_subset = set1.issubset(set2)
print(is_subset)  # Output: True

print()

# add()
# If you want to add a single item to the set use the add() method.

print('---- Add Method ----')

num_set = {1, 2, 3, 4, 5}
num_set.add(6)
print(num_set)

print()

# update()
# If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

print('---- Update Method ----')

num_set = {1, 2, 3, 4, 5}
num_set.update([6, 7, 8])
print(num_set)

print()

# remove()/discard()
# We can use remove() and discard() methods to remove items form list.

print('---- Remove Method ----')

num_set = {1, 2, 3, 4, 5}
num_set.remove(3)
# num_set.remove(10)
print(num_set)

print()


# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

print('---- Remove Method ----')

num_set = {1, 2, 3, 4, 5}
num_set.remove(3)
# num_set.remove(10)
print(num_set)

print()


# pop()
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

print('---- Pop Method ----')

num_set = {1, 2, 3, 4, 5}
popped_element = num_set.pop()
print("Popped Element:", popped_element)
print("Updated Set:", num_set)

print()

# del
# del is not a method, rather it is a keyword which deletes the set entirely.
print('---- del Method ----')
num_set = {1, 2, 3, 4, 5}
del num_set
print(num_set)

print()


# clear():
# This method clears all items in the set and prints an empty set.
print('---- Clear Method ----')

numbers_set = {1, 2, 3, 4, 5}
numbers_set.clear()

print("Set after clear:", numbers_set)

#Copy():
#create a copy of orignal set if we cahnge the copy set orignal set cannot change
print('---- Copy Method ----')

numbers_set = {1, 2, 3, 4, 5}
copied_set = numbers_set.copy()

print("Original Set:", numbers_set)
print("Copied Set:", copied_set)

copied_set.add(6)

print()

print("Original Set after modification:", numbers_set)
print("Copied Set after modification:", copied_set)

print()


# Check if item exists
# You can also check if an item exists in the set or not.

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")

