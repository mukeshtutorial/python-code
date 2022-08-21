# Give the number of units consumed as static input and store it in a variable.
numbOfUnits = 176
# Using If Else statements we check the conditions and calculate the cost per unit.
# If the number of units used equals 100, the cost per unit is Rs 3.46.
if numbOfUnits <= 100:
    totalbill = numbOfUnits * 3.46
# If the number of units used is greater than 101 and less than 300,
# the cost per unit is Rs 7.43.
elif numbOfUnits >= 101 and numbOfUnits <= 300:
    totalbill = 346 + ((numbOfUnits - 100) * 7.43)
# If you consume more than 301 units and less than 500 units,
# the cost per unit is Rs 10.32.
elif numbOfUnits >= 301 and numbOfUnits <= 500:
    totalbill = 346 + 1486 + ((numbOfUnits - 300) * 10.32)
# If the number of units consumed exceeds 501,
# the cost per unit is Rs 11.71.
else:
    totalbill = 346 + 1486 + 2064 + ((numbOfUnits - 500) * 11.71)
# After Calculating cost per unit we multiply the number of units by 1.45 and
# add it to the bill(Adding monthly line rent to the bill)
totalbill = totalbill + (numbOfUnits*1.45)
# We add Rs 100 to the bill as additional fixed meter rent.
totalbill = totalbill + 100
# We multiply the present bill amount by 0.16 (Adding the tax) and add this bill to the past bill.
totalbill = totalbill + (totalbill*0.16)
# Print the Final Electricity Bill.
print("The Electricity bill for the units", numbOfUnits, '=', totalbill)