def is_balanced_parenthesis(string):
    stack = []

    for char in string:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            opening = stack.pop()
            if (opening == "(" and char != ")") or \
               (opening == "{" and char != "}") or \
               (opening == "[" and char != "]"):
                return False

    return len(stack) == 0

# Example usage
test_strings = ["(())", "{[()]}", "((())", "{[()]}]"]
for string in test_strings:
    result = is_balanced_parenthesis(string)
    if result:
        print(f"The string '{string}' has balanced parentheses.")
    else:
        print(f"The string '{string}' does not have balanced parentheses.")
