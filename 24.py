# Give the income as static input and store it in a variable.
givenincome = 670000
# We will use if and else statements here to complete our income tax calculating conditions,
# which are as follows,
# If your income is less than or equivalent to Rs. 2,50,000,the taxAmount=0.
if givenincome <= 250000:
    taxAmount = 0
# If your income is less than or equal to Rs. 5,00,000,
# the taxAmount will be 5% of your total income over Rs. 2,50,000.
elif givenincome <= 500000:
    taxAmount = (givenincome - 250000) * 0.05
# If your income is less than or equal to Rs. 7,50,000,
# your taxAmount rate will be 10% of your total income
# beyond Rs. 5,00,000, with an additional cost of Rs. 12,500.
elif givenincome <= 750000:
    taxAmount = (givenincome - 500000) * 0.10 + 12500
# If your income is less than or equivalent to Rs. 10,00,000,
# your taxAmount rate will be 15% of your total income over Rs. 7,50,000,
# with an additional fee of Rs. 37,500.
elif givenincome <= 1000000:
    taxAmount = (givenincome - 750000) * 0.15 + 37500
# If your income is less than or equal to Rs. 12,50,000,
# your taxAmount rate will be 20% of your total income beyond Rs. 10,00,000,
# with an additional fee of Rs. 75,000.
elif givenincome <= 1250000:
    taxAmount = (givenincome - 1000000) * 0.20 + 75000
# If your income is less than or equal to Rs. 15,00,000,
# your taxAmount rate will be 25% of your total income beyond Rs. 12,50,000,
# with an additional cost of Rs. 1,25,000.
elif givenincome <= 1500000:
    taxAmount = (givenincome - 1250000) * 0.25 + 125000
# If your income exceeds Rs. 15,00,000,
# you will be taxed at 30% of the excess, with an additional fee of Rs. 1,87,500.
else:
    taxAmount = (givenincome - 1500000) * 0.30 + 187500
# Print the Tax.
print('The tax for the income ', givenincome, '=', taxAmount)