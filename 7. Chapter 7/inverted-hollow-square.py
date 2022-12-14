# define the size of the square
size = int(input("Enter a positive number: "))

# iterate over the rows
for i in range(size):
    # iterate over the columns
    for j in range(size):
        # print a star for the first and last column, and the first and last row
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print('*', end='')
        # print a dash for all other positions
        else:
            print('-', end='')
    # move to the next line after each row is complete
    print()
