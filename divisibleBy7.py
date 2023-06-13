def display_numbers():
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            print(num)

# Call the function to display the numbers
display_numbers()
