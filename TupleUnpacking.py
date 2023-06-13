my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
half_length = len(my_tuple) // 2

first_half = my_tuple[:half_length]
last_half = my_tuple[half_length:]

print(*first_half)
print(*last_half)
