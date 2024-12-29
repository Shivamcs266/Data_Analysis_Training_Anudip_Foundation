#find the square

list[0,1,4,9,16]
for i in range(5):
    print(i**2)

L = []
for i in range(5):
    L.append(i**2)
print(L)


# Practice Question - 01.
# Print the list of odd & even number seperatly.

L = [7, 6, 9, 2, 5, 4, 12, 18, 20, 25]

# Initialize empty lists for odd and even numbers
odd_numbers = []
even_numbers = []

# Loop through the list
for num in L:
    if num % 2 == 0:
        even_numbers.append(num)  # Append to even numbers
    else:
        odd_numbers.append(num)   # Append to odd numbers

# Print the results
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)




print("--------------------------------------")




L = [3, 4, 6, 8, 9, 12, 53, 32, 134, 64, 65, 23, 96, 87, 42, 53, 40, 61, 39]

for i in L:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("Odd numbers:", odd_numbers)
print("even numbers:", even_numbers)




print("========================================")



# Practice Question - 02.
# Print the list of positive and negative number.
L = [1, -2, 7, -12, 5, -9, -5, 12, -21, 34, -53, 32, 54, 23, 64, -48]

Positive_numbers = []
Negative_numbers = []

for i in L:
    if i >= 0:
        Positive_numbers.append(i)
    else:
        Negative_numbers.append(i)

print("Positive numbers:", Positive_numbers)
print("Negative numbers:", Negative_numbers)




print("-----------------------------------------------------")




#Break statement --- "When break is executed, the loop stops and the program continues with the next statement after the loop."

for i in range(5):
    if i == 4:
        break
    print(i)




#Continue statement--- "Used to skip the rest of the code in the current iteration and jump to the next iteration of the loop."

for i in range(10):
    if i == 5:
        continue
    print(i)



# # Example 2.
for i in range(10):
    if i % 2 == 0:
        continue  # Skip the current iteration if i is even
    print(i)




#User Defined Function --- set of code use to perform particular task.

#Syntax.
def function_name(parameters):
    # Function body
    return value  # Optional

    

#Call the function
#function_name(arguments)



#Example 1: Function Without Parameters
def greet():
    print("Hello, welcome to Python programming!")

greet()




#Example 2,
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")

# Calling the function with an argument
greet_user("Shivam")




#Example 3.
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print("The sum is:", result)




# Example 4: Function With Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}! Have a great day.")

# Calling the function with and without arguments
greet("Shivam Sharma")  # Passes a value
greet()         # Uses the default value




# Example 5: Function with Multiple Parameters
def calculate_area(length, width):
    return length * width

# Calling the function with arguments
area = calculate_area(10, 5)
print("The area is:", area)




print("-----------------------------------------------")




#___Swapping___________



# Example: Swap two numbers
a = 5
b = 10

# Swapping
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)



#  2.Using a Temporary Variable
a = 5
b = 10

# Swapping using a temporary variable
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)



# 3. Using Arithmetic Operations
a = 5
b = 10

# Swapping using addition and subtraction
a = a + b  # a becomes 15
b = a - b  # b becomes 5
a = a - b  # a becomes 10

print("After swapping:")
print("a =", a)
print("b =", b)
