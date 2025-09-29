set_countries = {'Col', 'Mex', 'Per'}

# size
print(set_countries)
print("Size set_countries: ", len(set_countries))
print()

# add
set_countries.add('Arg')
set_countries.add('Par')
print("After add Arg and Par: ", set_countries)
print()

# update
set_countries.update({'Bol', 'Chi', 'Uru'})
print("After update Bol, Chi, Uru: ", set_countries)
print()

# remove and discard
set_countries.remove('Uru')
print("After remove Uru: ", set_countries)
# If the element does not exist, it raises a KeyError. Therefore, it is recommended to use discard() when you are not sure if the element exists.
set_countries.discard('Ven')
print("After discard Ven (not exist): ", set_countries)
print()

# clear
set_countries.clear()
print("After clear: ", set_countries)
print("Size set_countries after clear: ", len(set_countries))