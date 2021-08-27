# Author: Corey Johnson
# Date: 2021-08-26
# Title: Amazon Fulfillment Fee Calculator


from tkinter import *
import math

OPTIONS = [
    "Amazon US",
    "Amazon CA",
    "Walmart"
]


def calculateFulfillmentFeeUS():
    length = float(length_e.get())
    width = float(width_e.get())
    height = float(height_e.get())
    unitWeight = float(unitWeight_e.get())
    girth = (width + height) * 2
    dimWeight = (length * width * height) / 139

    """Calculate Product Size Tier"""
    if length <= 15 and width <= 12 and height <= 0.75 and unitWeight <= 1:
        sizeTier = "Small standard-size"
        # print(sizeTier)
    elif length <= 18 and width <= 14 and height <= 8 and unitWeight <= 20:
        sizeTier = "Large standard-size"
        # print(sizeTier)
    elif (length > 18 or width > 14 or height > 8) and (
            length <= 60 and width <= 30 and unitWeight <= 70 and (length + girth) <= 130):
        sizeTier = "Small oversize"
        # print(sizeTier)
    elif (length > 60 or width > 30 or unitWeight > 70) and (
            length <= 108 and unitWeight <= 150 and (length + girth) <= 130):
        sizeTier = "Medium oversize"
        # print(sizeTier)
    elif (length > 60 or width > 30 or unitWeight > 70) and (
            length <= 108 and unitWeight <= 150 and (length + girth) <= 165):
        sizeTier = "Large oversize"
        # print(sizeTier)
    elif length > 108 or (unitWeight or dimWeight) > 150 or (length + girth) > 165:
        sizeTier = "Special Oversize"
        # print(sizeTier)
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

    # print(f"Shipping Weight: {shippingWeight}")

    """Calculate Fulfillment Fee"""
    if sizeTier == "Small standard-size":
        if shippingWeight * 16 <= 6:
            fulfillFee = 2.70
            # print(f"Fulfillment Fee is ${fulfillFee}")
        elif 6 < shippingWeight * 16 <= 12:
            fulfillFee = 2.84
            # print(f"Fulfillment Fee is ${fulfillFee}")
        elif 12 < shippingWeight * 16 <= 16:
            fulfillFee = 3.32
            # print(f"Fulfillment Fee is ${fulfillFee}")
    elif sizeTier == "Large standard-size":
        if shippingWeight * 16 <= 6:
            fulfillFee = 3.47
            # print(f"Fulfillment Fee is ${fulfillFee}")
        elif 6 < shippingWeight * 16 <= 12:
            fulfillFee = 3.64
            # print(f"Fulfillment Fee is ${fulfillFee}")
        elif 12 < shippingWeight * 16 <= 16:
            fulfillFee = 4.25
            # print(f"Fulfillment Fee is ${fulfillFee}")
        elif 1 < shippingWeight <= 2:
            fulfillFee = 4.95
            # print(f"Fulfillment Fee is ${fulfillFee}")
        elif 2 < shippingWeight <= 3:
            fulfillFee = 5.68
            # print(f"Fulfillment Fee is ${fulfillFee}")
        elif shippingWeight > 3:
            weightFee = 0.3 * math.ceil(shippingWeight - 3)
            fulfillFee = round(5.68 + weightFee, 2)
            # print(f"Fulfillment Fee is ${fulfillFee}")
    elif sizeTier == "Small oversize":
        if shippingWeight <= 70:
            weightFee = 0.38 * math.ceil(shippingWeight - 1)
            fulfillFee = round(8.66 + weightFee, 2)
            # print(f"Fulfillment Fee is ${fulfillFee}")
    elif sizeTier == "Medium oversize":
        if shippingWeight <= 150:
            weightFee = 0.39 * math.ceil(shippingWeight - 1)
            fulfillFee = round(11.37 + weightFee, 2)
            # print(f"Fulfillment Fee is ${fulfillFee}")
    elif sizeTier == "Large oversize":
        if shippingWeight <= 90:
            fulfillFee = round(76.57, 2)
            # print(f"Fulfillment Fee is ${fulfillFee}")
        elif 90 < shippingWeight <= 150:
            weightFee = 0.79 * math.ceil(shippingWeight - 90)
            fulfillFee = round(76.57 + weightFee, 2)
            # print(f"Fulfillment Fee is ${fulfillFee}")
    elif sizeTier == "Special oversize":
        if shippingWeight <= 90:
            fulfillFee = round(138.11, 2)
            # print(f"Fulfillment Fee is ${fulfillFee}")
        elif 90 < shippingWeight <= 150:
            weightFee = 0.79 * math.ceil(shippingWeight - 90)
            fulfillFee = round(138.11 + weightFee, 2)
            # print(f"Fulfillment Fee is ${fulfillFee}")
    fulfillmentFeeEntry.set(fulfillFee)
    sizeTierText.set(sizeTier)


