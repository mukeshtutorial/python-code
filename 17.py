# Give the decimal number as static input and store it in a variable.
deciml_num = 30
# Take a variable say 'k' and initialize its value with 0.
k = 0
# Take a list of length 50 and initialize all the values to zero using the multiplication operator. 
# Store it in another variable.
Hexa_deciml = ['0']*50

print(
    "The Hexadecimal value of the given decimal number {", deciml_num, "} is: ")
# Loop till the given decimal number is not equal to zero using the while loop.
while deciml_num != 0:
 # Inside the loop, calculate the value of decimal number modulus 16 to get the remainder
    # and store it in another variable.
    remndr = deciml_num % 16
  # Check if the above remainder value is less than 10 using the if conditional statement.
    if remndr < 10:
       # If the statement is true, then get the character with the ASCII value remainder+48 using
        # the if conditional statement and store it in a variable
        chrvalue = chr(remndr+48)
  # Initialize the hexadecimal list at the index 'k' with the above-calculated character.
        Hexa_deciml[k] = chrvalue
    # Increment the value of k by 1 and store it in the same variable k.
        k += 1

    else:
      # Else if the statement is false, get the character with the ASCII value remainder+55.
        # Store it in another variable.
        Hexa_deciml[k] = chr(remndr+55)
  # Increment the value of k by 1 and store it in the same variable k.
        k += 1
  # Divide the given decimal number by 16 and store it in the same variable.
    deciml_num //= 16
# Loop in decreasing order from k-1 to 0 with the stepsize of -1 using the for loop.
for itr in range(k-1, -1, -1):
  # Print the element present at the iterator value of the hexadecimal list to get the
    # hexadecimal value of the given decimal number.
    print(Hexa_deciml[itr], end="")