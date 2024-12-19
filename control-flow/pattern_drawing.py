# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate that the input is a positive integer
while size <= 0:
    print("Invalid input. Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through rows
while row < size:
# Use a for loop to print the asterisks for each row
        for _ in range(size):
            print("*", end="")
        # Print a newline character to move to the next row
        print()
        # Increment the row counter
        row += 1