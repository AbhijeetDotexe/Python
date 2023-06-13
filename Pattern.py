def print_numberpattern(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(i, 0, -1):
            print(j, end="")
        for k in range(2, i + 1):
            print(k, end="")
        print()

def print_starpattern():
    for i in range(1, 4):
        for j in range(3 - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()
    for i in range(2, 0, -1):
        for j in range(3 - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()

print_numberpattern(4)
print_starpattern()
