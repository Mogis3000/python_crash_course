# Python Crash Course pg 61 - Working with Part of a list
# Blake Barrow / 16 June 2021

#---------------------------------------------------------------------------------------
# SLICING A LIST
# In order to identify a part of a list, use the syntax: list_name[first index number: last index number +1]
players = ['charles', 'martina', 'michael', 'florence', 'eli']

'''
# this slice provides the first 3 values of the list
print(players[0:3])

# this slice provides the second thru fourth values of the list
print(players[1:4])

# this slice omits the first value, which Python interprets as the first index
print(players[:3])
#the slice above is identical to the first slice from this example

# similar to above, this slice omits the second value, which Python interprets as the end of the list
print(players[2:])

# this slice uses a negative value as the first index to tell Python to retrieve the entries that are before the second index, going backwards
print(players[-3:])
'''

# You can use a slice in a for loop if you want to loop through a subset of the elements in a list.

print('Here are the first three players on my team:')

for player in players[:3]:
	print(player.title())
	