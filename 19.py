# Give the number as static input and store it in a variable.
num = 5
# Take a variable, initialize it with the value '1', and store it in another
# variable say 'factorial'.
factorl = 1
# Loop from 1 to the given number using the for loop.
for i in range(1, num+1):
 # Calculate the factorial of a given number by multiplying the above variable "factorial"
    # with the iterator and store it in the same variable 'factorial'.
    factorl = factorl*i
# Take a variable, initialize it with the value '0', and store it in another variable
# say 'c'.
c = 0
print("The divisors of factorial of a given number{", num, "}:")
# Loop from 1 to the above obtained factorial number using the for loop.
for i in range(1, factorl+1):
  # Check if the value of factorial modulus iterator value is equal to 0 using
    # the if conditional statement.
    if(factorl % i == 0):
     # If the statement is true, print the iterator value and increment the value of 'c'.
        # Store it in the same variable 'c'.
        print(i, end=" ")
        c = c+1
print()
# Print the count of divisors of factorial of a given number.
print("The count of divisors of factorial of a given number{", num, "}=", c)