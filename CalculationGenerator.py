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
        
def createNumberWithIndentation():
    num = random.randint(0, 1000)
    tex = ""
    if num < 10:
        tex+="       "
    if num < 100 and num > 10:
        tex+="     "
    elif num < 1000 and num > 100:
        tex+="   "
    tex += str(num)
    return tex

def subtractionUnder():
    out = [str(random.randint(0, 1000))]
    while True:
        subt = random.randint(-1000, 0)
        if int(out[0]) >= (subt*(-1)):
            out.append(str(subt))
            out.append("------")
            out.append("       ")
            return out

def createDivisionUnder():
    while True:
        a = random.randint(0, 1000)
        b = random.randint(2, 10)
        if (a % b) == 0:
            return f"{a}:{b} = ____"
        
def createDivisonUnderWithRemainder():
    a = random.randint(0, 1000)
    b = random.randint(2, 10)
    return f"{a}:{b} = ____"

if __name__ == '__main__':
    kindOfSlip = int(input("""1) Multiplikation; 2) Addition, 3) Division, 4) Subtraction, 
    5) Division with remainder 6)Addition and subtraction 7) change measure, 8) Addition three digits, 
    9) Addition with numbers under each other, 11) Division with a result larger than ten, 12) the same with remainder: """))
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
                pdf.cell(40, 10, createAddition(2), new_x="LMARGIN", new_y="NEXT")
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
            for y in range(3):
                for i in range(rows9):
                    for y in range(4):
                        pdf.cell(50, 10, createNumberWithIndentation())
                    pdf.cell(50, 10, createNumberWithIndentation(), new_x="LMARGIN", new_y="NEXT")
                for i in range(4):
                    pdf.cell(50, 10, "-------")
                pdf.cell(50, 10, "-------", new_x="LMARGIN", new_y="NEXT")
                for z in range(2):
                    for i in range(4):
                        pdf.cell(50, 10, "")
                    pdf.cell(50, 10, "", new_x="LMARGIN", new_y="NEXT")
        elif kindOfSlip == 10:
            lists = []
            for x in range(5):
                for i in range(5):
                    lists.append(subtractionUnder())
                for y in range(4):
                    pdf.cell(30, 10, lists[0][y], align = "R")
                    pdf.cell(30, 10, lists[1][y], align = "R")
                    pdf.cell(30, 10, lists[2][y], align = "R")
                    pdf.cell(30, 10, lists[3][y], align = "R")
                    pdf.cell(30, 10, lists[4][y], align = "R", new_x="LMARGIN", new_y="NEXT")
                lists = []
        elif kindOfSlip == 11:
            for i in range(4):
                for y in range(4):
                    pdf.cell(50, 40, createDivisionUnder())
                pdf.cell(50, 40, createDivisionUnder(), new_x="LMARGIN", new_y="NEXT")
        elif kindOfSlip == 12:
            for i in range(4):
                for y in range(4):
                    pdf.cell(50, 40, createDivisonUnderWithRemainder())
                pdf.cell(50, 40, createDivisonUnderWithRemainder(), new_x="LMARGIN", new_y="NEXT")
    pdf.image("Meerschweinchen/"+str(random.randint(1,4))+".jpg", x = 50, y = 200, w = 100, h = 50)
    pdf.output("Caluclations.pdf")
