first_name = "   Peter"
last_name = "Parker      "

full_name = f'{first_name} {last_name}'

print("1: Full name with extra spaces")
print(full_name)

print("2: Full name with spaces stripped")
print(full_name.strip())

print("3: First (lstrip) and last name (rstrip) individually stripped")
print(f'{first_name.lstrip()} {last_name.rstrip()}')