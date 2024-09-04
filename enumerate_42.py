
# Enumerate Funion 42

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print(Dict)

for key, value in Dict.items():
    print(key, value)
    pass


# enumerate

pylist = ["Geeks", "for", "Geeks"]
for index, word in enumerate(pylist):
    print(index, word)

print("change index --->")

for index, word in enumerate(pylist, start=4):
    print(index, word)


# returns tuple, index, value
print(list(enumerate(pylist)))

# returns dict, index, values, 
print(dict(enumerate(pylist)))