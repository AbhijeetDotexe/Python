def remove_spaces_recursive(string):
    if len(string) == 0:
        return ""

    if string[0] == " ":
        return remove_spaces_recursive(string[1:])
    else:
        return string[0] + remove_spaces_recursive(string[1:])


# Example usage
my_string = "Hello, World!"
string_without_spaces = remove_spaces_recursive(my_string)
print(string_without_spaces)
