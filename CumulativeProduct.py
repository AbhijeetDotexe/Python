def cumulative_product(numbers):
    result = []
    product = 1
    for num in numbers:
        product *= num
        result.append(product)
    return result

# Example usage
my_numbers = [1, 2, 3, 4, 5]
cumulative_result = cumulative_product(my_numbers)
print(cumulative_result)
