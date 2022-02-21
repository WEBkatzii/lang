import os

code = ""
varlist = []
functionlist = []

def var(code, varlist, funclist, codelist):
    varlist.append(code[4:])
    print(f"declared var{len(varlist)-1}: {varlist[len(varlist)-1]}")

def out(code, varlist, funclist, codelist):
    if code.find("out:var") == 0:
        semicolon = code.find(";")
        print(varlist[int(code[7:semicolon])])
    else:
        print(code[4:])

def stop(code, varlist, funclist, codelist):
    exit()

def free(code, varlist, funclist, codelist):
    os.system("clear")

def add(code, varlist, funclist, codelist):
    varlist[int(code[7:8])] = str(int(varlist[int(code[7:8])]) + int(code[9:]))

def get(code, varlist, funclist, codelist):
    varlist.append(input(code[3:]))
    print(f"declared var{len(varlist)-1}: {varlist[len(varlist)-1]}")

def interfunc(codelist, funclist, varlist, functionlist, functionlistcall):
    for line in len(functionlist[functionlistcall]):
        count += 1
        code = line.format(count, line)
        code =  code[0:-1]

        interprete(code, codelist, funclist, varlist)

# this function doesnt work
def func(varlist, funclist, codelist):
    if type(int(code[5:code.find(";")])) == int:
        print("intfunc no works")
        interfunc(codelist, funclist, varlist, functionlist, int(code[5:code.find(";")])) 
    else:
        functionlist.append([code[5:].split("°")])

def when(code, varlist, funclist, codelist):
    semicolon = code.find(";")
    if varlist[int(code[9:10])] == code[11:semicolon]:
        scode = code[(semicolon+1):len(code)]
        interprete(scode, codelist, funclist, varlist)
    elif code[-7:] == "counter":
        varlist[int(code[9:10])] = str(int(varlist[int(code[9:10])]) + 1)
        print(f"repeated {varlist[int(code[9:10])]}x")
        interprete(code, codelist, funclist, varlist)

def whennot(code, varlist, funclist, codelist):
    semicolon = code.find(";")
    if varlist[int(code[8:9])] != code[10:semicolon]:
        scode = code[(semicolon+1):len(code)]
        interprete(scode, codelist, funclist, varlist)

def comment(code, varlist, funclist, codelist):
    pass

codelist = ["var", "out", "stop", "free", "when", "add", "/", "in", "not", "func"]
funclist = [var, out, stop, free, when, add, comment, get, whennot, func]

filename = input("Filename:")
with open(filename,"r") as readfile:
    Lines = readfile.readlines()
count = 0

def interprete(code, codelist, funclist, varlist):
    semicolon = code.find(":")
    try:
        funcnum = codelist.index(code[:semicolon])
        if code[-5:-1] == "loop":
            for i in range(int(code[-1:])):
                funclist[funcnum](code[:-5], varlist, funclist, codelist)
        elif code[-8:-1] == "loopvar":
            for i in range(int(varlist[int(code[-1:])])):
                funclist[funcnum](code[:-8], varlist, funclist, codelist)
        else:
            funclist[funcnum](code, varlist, funclist, codelist)
    except:
        print(f"Error executing \"{code}\"")
        exit()

for line in Lines:
    count += 1
    code = line.format(count, line)
    code =  code[0:-1]

    interprete(code, codelist, funclist, varlist)