def calculateFulfillmentFeeCA():
    length = float(length_e.get())
    width = float(width_e.get())
    height = float(height_e.get())
    unitWeight = float(unitWeight_e.get())
    girth = (width + height) * 2

    """Calculate Product Size Tier"""
    if length <= 38 and width <= 27 and height <= 2 and unitWeight <= 0.5:
        sizeTier = "Envelope"
        # print(sizeTier)
    elif (length > 38 or width > 27 or height > 2) and (
            length <= 45 and width <= 35 and height <= 20 and unitWeight <= 9):
        sizeTier = "Standard-size"
        # print(sizeTier)
    elif length > 270 or (length + (2 * width) + (2 * height)) > 419 or unitWeight > 69:
        sizeTier = "Oversize - Special Handling"
        # print(sizeTier)
    elif length > 45 or width > 35 or height > 20 or 9 < unitWeight <= 69:
        sizeTier = "Oversize"
        # print(sizeTier)
    else:
        print("\n------------------------------------\n" +
              "Error - Check Dimensions and Weight \n" +
              "------------------------------------\n")

    """Calculate Shipping Weight"""
    dimWeight = (length * width * height) / 5000

    if sizeTier == "Envelope":
        if dimWeight > unitWeight:
            shippingWeight = dimWeight
        else:
            shippingWeight = unitWeight

        shippingWeight = math.ceil((shippingWeight + 0.025) * 10) / 10
        # print(f"Shipping Weight: {shippingWeight}")
    elif sizeTier == "Standard-size":
        if dimWeight > unitWeight:
            shippingWeight = dimWeight
        else:
            shippingWeight = unitWeight

        if shippingWeight < 0.25:
            shippingWeight = math.ceil((shippingWeight + 0.04) * 4) / 4
        elif 0.25 <= shippingWeight < 0.5:
            shippingWeight = math.ceil((shippingWeight + 0.06) * 4) / 4
        elif shippingWeight >= 0.5:
            shippingWeight = math.ceil((shippingWeight + 0.125) * 4) / 4
        # print(f"Shipping Weight: {shippingWeight}")
    elif sizeTier == "Oversize" or "Oversize - Special Handling":
        if dimWeight > unitWeight:
            shippingWeight = dimWeight
        else:
            shippingWeight = unitWeight

        shippingWeight = math.ceil((shippingWeight + 0.5) * 2) / 2
        # print(f"Shipping Weight: {shippingWeight}")

    """Calculate Fulfillment Fee"""
    if sizeTier == "Standard-size":
        if shippingWeight <= 0.250:
            fulfillFee = 5.44
            # print(f"Fulfillment Fee is CAD ${fulfillFee}")
        elif shippingWeight <= 0.500:
            fulfillFee = 5.57
            # print(f"Fulfillment Fee is CAD ${fulfillFee}")
        elif shippingWeight <= 1.000:
            fulfillFee = 6.40
            # print(f"Fulfillment Fee is CAD ${fulfillFee}")
        elif shippingWeight <= 1.500:
            fulfillFee = 7.06
            # print(f"Fulfillment Fee is CAD ${fulfillFee}")
        elif shippingWeight > 1.500:
            fulfillFee = 7.06
            additionalFee = math.ceil((shippingWeight - 1.500) / 0.500) * 0.43
            fulfillFee = fulfillFee + additionalFee
            # print(f"Fulfillment Fee is CAD ${fulfillFee}")
    elif sizeTier == "Envelope":
        if shippingWeight <= 0.1:
            fulfillFee = 3.37
            # print(f"Fulfillment Fee is CAD ${fulfillFee}")
        elif shippingWeight > 0.1:
            fulfillFee = 3.37
            additionalFee = math.ceil((shippingWeight - 0.1) / 0.1) * 0.31
            fulfillFee = fulfillFee + additionalFee
            # print(f"Fulfillment Fee is CAD ${fulfillFee}")
    elif sizeTier == "Oversize":
        if shippingWeight <= 1:
            fulfillFee = 9.71
            # print(f"Fulfillment Fee is CAD ${fulfillFee}")
        elif shippingWeight > 1:
            fulfillFee = 9.71
            additionalFee = math.ceil((shippingWeight - 1) / 0.5) * 0.44
            fulfillFee = fulfillFee + additionalFee
            # print(f"Fulfillment Fee is CAD ${fulfillFee}")
    elif sizeTier == "Oversize - Special Handling":
        if shippingWeight <= 1:
            fulfillFee = 9.71
            # print(f"Fulfillment Fee is CAD ${fulfillFee} plus Oversize - Special Handling Fee")
        elif shippingWeight > 1:
            fulfillFee = 9.71
            additionalFee = math.ceil((shippingWeight - 1) / 0.5) * 0.44
            fulfillFee = fulfillFee + additionalFee
            # print(f"Fulfillment Fee is CAD ${fulfillFee} plus Oversize - Special Handling Fee")
    fulfillmentFeeEntry.set(fulfillFee)
    sizeTierText.set(sizeTier)


