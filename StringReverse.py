class StringReverser:
    def __init__(self):
        self.input_string = ''

    def get_string(self):
        self.input_string = input("Enter a string: ")

    def reverse_string(self):
        words = self.input_string.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words


# Example usage
reverser = StringReverser()
reverser.get_string()
reversed_string = reverser.reverse_string()
print("Reversed string:", reversed_string)
