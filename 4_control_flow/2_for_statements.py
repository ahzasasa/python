# for statement: Iterates over the items of any sequence (a list or a string).

# Measure some strings:
words = ["cat", "window", "defenestrate"]

for word in words:
    print(word, len(word))

# ---

# Loop over a copy of the collection or to create a new collection:

users = {
    "James": "active",
    "Jake": "inactive",
    "Hongjoong": "active"
}

# Strategy: Iterate over a copy.

for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

print(users)
        
# Strategy: Create a new collection.

active_users = {}

for user, status in users.items():
    if status == "active":
        active_users[user] = status

print(active_users)