# Create list
my_list = []

# Append 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at second position (index 1)
my_list.insert(1, 15)

# Extend list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove last element
my_list.pop()

# Sort in ascending order
my_list.sort()

# Find and print index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)