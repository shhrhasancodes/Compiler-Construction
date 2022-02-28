import pandas as pd
I = 0

# dot problem


def SST(Tks):
    global I
    SST_sel = ['char', 'int', 'string', 'bool', 'float', 'ID', 'this', 'super', 'while', 'for', 'if', 'do',
               'break', 'continue', 'try', 'print', 'return', '++', '--', 'def', 'class', 'static', 'public', 'private', '$']
    if(Tks['classPart'][I] in SST_sel):
        if(DT(Tks)):
            if(SST1(Tks)):
                return True
        elif(Tks['classPart'][I] == 'ID'):
            I += 1
            if(SST2(Tks)):
                return True
    else:
        return False


def SST1(Tks):
    global I
    if(Tks['classPart'][I] == 'ID'):
        I += 1
        if(List(Tks)):
            return True
    else:
        return False


def SST2(Tks):
    global I
    if(Tks['classPart'][I] == '('):
        I += 1
        if(Parameter1(Tks)):
            if(Tks['classPart'][I] == ')'):
                return True
    elif(Tks['classPart'][I] == 'ID'):
        I += 1
        if(Tks['classPart'][I] == '='):
            I += 1
            if(Tks['classPart'][I] == 'new'):
                I += 1
                if(Tks['classPart'][I] == 'ID'):
                    I += 1
                    if(Tks['classPart'][I] == '('):
                        I += 1
                        if(Parameter1(Tks)):
                            if(Tks['classPart'][I] == ')'):
                                I += 1
                                if(Tks['classPart'][I] == ';'):
                                    return True
    else:
        return False

# Declaration


def DEC(Tks):
    global I
    DEC_sel = ['char', 'int', 'string', 'bool', 'float', 'ID', 'this', 'super', 'while', 'for', 'if', 'do',
               'break', 'continue', 'try', 'print', 'return', '++', '--', 'def', 'class', 'static', 'public', 'private']
    if(Tks['classPart'][I] in DEC_sel):
        if(DT(Tks)):
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                if(List(Tks)):
                    return True
    else:
        return False


def List(Tks):
    global I
    List_sel = [';', ',', 'private', 'public', 'protected', 'int', 'char', 'string', 'bool', 'float', 'def', 'ID', 'super', 'this', 'while',
                'for', 'if', 'return', 'print', 'break', 'continue', 'try', '++', '--', 'IC', 'CC', 'FC', 'SC', '!', '(']
    if(Tks['classPart'][I] in List_sel):
        if(Tks['classPart'][I] == ';'):
            I += 1
            return True
        elif(Tks['classPart'][I] == ','):
            I += 1
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                if(List(Tks)):
                    return True
    else:
        return False


def FuncDec(Tks):
    global I
    Funcdecl_sel = ['def', 'ID', 'int', 'string', 'char', 'float', 'bool', 'this', 'super', 'while', 'for', 'if',
                    'do', 'break', 'continue', 'try', 'print', 'return', '++', '--', 'class', 'public', 'private', 'static', '$']
    if(Tks['classPart'][I] in Funcdecl_sel):
        if(Tks['classPart'][I] == 'def'):
            I += 1
            if(DT(Tks)):
                if(Tks['classPart'][I] == 'ID'):
                    I += 1
                    if(Tks['classPart'][I] == '('):
                        I += 1
                        if(Parameter(Tks)):
                            if(Tks['classPart'][I] == ')'):
                                I += 1
                                if(Body(Tks)):
                                    return True
    else:
        return False


def ClassDec(Tks):
    global I
    print("again")
    Classdecl_sel = ['def', 'ID', 'int', 'string', 'char', 'float', 'bool', 'this', 'super', 'while', 'for', 'if',
                     'do', 'break', 'continue', 'try', 'print', 'return', '++', '--', 'class', 'public', 'private', 'static', '$']
    if(Tks['classPart'][I] in Classdecl_sel):
        if(C_AM(Tks)):
            if(Tks['classPart'][I] == 'class'):
                I += 1
                if(Tks['classPart'][I] == 'ID'):
                    I += 1
                    if(Tks['classPart'][I] == '('):
                        I += 1
                        if(Tks['classPart'][I] == ')'):
                            I += 1
                            if(inh(Tks)):
                                if(C_body(Tks)):
                                    return True
    else:
        return False


def C_AM(Tks):
    C_AM_sel = ['public', 'private', 'class']
    global I
    if Tks['classPart'][I] in C_AM_sel:
        if(Tks['classPart'][I] == 'public'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'private'):
            I += 1
            return True
        return True
    else:
        return False


