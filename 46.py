# function which accepts the gray code  and returns the binary code  of the gray code
def grayToBin(grayCde):
   # Converting the given gray code to integer
    graynum = int(grayCde, 2)
   # Taking a temporary variable which stores the the gray code integer number
    tempnum = graynum
    # using while loop
    while tempnum != 0:
        tempnum >>= 1
        graynum ^= tempnum

        # bin(n) returns n's binary representation with the prefix '0b' removed
        # the slice operation removes the prefix.
    return bin(graynum)[2:]


# given gray code as static
graycode = "1001000010"
# passing this graycode to grayToBin function
resultbin = grayToBin(graycode)
print('The Binary string of the given gray code=', graycode, 'is', resultbin)