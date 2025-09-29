# se pueden modificar
# No tienen un orden
# No permiten duplicados

set_countries = {'Col', 'Mex', 'Per'}
print(set_countries)
print(type(set_countries))

set_types = {0, 2.5, 'Hola', True}
print(set_types)

set_from_string = set('Hola')
print(set_from_string)
print()
numbers = [2, 2, 3, 4, 5, 5, 5, 6]
print(numbers)
set_from_list = set(numbers)
print(set_from_list)
unique_numbers = list(set_from_list)
print(unique_numbers)