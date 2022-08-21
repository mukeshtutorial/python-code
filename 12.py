# Give the original price as static input and store it in a variable.
gvn_Orignl_amt = 520
# Give the net price as static input and store it in another variable.
gvn_Net_amt = 650
# Calculate the GST amount by using the above given formula and store it in
# another variable.
GST_amnt = gvn_Net_amt - gvn_Orignl_amt
# Calculate the given GST percentage by using the above given formula and
# store it in another variable.
gvn_GST_percnt = ((GST_amnt * 100) / gvn_Orignl_amt)
# Print the given GST value for the above given original and net prices.
print("The GST percent for the above given input net and original prices = ",
      gvn_GST_percnt, end='')
print("%")