# given number in decimal number system
decimal_Number = 1028
# converting the given decimal_number to binary_number system
# we use bin() function to convert given decimal_number to binary_number system
binValue = bin(decimal_Number)
# converting the given decimal_number to octal_number system
# we use bin() function to convert given decimal_number to binary_number system
octalValue = oct(decimal_Number)
# converting the given decimal_number to hexadecimal_number system
# we use bin() function to convert given decimal_number to binary_number system
hexValue = hex(decimal_Number)
# printing the values after the conversion of bases that is
# decimal to binary,octal,hexadecimal
print("Printing the values after the conversion of bases"
      " that is decimal to binary,octal,hexadecimal:")
# printing the binary converted value
print("The binary value of the given decimal number",
      decimal_Number, "=", binValue)
# printing the octal converted value
print("The octal value of the given decimal number",
      decimal_Number, "=", octalValue)
# printing the hexadecimal converted value
print("The hexadecimal value of the given decimal number",
      decimal_Number, "=", hexValue)