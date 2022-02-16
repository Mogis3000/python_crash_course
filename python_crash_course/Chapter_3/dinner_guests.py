dinner_guests = ['josh', 'peter parker', 'beltz', 'goku', 'ahmad', 'neil armstrong', 'stephen hawking', 'simba']
list_len = len(dinner_guests)
list_len_msg = f"We're having {list_len} guests for dinner!\n"
print(list_len_msg)

message = ", why don't we hang out and hit up a buffet?!?"

print(f'{dinner_guests[0].title()}{message}')
print(f'{dinner_guests[1].title()}{message}')
print(f'{dinner_guests[2].title()}{message}')
print(f'{dinner_guests[3].upper()}{message}')
# Goku's name was capitalized on purpose!
print(f'{dinner_guests[4].title()}{message}')
print(f'{dinner_guests[5].title()}{message}')
print(f'{dinner_guests[6].title()}{message}')
print(f'{dinner_guests[7].title()}{message}')

print(f"\nTurns out that {dinner_guests[3].upper()} can't come to dinner....he's dead! I know someone that would enjoy hanging out with us instead!\n")

dinner_guests = ['josh', 'peter parker', 'beltz', 'piccolo', 'ahmad', 'neil armstrong', 'stephen hawking', 'simba']

list_len = len(dinner_guests)
list_len_msg = f"We're having {list_len} guests for dinner!\n"
print(list_len_msg)

message = ", let's get together and grab some food?"

print(f'{dinner_guests[0].title()}{message}')
print(f'{dinner_guests[1].title()}{message}')
print(f'{dinner_guests[2].title()}{message}')
print(f'{dinner_guests[3].title()}{message}')
print(f'{dinner_guests[4].title()}{message}')
print(f'{dinner_guests[5].title()}{message}')
print(f'{dinner_guests[6].title()}{message}')
print(f'{dinner_guests[7].title()}{message}')

print("\nWe were able to make reservations for 12 so I'm going to invite a few more friends.\n")

dinner_guests.insert(0, 'cloud')
dinner_guests.insert(5, 'aeris')
dinner_guests.append('terry crews')

list_len = len(dinner_guests)
list_len_msg = f"We're having {list_len} guests for dinner!\n"
print(list_len_msg)

message = ", we're having a party and we hope you can join us!"

print(f'{dinner_guests[0].title()}{message}')
print(f'{dinner_guests[1].title()}{message}')
print(f'{dinner_guests[2].title()}{message}')
print(f'{dinner_guests[3].title()}{message}')
print(f'{dinner_guests[4].title()}{message}')
print(f'{dinner_guests[5].title()}{message}')
print(f'{dinner_guests[6].title()}{message}')
print(f'{dinner_guests[7].title()}{message}')
print(f'{dinner_guests[8].title()}{message}')
print(f'{dinner_guests[9].title()}{message}')
print(f'{dinner_guests[10].title()}{message}')


uninvited_message = "Well...it looks like you had too much fun at this restaurant last time and you were banned for food fights, sorry "
uninvited_guest = dinner_guests.pop(0)
print(f'{uninvited_message}{uninvited_guest.title()}')

uninvited_guest = dinner_guests.pop(0)
print(f'{uninvited_message}{uninvited_guest.title()}')

uninvited_guest = dinner_guests.pop(0)
print(f'{uninvited_message}{uninvited_guest.title()}')

uninvited_guest = dinner_guests.pop(0)
print(f'{uninvited_message}{uninvited_guest.title()}')

uninvited_guest = dinner_guests.pop(0)
print(f'{uninvited_message}{uninvited_guest.title()}')

uninvited_guest = dinner_guests.pop(0)
print(f'{uninvited_message}{uninvited_guest.title()}')

uninvited_guest = dinner_guests.pop(0)
print(f'{uninvited_message}{uninvited_guest.title()}')

uninvited_guest = dinner_guests.pop(0)
print(f'{uninvited_message}{uninvited_guest.title()}')

uninvited_guest = dinner_guests.pop(0)
print(f'{uninvited_message}{uninvited_guest.title()}')

still_invited = ", you behaved at the last party so you're still invited. See you at 7!\n"
print(f'{dinner_guests[0].title()}{still_invited}')
print(f'{dinner_guests[1].title()}{still_invited}')

list_len = len(dinner_guests)
list_len_msg = f"We're having {list_len} guests for dinner!\n"
print(list_len_msg)

del dinner_guests[1]
del dinner_guests[0]

print(dinner_guests)

list_len = len(dinner_guests)
list_len_msg = f"We're having {list_len} guests for dinner!\n"
print(list_len_msg)