instructionSet = {
    'SHUF':'00', 'LOAD':'01',
    'PW1':'02', 'PW2':'03', 'DW':'04'
    }

OPCode = []


while(True):
    instruction = ["", ""]
    instruction = input().split()
    if(instruction[0] == "end"):
        break
    elif(instruction[0] not in instructionSet):
        print("Instruction \"", instruction[0], "\" not found.", sep="")
        data = ""
    else:
        OPCode.append(instructionSet[instruction[0]])
        OPCode.append(instruction[1])


for i in range(0, len(OPCode), 2):
    if i + 1 < len(OPCode):
        print(f"{OPCode[i]} {OPCode[i+1]}")
    else:
        print(f"{OPCode[i]} (data didn't found)")