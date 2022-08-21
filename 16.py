# Give the string as static input and store it in a variable.
gvn_str = "hello this is btechgeeks"
# Take an empty list say "ASCII_vals" and store it in another variable.
ASCII_vals = []
# Loop the above-given string using the for loop.
for itr in gvn_str:
  # Calculate the ASCII value of the iterator using the ord() function
  # and store it in another variable.
    a = ord(itr)
# Append the above obtained ASCII value of the iterator to the above-initialized
# list "ASCII_vals" using the append() method.
    ASCII_vals.append(a)
  # Print the given string after converting each character to an ASCII value.
print("The given string after convering each character to an ASCII value :", ASCII_vals)