# This code is for Python Crash Course page 46 - Lists
# Blake Barrow / 15 June 2021

# Think of at least 5 places in the world you'd like to visit
# Store the locations in a list. Make sure the list is not alphabetical
places = ['rome', 'victoria', 'sakura blossom festival', 'great wall of china', 'sydney']

# Print the list in its original order
print(places)

# Use sorted() to print list in alphabetical order without modifying the actual list
print(sorted(places))

# Prove the list has not been alphabetized
print(places)

# Use reverse() to change the order of the list and then print it to show the reversed list
places.reverse()
print(places)

# Use reverse() again to change list back to its original state and print it to view the list
places.reverse()
print(places)

# Use sort() to change your list so it's alphabetized; print the list to show it
places.sort()
print(places)

# Use sort() to change your list so it's in reverse alphabetical order; print the list to show it
places.sort(reverse=True)
print(places)