def calculateFulfillmentFeeWalmart():
    length = float(length_e.get())
    width = float(width_e.get())
    height = float(height_e.get())
    unitWeight = float(unitWeight_e.get())
    girth = (width + height) * 2
    dimWeight = (length * width * height) / 139
    sizeTier = "size"

    if dimWeight > unitWeight:
        shippingWeight = dimWeight
    else:
        shippingWeight = unitWeight

    shippingWeight = shippingWeight + 0.25

    if shippingWeight <= 1:
        fulfillFee = 3.45
        # print("Fulfillment Fee is $3.45")
    elif shippingWeight <= 2:
        fulfillFee = 4.95
        # print("Fulfillment Fee is $4.95")
    elif shippingWeight <= 3:
        fulfillFee = 5.45
        # print("Fulfillment Fee is $5.45")
    elif shippingWeight > 3:
        fulfillFee = 5.75
        if 4 < shippingWeight <= 20:
            shippingWeight = math.ceil(shippingWeight)
            additionalFee = (shippingWeight - 4) * 0.4
            fulfillFee = fulfillFee + additionalFee
        elif shippingWeight > 20:
            shippingWeight = math.ceil(shippingWeight)
            additionalFee = ((shippingWeight - 4) * 0.4) + 3
            fulfillFee = fulfillFee + additionalFee
        # print(f"Fulfillment Fee is ${fulfillmentFee}")
    fulfillmentFeeEntry.set(fulfillFee)
    sizeTierText.set(sizeTier)


# Initiate Tkinter
master = Tk()
fulfillmentFeeEntry = DoubleVar()
sizeTierText = StringVar()
market = StringVar(master)
market.set(OPTIONS[0])  # default value
popupMenu = OptionMenu(master, market, *OPTIONS)

# Sets up the GUI with labels
Label(master, text="Select Market: ").grid(row=0, sticky=W)
popupMenu.grid(row=0, column=1)
Label(master, text="Longest:").grid(row=1, sticky=W)
Label(master, text="Median:").grid(row=2, sticky=W)
Label(master, text="Shortest:").grid(row=3, sticky=W)
Label(master, text="Weight:").grid(row=4, sticky=W)
Label(master, text="Fulfillment Fee:").grid(row=6, sticky=W)
result = Label(master, text="", textvariable=fulfillmentFeeEntry).grid(row=6, column=1, sticky=W)
Label(master, text="Size Tier:").grid(row=7, sticky=W)
sizeTierResult = Label(master, text="", textvariable=sizeTierText).grid(row=7, column=1, sticky=W)

# Input boxes for the user
length_e = Entry(master)
width_e = Entry(master)
height_e = Entry(master)
unitWeight_e = Entry(master)

# Placement of the Variables on the GUI
length_e.grid(row=1, column=1)
width_e.grid(row=2, column=1)
height_e.grid(row=3, column=1)
unitWeight_e.grid(row=4, column=1)

b = Button(master, text="Calculate", command=lambda: calculateFulfillmentFeeUS() if market.get() == "Amazon US"
else (calculateFulfillmentFeeCA() if market.get() == "Amazon CA" else calculateFulfillmentFeeWalmart()))
b.grid(row=2, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)

# Changes the Market Fees that will be calculated
def change_dropdown(*args):
    print(market.get())


#market.trace('w', change_dropdown)

mainloop()
