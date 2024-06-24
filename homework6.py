my_dict = {'Diana': 1995, 'Irina': 1986, 'Svetlana': 1971, 'Sofia': 1998}
print(my_dict)
print(my_dict['Diana'])
my_dict['Valya'] = 1956
print(my_dict['Valya'])
my_dict.update({'Nikolya': 2000,
                'Olga': 1984})
print(my_dict)
a = my_dict.pop('Diana')
print(my_dict)
print(a)
# множество

my_set = {1, 5, 'hard', (9, 4), 3, 5, (9, 4), 8}
print(my_set)
my_set.update({'Ohh', 65, (7, 5)})
print (my_set)
print(my_set.discard(5))
print(my_set)