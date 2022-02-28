from asyncio.windows_events import NULL
import pandas as pd
I = 0






class MTEntry:
    
    def __init__(self, N, T, C, P):
        self.name = N
        self.type = T
        self.category = C
        self.parent = P

class ATEntry:
    
    def __init__(self, N, T, AM, CN):
        self.name = N
        self.type = T
        self.accessmod = AM
        self.classname = CN

class FTEntry():
    
    def __init__(self, N, T, Scope):
        self.name = N
        self.type = T
        self.scope = Scope

#Main Table dictionary
MT = []

#Attribute Table
AT = {}

#Function Table
FT = {}

#Scope
scope = 0

#Scope stack
scope_stack = []

#Current Class Reference
class_ref = ''

def Insert_MT(N, T, C, P):
    global MT
    global AT
    global class_ref

    class_ref = N

    try:
        mtobj = MTEntry(N, T, C, P)
        MT.append(mtobj)

        AT [class_ref] = []
        FT [class_ref] = []
        return True
    except:
        return False

def LookUp_MT(N):
    global MT

    for entry in MT:
        if entry.name == N:
            return entry
    return NULL

def Create_Scope():
    global scope
    global scope_stack

    scope += 1
    scope_stack.append(scope)

def Delete_Scope():
    global scope_stack
    
    scope_stack.pop()

def Compatibility(L, R, OP):
    pass

def Insert_AT(N, T, AM, CN):
    global class_ref
    global AT

    atobj = ATEntry(N, T, AM, CN)
    try:
        AT[class_ref].append(atobj)
        return True
    except:
        return False

def LookUp_AT_V(N, CN):
    global AT

    if CN in AT.keys():
        for table in AT[CN]:
            for entry in table:
                if entry.name == N:
                    return entry
    return NULL

def LookUp_AT_F(N, PL, CN):
    global AT

    if CN in AT.keys():
        for table in AT[CN]:
            for entry in table:
                if entry.name == N:
                    if entry.type == PL:
                        return entry
    return NULL

def LookUp_FT(N, Scope):
    global FT
    global class_ref

    for table in FT[class_ref]:
        for entry in table:
            if entry.name == N:
                if entry.scope == Scope:
                    return entry.type
    return NULL            

def InsertFT(N, T, Scope):
    global FT
    global class_ref

    ftobj = FTEntry(N, T, Scope)

    try:
        FT[class_ref].append(ftobj)
        return True
    except:
        return False









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
    Classdecl_sel = ['def', 'ID', 'int', 'string', 'char', 'float', 'bool', 'this', 'super', 'while', 'for', 'if',
                     'do', 'break', 'continue', 'try', 'print', 'return', '++', '--', 'class', 'public', 'private', 'static', '$']
    if(Tks['classPart'][I] in Classdecl_sel):
        if(C_AM(Tks)):
            cat = Tks['ValuePart'][I-1]
            if(Tks['classPart'][I] == 'class'):
                Type = Tks['ValuePart'][I]
                I += 1
                if(Tks['classPart'][I] == 'ID'):
                    Name = Tks['ValuePart'][I]
                    I += 1
                    if(Tks['classPart'][I] == '('):
                        I += 1
                        if(Tks['classPart'][I] == ')'):
                            I += 1
                            if(inh(Tks)):
                                if (Tks['classPart'][I-2] == 'extends'):
                                    parent = Tks['ValuePart'][I-1]

                                    #lookup MT for class name
                                    lookupmtres = LookUp_MT(Name)
                                    if lookupmtres == NULL:
                                        #lookup MT
                                        mtlookup = LookUp_MT(parent)
                                        if mtlookup == NULL:
                                            print("Undeclared parent")
                                            exit()
                                        elif mtlookup.type != 'class':
                                            print("Cant be extended")
                                            exit()
                                        else:
                                            pass
                                    else:
                                        print("Redeclaration Error")
                                        quit()

                                    
                                else:
                                    parent = ""
                                
                                #insert mt
                                if (Insert_MT(Name, Type, cat, parent) == True):
                                    pass
                                else:
                                    print("Redeclaration")
                                    
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
            Create_Scope()
            if(C_MST(Tks)):
                if(Tks['classPart'][I] == '}'):
                    I+= 1
                    Delete_Scope()
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
    global class_ref

    C_Decl_sel = ['def', 'ID', 'int', 'string', 'char',
                  'float', 'bool', 'public', 'private', 'protected', '}']
    if(Tks['classPart'][I] in C_Decl_sel):
        if(AM(Tks)):
            try:
                cat = Tks['ValuePart'][I-1]
            except:
                cat = ''
            if(DT(Tks)):
                D_T = Tks['ValuePart'][I-1]
                if(Tks['classPart'][I] == 'ID'):            
                    Name = Tks['ValuePart'][I]
                    I += 1
                    
                    #lookup AT
                    if (LookUp_AT_V(Name, class_ref) == NULL):
                        pass
                    else:
                        print("Redeclaration rror")
                        quit()

                    if(List(Tks)):
                        #insert AT
                        try:
                            Insert_AT(Name, D_T, cat, class_ref)
                        except:
                            print("Redeclaration Error")
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


def Semantic_Analyzer(Tokens):
    Tks = pd.DataFrame(Tokens)
    global I
    if Start(Tks):
        print("Valid Syntax \n")
    else:
        print("Sytax Error at Line Number", Tks['LineNo'][I])

    print("Main Table Entries")
    for i in range(len(MT)):
        print("\nClass Name :",MT[i].name)
        print("Class Type :",MT[i].type)
        print("Class Category :",MT[i].category)
        print("Class Parent :",MT[i].parent)

    print("\nAttribute Tables Entries:")
    for key in AT.keys():

        print("\nName :",AT[key][0].name)
        print("Class Name :",AT[key][0].classname)