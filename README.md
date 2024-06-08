# Python Term 1 Week 6 Saturday Class

# If-Else Practice Acitivity

## Building a calculator
Build a calculator that takes 3 inputs from the user:
2 inputs as numbers(floats) for operation and 3rd input to decide which operation they want to perform

# Lists
Composite Data Type, meaning multiple data types can be stored in one variable. 
Each piece is called an element.

# Loops

Like Post Malone describes, "Run away, but we're running in circles"
Used to repeat a block of code multiple times until a certain condition is met.

DRY Coding Principle: Don't Repeat Yourself

Examples: Counting coins in your piggy bank

'If' condition would decide whether or not to run the intended block. Whereas,
Loops would decide how many times the user wants to run the intended block

# While loop
While the condition is met, keep executing the intended block. If not met, skip the block. Ctrl + C to escape

Things to consider:
    - Program can enter the loop
    - Program can exit the loop

## Range
Predifined method (e.g. print - has a specific purpose)
A pre-defined function that generates a sequence of numbers.

Useful: Loops for iterating a specific number of times over a sequence of numbers.

range(1, 2, 3) (start, stop, step) if you don't define 1, it will automatically be 0, if you don't define step, it will automatically be 1
range(1, 5, 2)

doesn't work with floats

## For Loop
For each item in a sequence, execute the intended statements.

for variable_name in sequence:
    statements

    [] - for lists
    {} - for printing

## Practice Exapmle 1-
Finding the sum of the first ten numbers (1, 2, ...10)

Important to initialise variables if you're making changes to it

## Practice Example 2 
Find the largest number in the list
list = [3, 41, 12, 9, 74, 15]

# Loop control statements
Used to control the flow of the loop, terminate the loop early if you want or skip over some iteration

## Break statement
Terminates loop immediately, moves to the next statement after the loop.

## Continue statement
Skip the rest of the code inside the loop for the current iteration and moves to the next iteration

# Nested Loops
A loop inside another loop! Like inception.
Useful for running over multi-dimensional structures like the MATRIX or a list of lists.

## Practice Example 1
Print a right-angled triangle pattern of stars. (stars = 5)
*
**
***
****
*****

## Practice Example 2
Count the occurance of a letter in a list

# enumerate() function
Used to access the index and the value of the elements of the list.
Use two variables in for loop.

INDEX always starts from 0