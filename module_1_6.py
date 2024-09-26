my_dict = {'Anton' : 1999, 'Alex' : 1997, 'Sasha' : 2001}
print(my_dict)
print(my_dict.get('Alex'))
print(my_dict.get('Max'))
my_dict.update({'Denis' : 1995, 'Masha' : 2003})
print(my_dict)
a = my_dict.pop('Alex')
print(a)
print(my_dict)

my_set = {1, 2 , 1, 1, 3, 4 , 5}
print(my_set)
my_set.add(6)
my_set.add(7)
my_set.discard(1)
print(my_set)
