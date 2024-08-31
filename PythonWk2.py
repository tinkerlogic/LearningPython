# Example of if-elif-else statements

number = int(input("Enter a number: "))

# If the number is positive
if number > 0:
    print("The number is positive.")

# If the number is zero
elif number == 0:
    print("The number is zero.")

# If the number is negative
else:
    print("The number is negative.")



# Example of switch-case using a dictionary

def switch_case_example(choice):
    switcher = {
        1: "Case 1 selected.",
        2: "Case 2 selected.",
        3: "Case 3 selected.",
    }
    
    # Get the case action from the dictionary
    return switcher.get(choice, "Invalid choice.")

# Test the switch-case functionality
choice = int(input("Enter a choice (1, 2, or 3): "))
print(switch_case_example(choice))



# Example of break, continue, and pass in loops

for i in range(1, 11):
    if i == 5:
        break  # Exit the loop when i is 5
    elif i == 3:
        continue  # Skip the rest of the loop when i is 3
    elif i == 8:
        pass  # Pass does nothing; it's a placeholder
    print(i)



# Example of a while loop to print numbers from 1 to 5

count = 1

while count <= 5:
    print(count)
    count += 1  # Increment the counter



# Example of a simple function that returns a value

def add_numbers(a, b):
    result = a + b
    return result  # Return the result to the caller

# Test the function
sum_result = add_numbers(5, 3)
print("Sum:", sum_result)



# Example of local and global variables

x = 10  # Global variable

def local_example():
    x = 5  # Local variable (different from the global x)
    print("Inside function, local x =", x)

def global_example():
    global x  # Use the global keyword to modify the global variable
    x = 20
    print("Inside function, modified global x =", x)

# Test the functions
local_example()
print("Outside function, global x =", x)  # The global variable is unchanged

global_example()
print("Outside function, modified global x =", x)  # The global variable is modified