def inh(Tks):
    global I
    inh_sel = ['extends', ';', '{']
    if(Tks['classPart'][I] in inh_sel):
        if(Tks['classPart'][I] == 'extends'):
            I += 1
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                return True
        return True
    else:
        return False


def C_body(Tks):
    global I
    C_body_sel = ['ID', 'int', 'string', 'char', 'float', 'bool', 'this', 'super', 'while', 'for', 'if', 'do',
                  'break', 'continue', 'try', 'print', 'return', '++', '--', 'class', 'public', 'private', 'static', '$', ';', '{']
    if(Tks['classPart'][I] in C_body_sel):
        if(Tks['classPart'][I] == ';'):
            I += 1
            return True
        elif(Tks['classPart'][I] == '{'):
            I += 1
            if(C_MST(Tks)):
                if(Tks['classPart'][I] == '}'):
                    return True
    else:
        return False


def C_MST(Tks):
    global I
    C_MST_sel = ['def', 'ID', 'int', 'string', 'char',
                 'float', 'bool', 'public', 'private', 'protected', '}']
    if(Tks['classPart'][I] in C_MST_sel):
        if(C_SST(Tks)):
            if(C_MST(Tks)):
                return True
            return True
    else:
        return False


def C_SST(Tks):
    global I
    C_SST_sel = ['def', 'ID', 'int', 'string', 'char',
                 'float', 'bool', 'public', 'private', 'protected', '}']
    if(Tks['classPart'][I] in C_SST_sel):
        if(C_Decl(Tks)):
            return True
        elif(C_FuncDecl(Tks)):
            return True
    else:
        return False


# Decl inside class
def C_Decl(Tks):
    global I
    C_Decl_sel = ['def', 'ID', 'int', 'string', 'char',
                  'float', 'bool', 'public', 'private', 'protected', '}']
    if(Tks['classPart'][I] in C_Decl_sel):
        if(AM(Tks)):
            if(DT(Tks)):
                if(Tks['classPart'][I] == 'ID'):
                    I += 1
                    if(List(Tks)):
                        return True
    else:
        return False


def AM(Tks):
    AM_sel = ['public', 'private', 'protected', 'int', 'string', 'char',
              'float', 'bool']
    global I
    if Tks['classPart'][I] in AM_sel:
        if(Tks['classPart'][I] == 'public'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'private'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'protected'):
            I += 1
            return True
        return True
    else:
        return False


def C_FuncDecl(Tks):
    global I
    C_Funcdecl_sel = ['def', 'ID', 'int', 'string', 'char',
                      'float', 'bool', 'public', 'private', 'protected', '}']
    if(Tks['classPart'][I] in C_Funcdecl_sel):
        if(Tks['classPart'][I] == 'def'):
            I += 1
            if(RT(Tks)):
                if(Tks['classPart'][I] == 'ID'):
                    I += 1
                    if(Tks['classPart'][I] == '('):
                        I += 1
                        if(Parameter(Tks)):
                            if(Tks['classPart'][I] == ')'):
                                I += 1
                                if(F_body(Tks)):
                                    return True
    else:
        return False


def RT(Tks):
    global I
    if(Tks['classPart'][I] == 'void'):
        I += 1
        return True
    elif(DT(Tks)):
        return True
    else:
        return False

# Function body


def F_body(Tks):
    global I
    F_body_sel = ['def', 'ID', 'int', 'string', 'char',
                  'float', 'bool', 'public', 'private', 'protected', '{', ';']
    if(Tks['classPart'][I] in F_body_sel):
        if(Tks['classPart'][I] == ';'):
            I += 1
            return True
        elif(Tks['classPart'][I] == '{'):
            I += 1
            if(F_MST(Tks)):
                if(Tks['classPart'][I] == '}'):
                    I += 1
                    return True
    else:
        return False

# MST inside Function


def F_MST(Tks):
    F_MST_sel = ['super', 'this', 'ID', '=', '+=', '-=', '*=', '/=',
                 '%=', 'while', 'for', 'do', 'if', 'return', 'print', '}', 'int', 'string', 'char',
                 'float', 'bool' ]
    if(Tks['classPart'][I] in F_MST_sel):
        if(F_SST(Tks)):
            if(F_MST(Tks)):
                return True
            return True
    else:
        return False

# SST inside Function


def F_SST(Tks):
    F_SST_sel = ['super', 'this', 'ID', '=', '+=', '-=', '*=', '/=',
                 '%=', 'while', 'for', 'do', 'if', 'return', 'print', '}', 'int', 'string', 'char',
                 'float', 'bool']
    if(Tks['classPart'][I] in F_SST_sel):
        if(Dec1(Tks)):
            return True
    else:
        return False

# Decl inside Function


