def count_file(file_path):
    character_count = 0
    word_count = 0
    line_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
            character_count += len(line)
            word_count += len(line.split())

    return character_count, word_count, line_count


# Example usage
file_path = 'example.txt'
char_count, word_count, line_count = count_file(file_path)

print(f"Character count: {char_count}")
print(f"Word count: {word_count}")
print(f"Line count: {line_count}")
