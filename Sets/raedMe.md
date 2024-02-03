# In Python, a "set" is a built-in data structure that represents an unordered collection of unique elements. The key characteristics of a set in Python are:

# What is those?

1.)Uniqueness: A set cannot contain duplicate elements. If you try to add an element that is already present, it will not create a duplicate.

2.)Unordered: The elements in a set have no specific order. Unlike lists or tuples, you cannot access elements in a set by index.

3.)Mutable: Sets are mutable, meaning you can add and remove elements after the set is created.

# The set data type is useful when you need to perform operations like union, intersection, difference, and symmetric difference between sets. You can create a set using curly braces {} or the set() constructor.


# Here's an example:


# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to the set
my_set.add(6)

# Removing elements from the set
my_set.remove(3)

# Performing set operations
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)

# In Summary,in this example, union_set will contain all unique elements from both set1 and set2, intersection_set will contain common elements, difference_set will contain elements that are in set1 but not in set2, and symmetric_difference_set will contain elements that are unique to each set.