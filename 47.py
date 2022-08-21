# Give the height in centimeters as static input.
heightcm = 165
# Convert the given height in centimeters to feet by multiplying it with 0.0328
# and store it in a variable.
heightfeet = 0.0328*heightcm
# Convert the given height in centimeters to inches by multiplying it with 0.0.394
# and store it in a variable.
heightinches = 0.394*heightcm
# Print the height in feet and inches.
print("The given height", heightcm, 'cm',
      'in inches = ', round(heightinches, 2), 'inches')
print("The given height", heightcm, 'cm',
      'in feet = ', round(heightfeet, 2), 'feet')