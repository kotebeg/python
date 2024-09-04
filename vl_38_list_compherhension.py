# row methonds

numbers = [1, 2, 3, 4, 5, 6, 7]
new_lst = []

for number in numbers:
    new_lst.append(number*2)


print(new_lst)

lst_comp = [number*2 for number in numbers]
# gives possibility to manipulate iterator
print(lst_comp)