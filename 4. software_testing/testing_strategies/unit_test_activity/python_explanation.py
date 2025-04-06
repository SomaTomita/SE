# In order and duplicate elements
from doctest import OutputChecker


my_list = list("abc")  # → ['a', 'b', 'c']

# No order and no duplicate elements
my_set = set("def")  # → {'d', 'e', 'f'}

# Access by index
my_list[0]  # → 'a'
my_set[0]  # → error (no order)

# Search
# slow (linear search)
print("b" in my_list)  # output: True
# fast (hash search)
print("d" in my_set)  # output: True

# Mutable: both can add elements
my_list.append("d")
my_set.add("g")
print("List after append:", my_list)  # output: ['a', 'b', 'c', 'd']
print("Set after add:", my_set)  # output: {'d', 'e', 'f', 'g'}

# --------------------------------------------------

example_pad = {
    2: {"a", "b", "c"},
    3: {"d", "e", "f"},
}

current_letters = example_pad.get(2, set())
print(current_letters)
# output: {'a', 'b', 'c'}

current_letters = example_pad.get(3, set())
print(current_letters)
# output: {'d', 'e', 'f'}

for key, value in example_pad.items():
    print(key, value)
# output:
# 2 {'a', 'b', 'c'}
# 3 {'d', 'e', 'f'}

print(set(example_pad.keys()))
# output: {2, 3}

print(set(str(example_pad.keys())))
# output: {'2', '3'}

# --------------------------------------------------

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
# True if all elements of A are in B
A.issubset(B)  # → True

# True if all elements of B are in A
B.issubset(A)  # → False

# True if A and B have no elements in common
A.isdisjoint(B)  # → Fals
