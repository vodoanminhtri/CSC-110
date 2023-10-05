# Minh Tri Doan Vo
# Lab 2 - Math Conversion



#input from user in ft
userHeight =    float(input("Enter your height (ft): "))

import math
# round down the feet
heightFt =      math.floor(userHeight)

# use the left over float to calculate the inches
heightIn =      (userHeight - heightFt)*12

print("Your height is", heightFt, "feet", format(heightIn,".1f"), "inches.")
