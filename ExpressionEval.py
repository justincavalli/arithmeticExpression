# Name: Justin Cavalli
# Date: last edit 9/27/2022
# Description: This program uses the previously implemented ListStack
#              to evaluate arithmetic expressions

import sys
import ListStack
         
def iterateExpression():
    # loop through the expression and evaulate utlizing a stack
    expression = sys.argv[1]
    expStack = ListStack.ListStack()

    operators = '+', '-', '/', '*'
    digits = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    whitespace = ' ', '\n', '\t'

    num = ''    # keeps track of the digits in an operand

    for index in range(len(expression)):
        
        character = expression[index]
        if character in digits:
            # add the digit to the current string of digits being tracked
            num+= character

            # check if it's the last digit in the current number
            if(index + 1 == len(expression) or expression[index+1] not in digits):
                # push the number or evaluate now if the operator is *, /
                if(not expStack.is_empty() and (expStack.peep() == '*' or expStack.peep() == '/')):
                    # evaluate and push back on the stack
                    operator = expStack.pop()
                    leftOperand = expStack.pop()
                    expStack.push(evaluate(leftOperand, operator, num))
                else:
                    # push onto the stack but don't evaluate yet
                    expStack.push(num)
                
                # reset num
                num = ''

        elif character in operators:

            # special case for '-' to distinguish if a negative sign or operator
            if character == '-' and (expStack.is_empty() or expStack.peep() in operators):
                # assume it is a negative sign if it comes after an operator or is at the start of the expression
                num += character
                continue

            expStack.push(character)

        elif character in whitespace:
            # skip over all whitespace
            continue

        else:
            # invalid character in the expression
            raise Exception('Invalid character in expression')

    # stack now needs to be reversed to evaluate left to right
    newStack = ListStack.ListStack()

    while not expStack.is_empty():
        newStack.push(expStack.pop())

    while newStack.size() > 1:
        leftOperand = newStack.pop()
        operator = newStack.pop()
        rightOperand = newStack.pop()
        newStack.push(evaluate(leftOperand, operator, rightOperand))

    # last element in the stack should be the answer
    return newStack.pop()

def evaluate(leftOperand, operator, rightOperand):
    # cast as numbers, if an exception occurs, the expression must be invalid
    try:
        leftOperand = float(leftOperand)
        rightOperand = float(rightOperand)
    except:
        raise Exception('invalid expression')

    if operator == '+':
        return leftOperand + rightOperand
    elif operator == '-':
        return leftOperand - rightOperand
    elif operator == '*':
        return leftOperand * rightOperand
    elif operator == '/':
        if rightOperand == 0:
            raise Exception('cannot divide by 0')
        return leftOperand / rightOperand
    else:
        # unknown operator
        raise Exception('invalid character in expression')

print(iterateExpression())