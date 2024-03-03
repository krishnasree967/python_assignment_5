# Remove duplicates from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
unique_items = list(set(sample_list))
sample_tuple = tuple(unique_items)

min_number = min(sample_tuple)
max_number = max(sample_tuple)

print("unique items", unique_items)
print("tuple", sample_tuple)
print("min:", min_number)
print("max:", max_number)