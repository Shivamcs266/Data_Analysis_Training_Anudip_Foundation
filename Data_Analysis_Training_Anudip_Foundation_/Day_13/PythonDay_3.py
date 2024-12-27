#______Functions_________

# In Python, a function is a block of reusable code that performs a specific task. Functions help organize your code into smaller, modular, and manageable sections. Python has two types of functions: built-in functions (like print(), len(), etc.) and user-defined functions (created by the programmer).

# 1. Built in function  (there are 68 types of built in function)
# 2. Python Recursive function
# 3. Python Lambda function
# 4. User defined function


# INPUT

x=input("Af0440955")
print(x)

y=input("Shivam Sharma")
print(y)


#_____Average________________

a=5
b=4
c=6
d=2
e=8

sum=(a+b+c+d+e)
print(sum)

avg=sum/5
print(avg)

percentage = sum/500*100
print(percentage)



#Example -
#  5 input from the user-

Math = input (70)
English = input (60)
Hindi = input (80)
Science = input (65)
Social_Science= input (55)


avg=Math+English+Hindi+Science+Social_Science/5
print(avg)
   
print("=========================================")

#_________CONTROL FLOW STATEMENTS______

#_IF

# Ex.1

i=20
if(i>=15):
    print("i is greater than 15")

#Ex.2.1
# if attendence >=80 = Green mark
# if attendence >=50 but <80 = Yellow mark
# if attendence 0 to 50 = Red mark

a=(90)      #Enter your attedence
if a>=80:
    print("Green")

if a>=50 and a<80:
    print("Yellow")

if a>=0 and a<50:
    print("Red")

# Ex.2.2
a=(55)      #Enter your attedence
if a>=80:
    print("Green")

if a>=50 and a<80:
    print("Yellow")

if a>=0 and a<50:
    print("Red")

print("------------------------------------------")

#_if else 

# Ex 1.1
age=22
if age>=18:
    print("You are eligible")
else:
    print("You cannot vote")

# Ex 1.2
age=16
if age>=18:
    print("You are eligible")
else:
    print("You cannot vote")

print("--------------------------------------")

#_if-elif-else

#Ex.1
# score >=90 = A
# score 70-89 = B
# score 50-69 = C
# score 30-49 = D 
# others = E

a=(48)
if a>=90:
    print("A grade")

elif a>=70 and a<90:
    print("B grade")

elif a>=50 and a<70:
    print("C grade")

elif a>=30 and a<50:
    print("D grade")

else:
    print("Wrong input")