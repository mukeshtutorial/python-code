# Give the octal number as static input and store it in a variable.
gvn_octl_numb = 15
# Take a variable say 'a 'and initialize its value with 0.
a = 0
# Take another variable say deciml_numb and initialize its value with 0.
deciml_numb = 0
# Loop till the given octal number is not equal to zero using the while loop.
print("The Decimal value of the given Octal number {", gvn_octl_numb, "} is: ")
while(gvn_octl_numb != 0):
  # Inside the loop, calculate the value of the given octal number modulus 10
  # (to get the last digit) and store it in a variable say 'b'.
    b = (gvn_octl_numb % 10)
# Calculate the value of 8 raised to the power 'a' using the pow() function and multiply
# it with the above-obtained 'b'.
# Store it in another variable 'c'.
    c = b*pow(8, a)
  # Add the above variable 'c' with the deciml_numb and store it in the same variable
  # deciml_numb.
    deciml_numb = deciml_numb+c
  # Increment the value a by 1 and store it in the same variable 'a'.
    a += 1
# Divide the given octal number by 10 (to remove the last digit) and store it in the
# same variable gvn_octl_numb.
    gvn_octl_numb = gvn_octl_numb // 10
# Print the deciml_num to get the decimal value of the given Octal number.
print(deciml_numb)