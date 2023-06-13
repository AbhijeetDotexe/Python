import numpy as np

def add_matrices():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    print("\nEnter the elements of the first matrix:")
    matrix1 = np.zeros((rows, columns))
    for i in range(rows):
        for j in range(columns):
            matrix1[i][j] = float(input(f"Enter element at position ({i+1}, {j+1}): "))

    print("\nEnter the elements of the second matrix:")
    matrix2 = np.zeros((rows, columns))
    for i in range(rows):
        for j in range(columns):
            matrix2[i][j] = float(input(f"Enter element at position ({i+1}, {j+1}): "))

    result = matrix1 + matrix2
    print("\nThe sum of the two matrices is:")
    print(result)

def multiply_matrices():
    rows1 = int(input("Enter the number of rows for matrix 1: "))
    columns1 = int(input("Enter the number of columns for matrix 1: "))
    rows2 = int(input("Enter the number of rows for matrix 2: "))
    columns2 = int(input("Enter the number of columns for matrix 2: "))

    if columns1 != rows2:
        print("Error: Number of columns in matrix 1 should be equal to the number of rows in matrix 2.")
        return

    print("\nEnter the elements of the first matrix:")
    matrix1 = np.zeros((rows1, columns1))
    for i in range(rows1):
        for j in range(columns1):
            matrix1[i][j] = float(input(f"Enter element at position ({i+1}, {j+1}): "))

    print("\nEnter the elements of the second matrix:")
    matrix2 = np.zeros((rows2, columns2))
    for i in range(rows2):
        for j in range(columns2):
            matrix2[i][j] = float(input(f"Enter element at position ({i+1}, {j+1}): "))

    result = np.dot(matrix1, matrix2)
    print("\nThe product of the two matrices is:")
    print(result)

def transpose_matrix():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    print("\nEnter the elements of the matrix:")
    matrix = np.zeros((rows, columns))
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = float(input(f"Enter element at position ({i+1}, {j+1}): "))

    result = np.transpose(matrix)
    print("\nThe transpose of the matrix is:")
    print(result)

# Main program
while True:
    print("\nMatrix Operations Menu")
    print("1. Add two matrices")
    print("2. Multiply two matrices")
    print("3. Transpose a matrix")
    print("4. Quit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        add_matrices()
    elif choice == "2":
        multiply_matrices()
    elif choice == "3":
        transpose_matrix()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
