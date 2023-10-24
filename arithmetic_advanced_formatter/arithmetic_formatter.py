import regex as re

#problems = ['3801 - 2', '123 + 49']
def arithmetic_arranger(problems, ans=False):
    #thinking this of as 4 seperate lines where each word in that line
    #is seperated and so printed horizontally
    numerand_line = ''
    denom_line = ''
    result_line = ''
    lines = ''

    for element in problems:
        #print(element)
        #first error check
        if len(problems) > 5:
            return "Error: Too many problems."
        #second and third error check
        if re.search("[^\s0-9+-]",element):
            if re.search('[/]', element) or re.search('[*]', element):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        #taking apart the equation
        operand1 = element.split()[0]
        operand = element.split()[1]
        operand2 = element.split()[2]

        #fourth error check
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        #adding a max length so as to keep size of
        #output consistant
        if len(operand1) > len(operand2):
            length = len(operand1) + 2
        else:
            length = len(operand2) + 2

        #the computation of operation
        if operand == '+':
            result = int(operand1) + int(operand2)
        else:
            result = int(operand1) - int(operand2)
        #print(result)

        #These will be the individual words that are being added
        #into the lines
        numerand = operand1.rjust(length)
        denom = operand.rjust(length-5) + " " + operand2.rjust(length-2)
        result = str(result).rjust(length)
        line = ''.rjust(length-6)
        #     size = len(operand1) - 4
        #     for i in range(size):
        #         numerand += "      "
        # if len(operand2) <= 4:
        #     size = len(operand1) - 4
        #     for i in range(size):
        #         numerand += "     "

        for i in range(length):
            line += '-'

        #adding words to lines
        if element != problems[-1]:
            numerand_line += numerand + "    "
            denom_line += denom + "    "
            result_line += result + "    "
            lines += line + "    "
        else:
            numerand_line += numerand
            denom_line += denom
            result_line += result
            lines += line

    #the output format with option of
    #result showing
    if ans:
        output = numerand_line + '\n' + denom_line + '\n' + lines + '\n' + result_line
    else:
        output = numerand_line + '\n' + denom_line + '\n' + lines
    return output

#print(arithmetic_arranger(problems))