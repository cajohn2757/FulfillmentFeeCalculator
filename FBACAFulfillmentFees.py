#Author: Corey Johnson
#Date: 2021-08-26
#Title: Amazon Fulfillment Fee Calculator

import math

print("\nDimensions in Centimetres and Weights in Kilograms\n")
length = float(input("Longest: "))
width = float(input("Median: "))
height = float(input("Shortest: "))
weight = float(input("Weight: "))


"""Calculate Product Size Tier"""
if length <= 38 and width <= 27 and height <= 2 and weight <= 0.5:
    sizeTier = "Envelope"
    print(sizeTier)
elif (length > 38 or width > 27 or height > 2) and (length <= 45 and width <= 35 and height <= 20 and weight <= 9):
    sizeTier = "Standard-size"
    print(sizeTier)
elif length > 270 or (length + (2*width) + (2*height)) > 419 or weight > 69:
    sizeTier = "Oversize - Special Handling"
    print(sizeTier)
elif length > 45 or width > 35 or height > 20 or 9 < weight <= 69:
    sizeTier = "Oversize"
    print(sizeTier)
else:
    print("\n------------------------------------\n" +
          "Error - Check Dimensions and Weight \n" +
          "------------------------------------\n")


"""Calculate Shipping Weight"""
dimWeight = (length*width*height)/5000

if sizeTier == "Envelope":
    if dimWeight > weight:
        shippingWeight = dimWeight
    else:
        shippingWeight = weight

    shippingWeight = math.ceil((shippingWeight + 0.025) * 10) / 10
    print(f"Shipping Weight: {shippingWeight}")
elif sizeTier == "Standard-size":
    if dimWeight > weight:
        shippingWeight = dimWeight
    else:
        shippingWeight = weight

    if shippingWeight < 0.25:
        shippingWeight = math.ceil((shippingWeight + 0.04) * 4) / 4
    elif 0.25 <= shippingWeight < 0.5:
        shippingWeight = math.ceil((shippingWeight + 0.06) * 4) / 4
    elif shippingWeight >= 0.5:
        shippingWeight = math.ceil((shippingWeight + 0.125) * 4) / 4
    print(f"Shipping Weight: {shippingWeight}")
elif sizeTier == "Oversize" or "Oversize - Special Handling":
    if dimWeight > weight:
        shippingWeight = dimWeight
    else:
        shippingWeight = weight

    shippingWeight = math.ceil((shippingWeight + 0.5) * 2) / 2
    print(f"Shipping Weight: {shippingWeight}")


"""Calculate Fulfillment Fee"""
if sizeTier == "Standard-size":
    if shippingWeight <= 0.250:
        fulfillmentFee = 5.44
        print(f"Fulfillment Fee is CAD ${fulfillmentFee}")
    elif shippingWeight <= 0.500:
        fulfillmentFee = 5.57
        print(f"Fulfillment Fee is CAD ${fulfillmentFee}")
    elif shippingWeight <= 1.000:
        fulfillmentFee = 6.40
        print(f"Fulfillment Fee is CAD ${fulfillmentFee}")
    elif shippingWeight <= 1.500:
        fulfillmentFee = 7.06
        print(f"Fulfillment Fee is CAD ${fulfillmentFee}")
    elif shippingWeight > 1.500:
        fulfillmentFee = 7.06
        additionalFee = math.ceil((shippingWeight - 1.500)/0.500)*0.43
        fulfillmentFee = fulfillmentFee + additionalFee
        print(f"Fulfillment Fee is CAD ${fulfillmentFee}")
elif sizeTier == "Envelope":
    if shippingWeight <= 0.1:
        fulfillmentFee = 3.37
        print(f"Fulfillment Fee is CAD ${fulfillmentFee}")
    elif shippingWeight > 0.1:
        fulfillmentFee = 3.37
        additionalFee = math.ceil((shippingWeight - 0.1)/0.1)*0.31
        fulfillmentFee = fulfillmentFee + additionalFee
        print(f"Fulfillment Fee is CAD ${fulfillmentFee}")
elif sizeTier == "Oversize":
    if shippingWeight <= 1:
        fulfillmentFee = 9.71
        print(f"Fulfillment Fee is CAD ${fulfillmentFee}")
    elif shippingWeight > 1:
        fulfillmentFee = 9.71
        additionalFee = math.ceil((shippingWeight - 1)/0.5)*0.44
        fulfillmentFee = fulfillmentFee + additionalFee
        print(f"Fulfillment Fee is CAD ${fulfillmentFee}")
elif sizeTier == "Oversize - Special Handling":
    if shippingWeight <= 1:
        fulfillmentFee = 9.71
        print(f"Fulfillment Fee is CAD ${fulfillmentFee} plus Oversize - Special Handling Fee")
    elif shippingWeight > 1:
        fulfillmentFee = 9.71
        additionalFee = math.ceil((shippingWeight - 1)/0.5)*0.44
        fulfillmentFee = fulfillmentFee + additionalFee
        print(f"Fulfillment Fee is CAD ${fulfillmentFee} plus Oversize - Special Handling Fee")

