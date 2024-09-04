# row methonds

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_in_word = ['one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine', 'ten']
new_lst = []

for number in numbers:
    new_lst.append(number*2)


print(new_lst)

lst_comp = [number*2 for number in numbers_in_word]
# gives possibility to manipulate iterator
print(lst_comp)


lst_comp = [number*2 for number in range(5)]
print(lst_comp)


lst_comp = [number*1 for number in range(1, 8)]
print(lst_comp)