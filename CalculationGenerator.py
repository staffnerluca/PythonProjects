#This program creats a slip that contains 100 calculations to study with kids the basics of math. 100 is the highest result you can get.
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

def createAddition(): 
    while True:
        first = random.randint(0, 100)
        second = random.randint(0, 100)
        if first + second <= 100:
            return f"{first}+{second}=____"

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

if __name__ == '__main__':
    kindOfSlip = int(input("1) Multiplikation; 2) Addition, 3) Division, 4) Subtraction, 5) Division with remainder 6)Addition and subtraction: "))
    pdf = FPDF("P", "mm", "A4")
    size=20
    numberOfSlips=int(input("How many slips are needed?: "))
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
                    pdf.cell(40, 10, createAddition())
                pdf.cell(40, 10, createAdditionOrSubtraction(), new_x="LMARGIN", new_y="NEXT")
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
    pdf.output("Caluclations.pdf")
