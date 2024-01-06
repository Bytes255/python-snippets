# This is a list AKA array, can contain multiple types of data
# It can also contain other lists
my_list = ["foo", 5.5, (0,1), 5, [1]]

# Python's loops let you iterate directly with the elements
# of the array
print("My list contains:")
for item in my_list:
    print(f"-> {item} which is a {type(item)}")
    
# This is a bidimensional list AKA a matrix
# is a list that contains other lists inside
my_matrix = [[1, 2], [3, 4]]

# The graphical representation of this matrix is
#   |1  2| ^ the vertical axis is called "column"
#   |3  4| > the horizontal axis is called "row"

print("\nMy matrix contains")
# You can loop through them with a nested loop
for row in my_matrix:
    for element in row:
        print(f"-> {element}")
        
# The loop is reading the matrix as we read a book
# Left to right, top to bottom

# You can also loop througt a range()
# The first argument is the beginning, in this case we start in 1
# The second argument is the end, which won't be used
# Think about the end as (n - 1)
print("\nMy range contains")
for num in range(1, 4):
    print(num)
    
# With this loop you can add elements to a list
# To do this we use the .append() method
empty_list = []
for num in range(10):
    empty_list.append(num)

print(f"\nWe've filled this list with data {empty_list}")

# I rather use the list comprehension
# Which is other kind of loop after all
list_comprehension =[x for x in range(10)]
print(f"List comprehension is less difficult than it seems {list_comprehension}")
