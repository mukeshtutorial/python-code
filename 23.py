# Create a function to say modular_MultInverse which takes the given first and second
# numbers as the arguments and returns the modular multiplicative inverse of
# ‘first number’ under modulo ‘second number’.


def modular_MultInverse(fst_numb, secnd_numb):
  # Calculate the value of the given first number modulus second number and store it in the
  # same variable first number.
    fst_numb = fst_numb % secnd_numb
    # Loop from 1 to the given second number using the for loop.
    for itror in range(1, secnd_numb):
        # Multiply the given first number with the iterator value and store it in
        # another variable.
        mul = (fst_numb * itror)
      # Check if the above result modulus second number is equal to 1 using the if conditional
      # statement.
        if (mul % secnd_numb == 1):
          # If it is true, then return the iterator value.
            return itror
    # Return 1.
    return 1


# Give the first number as static input and store it in a variable.
fst_numb = 10
# Give the second number as static input and store it in another variable.
secnd_numb = 17
# Pass the given first and second numbers as the arguments to the modular_MultInverse
# function.
# Print the modular multiplicative inverse of ‘first number’ under modulo ‘second number'.
print("The modular multiplicative inverse of given first number under modulo second number = ",
      modular_MultInverse(fst_numb, secnd_numb))