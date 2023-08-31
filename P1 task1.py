rows = int(input("Enter number of rows: "))
k="#"
if rows < 1 or rows > 8:
    print("Invalid")
else:
    for i in range(rows):
        print(" " * (rows - i - 1) + k * (i + 1), end="")
        print("  ", end="")
        print(k * (i + 1))