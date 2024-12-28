 #_________LOOP_______________

#A loop in Python is a programming construct that allows you to execute a block of code repeatedly. 
#Python provides two main types of loops :

#FOR LOOP --- The for loop iterates over a sequence (like a list, tuple, string, or range) and executes the block of code for each element in the sequence.

#Examples.
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range to iterate over numbers
for i in range(5):  # 0 to 4
    print(i)


for x in range (5):
    print(x)
    


names=["Shivam","Astitwa","Rahul"]
for x in names:
    print(x)



for a in "Shivam kumar Sharma":
    print(a)


 
for i in "Shivam Sharma raghav":
    print(i)
else:
    print("its over")



print("===================================")

#WHILE LOOP -- The while loop executes a block of code as long as a specified condition is True.


# Using while to count
count = 0
while count < 5:
    print(count)
    count += 1  # Increment to avoid infinite loop

print("===================================")

#Controlling Loops--You can control the flow of loops using:

#break: Exit the loop immediately.

#example.

for num in range(10):
    if num == 5:
        break
    print(num)


print("===================================")
#continue: Skip the current iteration and move to the next one.

for num in range(5):
    if num == 2:
        continue
    print(num)


