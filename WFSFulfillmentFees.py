#Author: Corey Johnson
#Date: 2021-08-26
#Title: Amazon Fulfillment Fee Calculator

import math

print("\nDimensions in Inches and Weights in Pounds\n")
length = float(input("Length: "))
width = float(input("Width: "))
height = float(input("Height: "))
weight = float(input("Weight: "))



dimWeight = (length*width*height)/139

if dimWeight > weight:
    weight = dimWeight

weight = weight + 0.25

if weight <= 1:
    print("Fulfillment Fee is $3.45")
elif weight <= 2:
    print("Fulfillment Fee is $4.95")
elif weight <= 3:
    print("Fulfillment Fee is $5.45")
elif weight > 3:
    fulfillmentFee = 5.75
    if 4 < weight <= 20:
        weight = math.ceil(weight)
        additionalFee = (weight - 4)*0.4
        fulfillmentFee = fulfillmentFee + additionalFee
    elif weight > 20:
        weight = math.ceil(weight)
        additionalFee = ((weight-4) * 0.4) + 3
        fulfillmentFee = fulfillmentFee + additionalFee
    print(f"Fulfillment Fee is ${fulfillmentFee}")

