def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

def compare_files(file1_path, file2_path):
    file1_lines = count_lines(file1_path)
    file2_lines = count_lines(file2_path)

    print(f"Total number of lines in {file1_path}: {file1_lines}")
    print(f"Total number of lines in {file2_path}: {file2_lines}")

# Example usage
file1_path = 'file1.txt'
file2_path = 'file2.txt'

compare_files(file1_path, file2_path)
