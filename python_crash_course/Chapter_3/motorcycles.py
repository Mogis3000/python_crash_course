# This code is to teach how to edit items in a list
# Blake Barrow / 10 June 2021


#---------------------------------------------------------------------------
# This is where I build the first list of motorcycles
# Values in a list are identified by their position, the first position is value 0
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# I now add Ducati to the list by overwriting position 0, which was honda
motorcycles[0] = 'ducati'
print(motorcycles)

# I add honda back into the list of motorcycles, but it is added at the end
motorcycles.append('honda')
print(motorcycles)


#---------------------------------------------------------------------------
# I now start with an empty list and will build it as I go

# This line is just to make some space from the previous section


motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# The insert command adds an entry into the position specified
motorcycles.insert(0, 'ducati')
print(motorcycles)

# The del command removes a specified entry
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)


#---------------------------------------------------------------------------
# This section begins exercises with popping list items
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)



#---------------------------------------------------------------------------
# This exercise is for how to use a popped value
motorcycles = ['honda', 'yahama', 'suzuki']

last_owned = motorcycles.pop()
print(f'The last motorcycle I owned was a {last_owned.title()}.')

first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')


#---------------------------------------------------------------------------
# This exercise is for how to work with item values

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)


#---------------------------------------------------------------------------
# This exercise is for how to work with items that have been removed

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me!')








#---------------------------------------------------------------------------
