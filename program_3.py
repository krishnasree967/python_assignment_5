# Create a Python set such that it shows the element from both lists in a pair.

list_1= [2, 3, 4, 5, 6, 7, 8]
list_2= [4, 9, 16, 25, 36, 49, 64]

pairs = zip(list_1, list_2)

result_set = set(pairs)

print("Result is", result_set)