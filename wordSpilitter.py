from enum import Flag
from regex import *
import pandas as pd

#file = "words.txt"
lineNo = 1    # line no in file
temp = ""     # store word

classPart = []
ValuePart = []
line = []

Qotation = addFlag = equalFlag = minusFlag = multiplyFlag = divideFlag = mcommentFlag = moduloFlag = lessthanFlag = notFlag = greaterthanFlag = orFlag = dotFlag = AndFlag = False

qoutationCount = addCount = equalCount = minusCount = AndCount = orCount = mcommentCount = last_line = 0

char = qotationTemp = dotTemp = dotTemp1 = dot = ""


def printWord(string):

    global temp, char, lineNo, classPart, ValuePart, line
    classPart.append(str(is_keyword(string)))
    ValuePart.append(temp)
    line.append(lineNo)
    temp = ""


def Printing():

    global classPart, ValuePart, line
    file2 = open("Tokens.txt", "w")

    data = {
        "classPart": classPart,
        "ValuePart": ValuePart,
        "LineNo": line
    }
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df = pd.DataFrame(data)
    file2.write(str(df))
    file2.close()
    temp = ""
    # print(df)
    return df
    # for ind in df.index:
    #     print(df['classPart'][ind])


def wordCount(file):

    global lineNo, temp, Qotation, qoutationCount, addCount, equalCount, addFlag, equalFlag, minusCount, minusFlag, multiplyFlag, moduloFlag, divideFlag, notFlag, greaterthanFlag, lessthanFlag, char, AndCount, AndFlag, orCount, orFlag, dotFlag, dotTemp, dotTemp1, dot, mcommentFlag, mcommentCount, last_line, qotationTemp

    punctuator = [',', ';', '(', ')', '{', '}', '[', ']', ':', '?']
    operator = ['*', '/', '%', '!', '<', '>']
    PlusMinus = ['+', '-']

    with open(file, 'r') as files:  # open and close files
        for line in files:             # iterate through lines in file
            for char in line:          # iterate through character in a line
                # if new line character founded , print temp increase line no by 1 and reset char and temp
                if char == "\n" and Qotation == False and mcommentFlag == False and dotFlag == False:
                    if temp != "":
                        printWord(temp)
                        char = ""
                        lineNo += 1
                        addFlag = equalFlag = minusFlag = multiplyFlag = divideFlag = moduloFlag = lessthanFlag = notFlag = greaterthanFlag = orFlag = dotFlag = AndFlag = False
                    else:
                        temp = ""
                        char = ""
                        lineNo += 1
                elif char == "\n" and mcommentFlag == True:
                    lineNo += 1

                if char == "~" and Qotation == True:
                    pass
                elif char == "~":
                    mcommentCount += 1
                    mcommentFlag = True
                    if temp != "" and mcommentCount == 1:
                        printWord(temp)
                        temp = char
                        char = ''
                    elif mcommentCount == 2:
                        temp = ""
                        char = ""
                        mcommentCount = 0
                        mcommentFlag = False

                # space condition
                if char == " " and Qotation == True:
                    pass
                elif char == " " and mcommentFlag == True:
                    pass
                elif char == " ":
                    addFlag = equalFlag = minusFlag = multiplyFlag = divideFlag = moduloFlag = lessthanFlag = notFlag = greaterthanFlag = orFlag = dotFlag = AndFlag = False
                    addCount = minusCount = equalCount = AndCount = orCount = 0
                    if temp != "":
                        printWord(temp)
                        char = ""
                    char = ""

                if char in punctuator and Qotation == True:
                    pass
                elif char in punctuator and mcommentFlag == True:
                    pass
                elif char in punctuator:
                    if temp != "":
                        printWord(temp)
                    temp = temp + char
                    printWord(temp)
                    temp = ""
                    char = ""

                elif char == "\"" and mcommentFlag == True:
                    pass
                elif char == "\"":
                    qotationTemp = char
                    Qotation = True
                    qoutationCount += 1

                    if temp != "" and qoutationCount == 1:
                        printWord(temp)

                    if char == "\"" and qoutationCount == 2:
                        qoutationCount = 0
                        Qotation = False
                        printWord(qotationTemp+temp+qotationTemp)
                        qotationTemp = ""
                    char = ""

                elif char == "\n" and qoutationCount == 1:
                    qoutationCount = 0
                    Qotation = False
                    qotationTemp = qotationTemp+temp
                    temp = qotationTemp
                    printWord(qotationTemp)
                    char = ""
                    lineNo += 1

                # addition condition
                if char == "+" and Qotation == True:
                    pass
                elif char == "+" and mcommentFlag == True:
                    pass
                elif char == "+":
                    addCount += 1
                    if temp != "" and addFlag == False:
                        printWord(temp)
                    addFlag = True
                    if temp == "+" and addCount == 2:
                        addCount = 0
                        addFlag = False
                        temp = temp+char
                        printWord(temp)
                        char = ""
                    elif temp != "" and addCount == 2:
                        printWord(temp)
                        addCount = 0
                        addFlag = False

                # minus condition
                if char == "-" and Qotation == True:
                    pass
                elif char == "-" and mcommentFlag == True:
                    pass
                elif char == "-":
                    minusCount += 1
                    if temp != "" and minusFlag == False:
                        printWord(temp)
                    minusFlag = True
                    if temp == "-" and minusCount == 2:
                        minusCount = 0
                        minusFlag = False
                        temp = temp+char
                        printWord(temp)
                        char = ""
                    elif temp != "" and minusCount == 2:
                        printWord(temp)
                        minusCount = 0
                        minusFlag = False

                if temp in PlusMinus and char == "=" and Qotation == True:
                    pass
                elif temp in PlusMinus and char == "=" and mcommentFlag == True:
                    pass
                elif temp in PlusMinus and char == "=":
                    temp = temp+char
                    printWord(temp)
                    addCount = 0
                    addFlag = False
                    minusCount = 0
                    minusFlag = False
                    char = ""

                if temp in PlusMinus and char != "" and Qotation == True:
                    pass
                elif temp in PlusMinus and char != "" and mcommentFlag == True:
                    pass
                elif temp in PlusMinus and char != "":
                    if re.fullmatch("(^[^\d\W]\w*\Z)", char):
                        printWord(temp)
                        addCount = 0
                        addFlag = False
                        minusCount = 0
                        minusFlag = False

                # operator conditions
                if char in operator and Qotation == True:
                    pass
                elif char in operator and mcommentFlag == True:
                    pass
                elif char in operator:
                    if temp != "" and greaterthanFlag == False and char == "<":
                        printWord(temp)
                    greaterthanFlag = True
                    if temp != "" and lessthanFlag == False and char == ">":
                        printWord(temp)
                    lessthanFlag = True
                    if temp != "" and notFlag == False and char == "!":
                        printWord(temp)
                    notFlag = True
                    if temp != "" and moduloFlag == False and char == "%":
                        printWord(temp)
                    moduloFlag = True
                    if temp != "" and divideFlag == False and char == "/":
                        printWord(temp)
                    divideFlag = True
                    if temp != "" and multiplyFlag == False and char == "*":
                        printWord(temp)
                    multiplyFlag = True

                if temp in operator and char == "=" and Qotation == True:
                    pass
                elif temp in operator and char == "=" and mcommentFlag == True:
                    pass
                elif temp in operator and char == "=":
                    temp = temp+char
                    printWord(temp)
                    multiplyFlag = divideFlag = moduloFlag = notFlag = greaterthanFlag = lessthanFlag = False
                    char = ""

                if temp in operator and char != "=" and Qotation == True:
                    pass
                elif temp in operator and char != "=" and mcommentFlag == True:
                    pass
                elif temp in operator and char != "=":
                    printWord(temp)
                    multiplyFlag = divideFlag = moduloFlag = notFlag = greaterthanFlag = lessthanFlag = False

                # && condition
                if char == "&" and Qotation == True:
                    pass
                elif char == "&" and mcommentFlag == True:
                    pass
                elif char == "&":
                    AndCount += 1
                    if temp != "" and AndFlag == False:
                        printWord(temp)
                    AndFlag = True
                    if temp != "" and AndCount == 2:
                        AndCount = 0
                        AndFlag = False
                        temp = temp+char
                        printWord(temp)
                        char = ""

                # || condition
                if char == "|" and Qotation == True:
                    pass
                elif char == "|" and mcommentFlag == True:
                    pass
                elif char == "|":
                    orCount += 1
                    if temp != "" and orFlag == False:
                        printWord(temp)
                    orFlag = True
                    if temp != "" and orCount == 2:
                        orCount = 0
                        orFlag = False
                        temp = temp+char
                        printWord(temp)
                        char = ""

                # dot condition
                if char == "." and Qotation == True:
                    pass
                elif char == "." and mcommentFlag == True:
                    pass
                elif char == ".":
                    if temp != "" and dotFlag == False:
                        if re.fullmatch("([+|-][0-9]+)|([0-9]+)", temp):
                            dotTemp = temp
                            temp = ""
                            dotFlag = True
                            dot = char
                            char = ""
                        else:
                            printWord(temp)
                            dotFlag = True
                            dot = char
                            char = ""
                    elif temp != "" and dotFlag == True:
                        if re.fullmatch("([+|-][0-9]+)|([0-9]+)", temp):
                            dotTemp1 = temp
                            temp = dotTemp+dot+dotTemp1
                            printWord(temp)
                            dotFlag = False
                            dot = dotTemp = dotTemp1 = ""
                        else:
                            if dot != "":
                                i = temp
                                temp = dot
                                printWord(temp)
                                temp = i
                            printWord(temp)
                            dotFlag = True
                            dot = char
                            char = ""
                    else:
                        dot = char
                        char = ""
                        dotFlag = True

                if dotFlag == True and Qotation == True:
                    pass
                elif dotFlag == True and mcommentFlag == True:
                    pass
                elif dotFlag == True and char == "\n":
                    if temp != "" and dotFlag == True:
                        if re.fullmatch("([+|-][0-9]+)|([0-9]+)", temp):
                            dotTemp1 = temp
                            temp = dotTemp+dot+dotTemp1
                            printWord(temp)
                            dot = dotTemp = dotTemp1 = char = ""
                            lineNo += 1
                            addFlag = equalFlag = minusFlag = multiplyFlag = divideFlag = moduloFlag = lessthanFlag = notFlag = greaterthanFlag = orFlag = dotFlag = AndFlag = False
                        else:
                            if dot != "":
                                i = temp
                                temp = dot
                                printWord(temp)
                                temp = i
                            printWord(temp)
                            dot = dotTemp = dotTemp1 = char = ""
                            lineNo += 1
                            addFlag = equalFlag = minusFlag = multiplyFlag = divideFlag = moduloFlag = lessthanFlag = notFlag = greaterthanFlag = orFlag = dotFlag = AndFlag = False

                # equals condition
                if char == "=" and Qotation == True:
                    pass
                elif char == "=" and mcommentFlag == True:
                    pass
                elif char == "=":
                    equalCount += 1
                    if temp != "" and equalFlag == False:
                        printWord(temp)
                    equalFlag = True
                    if temp != "" and equalCount == 2:
                        equalCount = 0
                        equalFlag = False
                        temp = temp+char
                        printWord(temp)
                        char = ""

                if "=" in temp and char != "=" and Qotation == True:
                    pass
                elif "=" in temp and char != "=" and mcommentFlag == True:
                    pass
                elif "=" in temp and char != "=":
                    printWord(temp)
                    equalCount = 0
                    equalFlag = False

                if mcommentFlag == True:
                    temp = temp + char
                else:
                    temp = temp + char

        if mcommentFlag == True:
            printWord(temp)
        else:
            if temp != "" and dotFlag == True:
                i = temp
                temp = dot
                printWord(temp)
                temp = i
                printWord(temp)
            elif temp != "":
                printWord(temp)
    temp = "$"
    printWord(temp)
    return Printing()
