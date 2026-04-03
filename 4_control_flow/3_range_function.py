# Generates arithmetic progressions:

for i in range(5):
    print(i)

# ---

# Start at another number, increment (step):
print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

# ---

# Iterate over the indices of a sequence:

a = ["Mary", "had", "a", "little", "lamb"]

for i in range(len(a)):
    print(i, a[i])

# ---

print(range(10))
print(sum(range(4)))
