def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Example usage
my_string = "Hello, World!"
character_counts = count_characters(my_string)
print(character_counts)
