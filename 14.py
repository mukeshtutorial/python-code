selection = input("Press (1) for Cinema, (2) for Theater : ")
student = input("Are you student(Y/N) : ")
price = 0
# non-discounted fee calculation
if selection == '1':
    price = 10  # cinema
elif selection == '2':
    price = 5  # theatre
# student discount
if student == 'Y' or student == 'y':
    price = price / 2  # %50
print(" The fee you have to pay :{}".format(price))
