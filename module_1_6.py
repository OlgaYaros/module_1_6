my_dict = {'Ivan':1980, 'lyba':1950, 'Sergey':1958, 'Lera':2000}
print(my_dict)
print(my_dict['lyba'])
print(my_dict.get('Alex'))
my_dict.update({'Pasha':2003, 'Grisha':2011})
print(my_dict.pop('Sergey'))
print(my_dict)
my_set = {1, 3, 5, 1, 'box', 4.3, 3, 'dog', 2.7, 'fox', 4.3, 'box'}
print(my_set)
my_set.add(7)
my_set.add('Sveta')
my_set.discard(5)
print(my_set)