# Take a variable to say numb and initialize its value with 1000000007(10^9+7).
numb = 1000000007

# Create a function to say exponentl_squaring() which takes the given two base and
# exponential values as the arguments and returns the value of the power of base and
# exponent modular 10^9+7.


def exponentl_squaring(gvn_baseval, gvn_exponentlval):
  # Inside the function, take a variable say p, and initialize its value to 1.
    p = 1
    # Loop until the given exponential value is greater than 0 using the while loop.
    while(gvn_exponentlval > 0):
           # Check if the given exponential value is odd using the if conditional statement.
        if (gvn_exponentlval % 2 != 0):
            # If it is true, multiply p with the given base value and store it in another
            # variable.
            k = p * gvn_baseval
            # Calculate the value of the above result modulus numb(10^9+7) and store it in the
            # same variable p.
            p = k % numb
      # Multiply the given base value with itself and apply the modulus operator with
      # 10^9+7(numb).
      # Store it in the same variable given base value.
        gvn_baseval = (gvn_baseval * gvn_baseval) % numb
        # Divide the given exponential value by 2 and convert it to an integer using the
        # int() function.
        # Store it in the same variable given exponential value.
        gvn_exponentlval = int(gvn_exponentlval / 2)
   # Return the value of p modulus 10^9+7.
    return p % numb


# Give the base value as static input and store it in a variable.
gvn_baseval = 5
# Give the exponential value as static input and store it in another variable.
gvn_exponentlval = 3
# Pass the given base and exponential values as the arguments to the exponentl_squaring()
# function and store it in a variable.
rslt = exponentl_squaring(gvn_baseval, gvn_exponentlval)
# Print the value of the power of base and exponent modular 10^9+7.
print("The value of the power of base and exponent modular 10^9+7 = ", rslt)