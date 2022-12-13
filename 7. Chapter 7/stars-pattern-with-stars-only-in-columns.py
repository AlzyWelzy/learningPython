# Get the size of the square from the user
size = int(input("Enter the size of the square: "))

# Use a nested loop to iterate over the rows and columns
for i in range(size):
    for j in range(size):
        # Print a star if the current position is on the edge of the square
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
