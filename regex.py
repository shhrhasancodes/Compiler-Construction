import re

MDM = ['*', '/', '%']
PM = ['+', '-']
AS_Operator = ['+=', '-=', '*=', '/=', '%=', '=']
incdecOP = ['++', '--']
logicalOp = ['&&', '||', '!']
relationalOP = ['<', '>', '<=', '>=', '!=', '==']
punctuator = [',', ';', '(', ')', '{', '}', '[', ']', ':', '?']
Data_Types = ['int', 'string', 'float', 'char', 'bool']
Access_Modifier = ['public', 'private', 'protected']
Void = ['void']


def is_keyword(str):
    keyword = ["return", "false", "break", "while", "for", "class", "if",
               "else", "try", "except", "finally", "continue", "def", "print", "true", "extends", "this", "super", "new", "do", "static", "args", "Main"]
    if str in keyword:
        return (str)
    elif str in MDM:
        return str
    elif str in Data_Types:
        return str
    elif str in Access_Modifier:
        return str
    elif str in PM:
        return str
    elif str in relationalOP:
        return str
    elif str in logicalOp:
        return str
    elif str in incdecOP:
        return str
    elif str in punctuator:
        return str
    elif str in AS_Operator:
        return str
    elif str in Void:
        return str
    elif str == "$":
        return str
    elif re.fullmatch("(^[^\d\W]\w*\Z)", str):
        return ('ID')
    elif(re.fullmatch("([+|-][0-9]+)|([0-9]+)", str)):
        return ("IC")
    elif(re.fullmatch("([+|-][0-9]*[.][0-9]+)|([0-9]*[.][0-9]+)", str)):
        return ("FC")
    elif(re.fullmatch("[\w\W]", str)):
        return ("CC")
    elif (re.fullmatch("[\"][\w\W]*[\"]", str)):
        return ("SC")
    else:
        return "invalid lexeme"


#AssignOP = ['=']
# elif (re.fullmatch("[\"][\w\W]*", str)):
    #     return ("Is String Constatnt")
# elif str in AssignOP:
    #     return ('ASO')


# def Is_Identifier(string):
#     if(re.fullmatch("(^[^\d\W]\w*\Z)", string)):
#         print('Is Identifier')
#     else:
#         Is_Int_Constatnt(string)


# def Is_Int_Constatnt(string):
#     if(re.fullmatch("([+|-][0-9]+)|([0-9]+)", string)):
#         print("Is Int Constatnt")
#     else:
#         Is_Float_Constant(string)


# def Is_Float_Constant(string):
#     if(re.fullmatch("([+|-][0-9]*[.][0-9]+)|([0-9]*[.][0-9]+)", string)):
#         print("Is Float Constatnt")
#     else:
#         Is_Char_Constant(string)


# def Is_Char_Constant(string):
#     if(re.fullmatch("[\w\W]", string)):
#         print("Is Char Constatnt")
#     else:
#         Is_String_Constant(string)


# def Is_String_Constant(string):
#     if(re.fullmatch("[\w\W]*", string)):
#         print("Is String Constatnt")
#     else:
#         return "invalid lexeme"


# str = input()
# is_keyword(str)
