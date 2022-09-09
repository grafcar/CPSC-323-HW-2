def parsec (value):
    value.strip()
    value = value[:len(value)-2]
    value = value.split(" ")
    return value

def key(value):
    result = []
    i = 0
    while (len(value) > i):
        temp = input()
        result.append(temp)
        i += 1
    return result

def isNum(value):
    if type(value) == int:
        return True
    elif type(value) == float:
        return True
    elif value[0] == "1" or value[0] == "2" or value[0] == "3" or value[0] == "4" or value[0] == "5" or value[0] == "6" or value[0] == "7" or value[0] == "8" or value[0] == "9" or value[0] == "0":    
        return True
    else:
        return False

def isOperand(value):
    if value == "*" or value == "+" or value == "-" or value == "/":
        return True
    else:
        return False

#calculates x and y with the current operand, converts x and y from string to int when returning
def calculate(x,y, operand):
    if isNum(operand):
        return
    if operand == "*":
        return float(x)*float(y)
    elif operand == "-":
        return float(x)-float(y)
    elif operand == "+":
        return float(x)+float(y)
    elif operand == "/":
        return float(x)/float(y)
    else:
        print("There was an error with the calculation, please ensure the numbers and operands are correct") #if ends up with more number/operands than its counter part
        return 

def var(value):
    list = []
    i = 0
    while(len(value) > i):
        if not isNum(value[i]) and not isOperand(value[i]):
            list.append(value[i])
        i += 1
    return list

def varOp(value, ans):
    list = []
    i = 0
    j = 0
    while(len(value) > i):
        if not isNum(value[i]) and not isOperand(value[i]):
            list.append(ans[j])
            j += 1
            i += 1
        else:
            list.append(value[i])
            i += 1
    return list

operation = input("Please enter your numbers and operators in postfix. When done enter $\n")

#if the input does not end in $ ask for the input again
while operation[len(operation)-1] != "$":
    operation = input("Remember to type $ at the end. Please enter your values again:\n")

#starting values
value = 0
operation = parsec(operation)
variable = var(operation)
variable = key(variable)
operation = varOp(operation, variable)
index = 0 
cont = True
result = True

#at the end of the calculation a question will be asked if cont, if input is 'y' then cont = true
while cont:
    #if the list of strings is less than 3, end loop
    while len(operation) >= 3:
        #if first 2 items of the list are numbers AND the third is an operand
        if isNum(operation[index]) and isNum(operation[index+1]) and isOperand(operation[index+2]):
            value = calculate(operation[index], operation[index+1], operation[index+2])
            operation = operation[:index] + operation[index+3:] #deletes the current 3 items of the index
            operation.insert(index,value) #inserts the new item on the index
            index = 0
        else:
            index += 1 #increment index value

    if result: print("Your result is: ", value)
    ans = input("Would you like to continue: y/n\n")
    if ans == "y":
        cont = True
        operation = input("Please enter your numbers and operators in postfix. When done enter $\n")

        while operation[len(operation)-1] != "$":
            operation = input("Remember to type $ at the end. Please enter your values again:\n")

        value = 0
        operation = parsec(operation)
        index = 0
        result = True
    elif ans == "n":
        cont = False
    else:
        result = False
        print("Please enter a valid character!")
