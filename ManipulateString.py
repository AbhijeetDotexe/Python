class Manipulate:
    def __init__(self):
        self.string = ''

    def get_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print("Previously entered string in all capital letters: " + self.string.upper())


# Example usage
mani = Manipulate()
mani.get_string()
mani.print_string()
