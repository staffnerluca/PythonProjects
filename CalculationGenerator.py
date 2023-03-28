import random
from fpdf import FPDF


def createMultiplication():
    first = random.randint(1, 10)
    second = random.randint(1, 10)
    return f"{first}·{second}=____"


def createDivision():
    while True:
        first = random.randint(1, 100)
        second = random.randint(1, 10)
        if first % second == 0 and first/second <= 10:
            return f"{first}:{second}=____"

def createAddition(digits): 
    while True:
        first = random.randint(0, 10**digits)
        second = random.randint(0, 10**digits)
        if first + second <= 100**digits:
            return f"{first}+{second}=____"

def createAdditionUnder(number):
    while True:
        output = []
        su = 0
        for i in range(number):
            output.append(random.randint(0, 9999))
        if not sum(output) > 9999:
            return output            
        
def createAdditionOrSubtraction():
    while True:
        first = random.randint(0, 100)
        second = random.randint(0, 100)
        #1 is plus and 0 is minus
        plusOrMinus = random.randint(0, 1)
        if plusOrMinus == 1:
            if first + second <= 100:
                return f"{first}+{second}=____"
        elif plusOrMinus == 0:
            if first >= second:
                return f"{first}-{second}=____"
            else:
                return f"{second}-{first}=____"

def createSubtraction():
    first = random.randint(0, 100)
    second = random.randint(0, 100)
    if first>second:
        return f"{first}-{second}=____"
    else:
        return f"{second}-{first}=____"

def createDivisionRemain():
    first = random.randint(0, 100)
    second = random.randint(2, 10)
    if first>second:
        return f"{first}:{second}=___"
    else:
        return f"{second}:{first}=___"

def createChangeMeasure():
    lengths = ["mm", "cm", "dm", "m"]
    while True:
        original = random.randint(0, 1000)
        startMeasure = random.randint(0, 3)
        goalMeasure = random.randint(0, 3)
        if (startMeasure>goalMeasure or original % 10**(goalMeasure-startMeasure) == 0) and not startMeasure == goalMeasure:
            return f"{original} {lengths[startMeasure]} = ___ {lengths[goalMeasure]}"
        

if __name__ == '__main__':
    kindOfSlip = int(input("1) Multiplikation; 2) Addition, 3) Division, 4) Subtraction, 5) Division with remainder 6)Addition and subtraction 7) change measure, 8) Addition three digits, 9) Addition with numbers under each other: "))
    pdf = FPDF("P", "mm", "A4")
    size=20
    numberOfSlips=int(input("How many slips are needed?: "))
    if kindOfSlip == 9:
        rows9 = int(input("How many rows? "))
    for i in range(numberOfSlips):
        pdf.add_page()
        pdf.set_font("times", "", 16)
        pdf.cell(180, 30, f"Calculations", 1, new_x="LMARGIN", new_y="NEXT", align="C")
        pdf.cell(180, 10, "", 0, new_x="LMARGIN", new_y="NEXT")
        for i in range(size):
            if kindOfSlip == 1:
                for x in range(4):
                    pdf.cell(40, 10, createMultiplication())
                pdf.cell(40, 10, createMultiplication(), new_x="LMARGIN", new_y="NEXT")
            elif kindOfSlip == 2:
                for z in range(4):
                    pdf.cell(40, 10, createAddition(2))
                pdf.cell(40, 10, createAdditionTwoDigits(2), new_x="LMARGIN", new_y="NEXT")
            elif kindOfSlip == 3:
                for y in range(4):
                    pdf.cell(40, 10, createDivision())
                pdf.cell(40, 10, createDivision(), new_x="LMARGIN", new_y="NEXT")
            elif kindOfSlip == 4:
                for y in range(4):
                    pdf.cell(40, 10, createSubtraction())
                pdf.cell(40, 10, createSubtraction(), new_x="LMARGIN", new_y="NEXT")
            elif kindOfSlip == 5:
                for y in range(4):
                    pdf.cell(40, 10, createDivisionRemain())
                pdf.cell(40, 10, createDivisionRemain(), new_x="LMARGIN", new_y="NEXT")
                for y in range(4):
                    pdf.cell(40, 10, "R:")
                pdf.cell(40, 10, "R:",  new_x="LMARGIN", new_y="NEXT")
            elif kindOfSlip == 6:
                for y in range(4):
                    pdf.cell(40, 10, createAdditionOrSubtraction())
                pdf.cell(40, 10, createAdditionOrSubtraction(), new_x="LMARGIN", new_y="NEXT")
            elif kindOfSlip == 7:
                for y in range(3):
                    pdf.cell(50, 10, createChangeMeasure())
                pdf.cell(50, 10, createChangeMeasure(), new_x="LMARGIN", new_y="NEXT")
            elif kindOfSlip == 8:
                for y in range(3):
                    pdf.cell(50, 10, createAddition(3))
                pdf.cell(50, 10, createAddition(3), new_x="LMARGIN", new_y="NEXT")
        if kindOfSlip == 9:
            for y in range(4):
                for i in range(rows9):
                    for y in range(4):
                        pdf.cell(50, 10, str(random.randint(0, 1000)))
                    pdf.cell(50, 10, str(random.randint(0, 1000)), new_x="LMARGIN", new_y="NEXT")
                for i in range(4):
                    pdf.cell(50, 10, "-------")
                pdf.cell(50, 10, "-------", new_x="LMARGIN", new_y="NEXT")
                for z in range(2):
                    for i in range(4):
                        pdf.cell(50, 10, "")
                    pdf.cell(50, 10, "", new_x="LMARGIN", new_y="NEXT")
    pdf.output("Caluclations.pdf")