def Dec1(Tks):
    global I
    if(DT(Tks)):
        if(Tks['classPart'][I] == 'ID'):
            I += 1
            if(List(Tks)):
                return True
    else:
        return False


def Parameter(Tks):
    global I
    parameter_sel = ['char', 'int', 'string', 'bool', 'float', ')']
    if(Tks['classPart'][I] in parameter_sel):
        if(DT(Tks)):
            if(Tks['classPart'][I] == 'ID'):
                I += 1
                if(Tks['classPart'][I] == ','):
                    if P2(Tks):
                        return True
                    return False
                return True
            return False
    else:
        return False


def P2(Tks):
    global I
    if(Tks['classPart'][I] == ','):
        I += 1
        if(Parameter(Tks)):
            return True
        return False
    else:
        return False

# all done after this comment


def DT(Tks):
    global I
    datatype_sel = ['char', 'string', 'int',
                    'bool', 'float', 'ID', 'main', '[']
    if(Tks['classPart'][I] in datatype_sel):
        if(Tks['classPart'][I] == 'int'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'char'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'string'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'float'):
            I += 1
            return True
        elif(Tks['classPart'][I] == 'bool'):
            I += 1
            return True
    else:
        return False


def Parameter1(Tks):
    global I
    Parameter1_sel = ['IC', 'FC', 'CC', 'SC', ')']
    if(Tks['classPart'][I] in Parameter1_sel):
        if(Const(Tks)):
            if(Const1(Tks)):
                return True
            return True
        return True
    else:
        return False


def Const(Tks):
    global I
    if(Tks['classPart'][I] == 'IC'):
        I += 1
        return True
    elif(Tks['classPart'][I] == 'CC'):
        I += 1
        return True
    elif(Tks['classPart'][I] == 'FC'):
        I += 1
        return True
    elif(Tks['classPart'][I] == 'SC'):
        I += 1
        return True
    else:
        return False


def Const1(Tks):
    global I
    if(Tks['classPart'][I] == ','):
        I += 1
        if(Parameter1(Tks)):
            return True
    else:
        return False


def Body(Tks):
    global I
    body_sel = [';', '{', 'int', 'char', 'string', 'bool', 'float', 'ID', 'while', 'if', 'for', 'do',
                'break', 'continue', 'try', 'print', 'return', 'INCDEC', 'else', 'def', 'class', 'static', '$']
    if(Tks['classPart'][I] in body_sel):
        if(Tks['classPart'][I] == ';'):
            I += 1
            return True
        elif(Tks['classPart'][I] == '{'):
            I += 1
            if(MST(Tks)):
                if(Tks['classPart'][I] == '}'):
                    return True
    else:
        return False


def MST(Tks):
    global I
    MST_sel = ['int', 'char', 'bool', 'float', 'string', 'ID', 'this', 'super',
               'while', 'for', 'if', 'do', 'break', 'continue', 'print', 'return', 'INCDEC', '}']

    if(Tks['classPart'][I] in MST_sel):
        if(SST(Tks)):
            if(MST(Tks)):
                return True
            return True
    else:
        return False


def Main(Tks):
    global I
    if(Tks['classPart'][I] == 'static'):
        I += 1
        if(DT(Tks)):
            if(Tks['classPart'][I] == 'Main'):
                I += 1
                if(Tks['classPart'][I] == '('):
                    I += 1
                    if(Tks['classPart'][I] == 'string'):
                        I += 1
                        if(Tks['classPart'][I] == '['):
                            I += 1
                            if(Tks['classPart'][I] == ']'):
                                I += 1
                                if(Tks['classPart'][I] == 'args'):
                                    I += 1
                                    if(Tks['classPart'][I] == ')'):
                                        I += 1
                                        if(Body(Tks)):
                                            return True
    else:
        return False


def Start(Tks):
    global I
    Start_selection = ['int', 'string', 'float', 'char', 'bool', 'ID', 'this', 'super', 'while', 'for', 'if', 'do',
                       'break', 'continue', 'try', 'print', 'return', 'INCDEC', 'def', 'public', 'private', 'class', 'static', '$']

    if (Tks['classPart'][I] in Start_selection):
        if(SST(Tks)):
            if(Start(Tks)):
                return True
            return True
        elif(FuncDec(Tks)):
            if(Start(Tks)):
                return True
            return True
        elif(ClassDec(Tks)):
            if(Start(Tks)):
                return True
            return True
        elif(Main(Tks)):
            if(Start(Tks)):
                return True
            return True
    else:
        return False


def Syntax_Analyzer(Tokens):
    Tks = pd.DataFrame(Tokens)
    global I
    if Start(Tks):
        print("Valid Syntax")
    else:
        print("Sytax Error at Line Number", Tks['LineNo'][I])
