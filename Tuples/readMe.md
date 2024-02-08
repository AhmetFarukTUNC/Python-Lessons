# What Is The Tuple?

## A tuple in Python is a data structure that is used to store an ordered sequence of elements. Tuples are similar to lists, but with one key difference: tuples are immutable. Once a tuple is created, its elements cannot be modified or changed. Tuples are defined using parentheses () and elements are separated by commas.

# Here's a simple example:

### my_tuple = (1, 2, 3, 'hello', 3.14)

## In this example, my_tuple is a tuple containing an integer, another integer, a string, and a floating-point number.

# You can access elements in a tuple using indexing, just like in lists:

### first_element = my_tuple[0]
### second_element = my_tuple[1]

# Tuples can also be nested, meaning you can have tuples within tuples:

### nested_tuple = (1, (2, 3), 'hello', (4.5, 5))

## You can use tuples for various purposes, such as representing fixed collections of values, returning multiple values from a function, or as keys in dictionaries (since they are immutable).

# It's important to note that while tuples are immutable, the objects they contain may be mutable. For example, a tuple may include lists as elements, and those lists can be modified even though the tuple itself cannot.

### mutable_tuple = ([1, 2, 3], 'hello')
### mutable_tuple[0].append(4)
### print(mutable_tuple)  # Output: ([1, 2, 3, 4], 'hello')


# In summary, a tuple is a collection of ordered elements that is immutable once created.
