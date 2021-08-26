#Author: Corey Johnson
#Date: 2021-08-26
#Title: Amazon Fulfillment Fee Calculator

import math, numpy

print("\nDimensions in Inches and Weights in Pounds\n")
length = float(input("Longest: "))
width = float(input("Median: "))
height = float(input("Shortest: "))
unitWeight = float(input("Weight: "))
girth = (width + height) * 2
dimWeight = (length * width * height) / 139


"""Calculate Product Size Tier"""
if length <= 15 and width <= 12 and height <= 0.75 and unitWeight <= 1:
    sizeTier = "Small standard-size"
    print(sizeTier)
elif length <= 18 and width <= 14 and height <= 8 and unitWeight <= 20:
    sizeTier = "Large standard-size"
    print(sizeTier)
elif (length > 18 or width > 14 or height > 8) and (length <= 60 and width <= 30 and unitWeight <= 70 and (length + girth) <= 130):
    sizeTier = "Small oversize"
    print(sizeTier)
elif (length > 60 or width > 30 or unitWeight > 70) and (length <= 108 and unitWeight <= 150 and (length + girth) <= 130):
    sizeTier = "Medium oversize"
    print(sizeTier)
elif (length > 60 or width > 30 or unitWeight > 70) and (length <= 108 and unitWeight <= 150 and (length + girth) <= 165):
    sizeTier = "Large oversize"
    print(sizeTier)
elif length > 108 or (unitWeight or dimWeight) > 150 or (length + girth) > 165:
    sizeTier = "Special Oversize"
    print(sizeTier)
else:
    print("\n------------------------------------\n" +
          "Error - Check Dimensions and Weight \n" +
          "------------------------------------\n")


"""Calculating outbound Shipping Weight"""
if sizeTier == "Small standard-size":
    if unitWeight <= 0.75:
        shippingWeight = math.ceil(unitWeight * 16) / 16
    elif 0.75 < unitWeight <= 1:
        if dimWeight > unitWeight:
            shippingWeight = math.ceil(dimWeight * 16) / 16
        else:
            shippingWeight = math.ceil(unitWeight * 16) / 16
elif sizeTier == "Large standard-size":
    if unitWeight <= 0.75:
        shippingWeight = math.ceil(unitWeight * 16) / 16
    elif 0.75 < unitWeight < 1:
        if dimWeight > unitWeight:
            shippingWeight = math.ceil(dimWeight * 16) / 16
        else:
            shippingWeight = math.ceil(unitWeight * 16) / 16
    elif unitWeight >= 1:
        if dimWeight > unitWeight:
            shippingWeight = math.ceil(dimWeight)
        else:
            shippingWeight = math.ceil(unitWeight)
elif "oversize" in sizeTier:
    if dimWeight > unitWeight:
        shippingWeight = math.ceil(dimWeight)
    else:
        shippingWeight = math.ceil(unitWeight)
elif sizeTier == "Special Oversize":
    shippingWeight = math.ceil(unitWeight)

print(f"Shipping Weight: {shippingWeight}")


"""Calculate Fulfillment Fee"""
if sizeTier == "Small standard-size":
    if shippingWeight * 16 <= 6:
        fulfillFee = 2.70
        print(f"Fulfillment Fee is ${fulfillFee}")
    elif 6 < shippingWeight * 16 <= 12:
        fulfillFee = 2.84
        print(f"Fulfillment Fee is ${fulfillFee}")
    elif 12 < shippingWeight * 16 <= 16:
        fulfillFee = 3.32
        print(f"Fulfillment Fee is ${fulfillFee}")
elif sizeTier == "Large standard-size":
    if shippingWeight * 16 <= 6:
        fulfillFee = 3.47
        print(f"Fulfillment Fee is ${fulfillFee}")
    elif 6 < shippingWeight * 16 <= 12:
        fulfillFee = 3.64
        print(f"Fulfillment Fee is ${fulfillFee}")
    elif 12 < shippingWeight * 16 <= 16:
        fulfillFee = 4.25
        print(f"Fulfillment Fee is ${fulfillFee}")
    elif 1 < shippingWeight <= 2:
        fulfillFee = 4.95
        print(f"Fulfillment Fee is ${fulfillFee}")
    elif 2 < shippingWeight <= 3:
        fulfillFee = 5.68
        print(f"Fulfillment Fee is ${fulfillFee}")
    elif shippingWeight > 3:
        weightFee = 0.3 * math.ceil(shippingWeight-3)
        fulfillFee = round(5.68 + weightFee, 2)
        print(f"Fulfillment Fee is ${fulfillFee}")
elif sizeTier == "Small oversize":
    if shippingWeight <= 70:
        weightFee = 0.38 * math.ceil(shippingWeight-1)
        fulfillFee = round(8.66 + weightFee, 2)
        print(f"Fulfillment Fee is ${fulfillFee}")
elif sizeTier == "Medium oversize":
    if shippingWeight <= 150:
        weightFee = 0.39 * math.ceil(shippingWeight-1)
        fulfillFee = round(11.37 + weightFee, 2)
        print(f"Fulfillment Fee is ${fulfillFee}")
elif sizeTier == "Large oversize":
    if shippingWeight <= 90:
        fulfillFee = round(76.57, 2)
        print(f"Fulfillment Fee is ${fulfillFee}")
    elif 90 < shippingWeight <= 150:
        weightFee = 0.79 * math.ceil(shippingWeight-90)
        fulfillFee = round(76.57 + weightFee, 2)
        print(f"Fulfillment Fee is ${fulfillFee}")
elif sizeTier == "Special oversize":
    if shippingWeight <= 90:
        fulfillFee = round(138.11, 2)
        print(f"Fulfillment Fee is ${fulfillFee}")
    elif 90 < shippingWeight <= 150:
        weightFee = 0.79 * math.ceil(shippingWeight - 90)
        fulfillFee = round(138.11 + weightFee, 2)
        print(f"Fulfillment Fee is ${fulfillFee}")


