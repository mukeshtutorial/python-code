# Create a function to say y_mod2powx which takes the given two numbers y and x as
# the arguments and returns the value of given y modulus 2 raised to the power x.


def y_mod2powx(gvn_yval, x):
   # Calculate the value of 2 raised to the power x using the pow() function and store it
   # in a variable.
    p = pow(2, gvn_xval)
    # Calculate the value of the given y value modulus the above result and store it in
    # another variable rslt.
    rslt = gvn_yval % p
    # Return the above result value rslt.
    return (rslt)


# Give the number x as static input and store it in a variable.
gvn_xval = 5
# Give the number y as static input and store it in another variable.
gvn_yval = 9
# Pass the given two numbers y and x as the arguments to the y_mod2powx function.
# Print the value of given y modulus 2 raised to the power x.
print("The result of given y modulus 2 raised to the power x =",
      y_mod2powx(gvn_yval, gvn_xval))