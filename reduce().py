# ===>  The reduce() function is used to reduce a list (or any iterable) to a single value.
# ===>  It does this by applying a function to the first two elements, 
#       then taking the result and applying the function to the next element, and so on.
# ===>  It works from left to right.

# # Syntax of reduce():

# from functools import reduce

# reduce(function, iterable[,initializer])


# 🔹Parameters:
# function == A function that takes two arguments and returns a single value.

# iterable == A sequence (like list, tuple).

# initializer (optional) == A value that is placed before the items of the iterable in the calculation.


# ###########################################################################################


# 🔹 How it works:

# reduce() applies the function to the first two items of the iterable.

# Then it applies the function to the result and the next item.

# This continues until the iterable is reduced to a single value.

############################################################################################

# 🔹 Example 1: Sum of numbers

# from functools import reduce

# numbers = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)  
# # 
# # Output: 10

# working
# Step 1: 1 + 2 = 3  
# Step 2: 3 + 3 = 6  
# Step 3: 6 + 4 = 10



# >>>>>.........
# from functools import reduce

# numbers = [1, 2, 3, 4]

# def add(x, y):
#     return x + y

# result = reduce(add, numbers)
# print(result)





# 🔹 Example 2: Using initializer

# from functools import reduce

# numbers = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, numbers, 10)
# print(result)


#working
# Step 1: 10 + 1 = 11  
# Step 2: 11 + 2 = 13  
# Step 3: 13 + 3 = 16  
# Step 4: 16 + 4 = 20


# 🔹 Example 3: Find maximum

from functools import reduce

numbers = [3, 5, 2, 8, 1]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum) 

#  # Output: 8


# working
# Step 1: compare 3 and 5 → 5  
# Step 2: compare 5 and 2 → 5  
# Step 3: compare 5 and 8 → 8  
# Step 4: compare 8 and 1 → 8


from functools import reduce

def find_max(a, b):
    return a if a > b else b

numbers = [3, 5, 2, 8, 1]
maximum = reduce(find_max, numbers)
print(maximum)  # Output: 8







# ........................................................................................................

# 1️⃣ Using reduce() with a Tuple

# from functools import reduce

# numbers = (2, 3, 4)  # This is a tuple
# result = reduce(lambda x, y: x * y, numbers)
# print(result)                                             # Output: 24 (2 * 3 * 4)


# 2️⃣ Using reduce() with a Set

# from functools import reduce

# numbers = {5, 2, 3}  # This is a set
# result = reduce(lambda x, y: x + y, numbers)
# print(result)                                             # Output: 10 (but order may vary)


# 3️⃣ Using reduce() with a String

# from functools import reduce

# chars = ["P", "y", "t", "h", "o", "n"]
# result = reduce(lambda x, y: x + y, chars)
# print(result)                                                          # Output: "Python"

