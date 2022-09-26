import sys
import ListStack
         
def iterateExpression():
    # loop through the expression and evaulate utlizing a stack
    expression = sys.argv[1]
    expStack = ListStack()

    operater = '+', '-', '/', '*'
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
                if(not expStack.__is_empty__() and (expStack.peep() == '*' or expStack.peep() == '/')):
                    # evaluate and push back on the stack
                    operator = expStack.pop()
                    leftOperand = expStack.pop()
                    expStack.push(evaluate(leftOperand, operator, num))
                else:
                    # push onto the stack but don't evaluate yet
                    expStack.push(num)
                
                # reset num
                num = ''

        elif character in operater:
            expStack.push(character)

        elif character in whitespace:
            # skip over all whitespace
            continue

        else:
            # invalid character in the expression
            raise Exception('Invalid character in expression')

    while expStack.size() > 1:
        rightOperand = expStack.pop()
        operator = expStack.pop()
        leftOperand = expStack.pop()
        expStack.push(evaluate(leftOperand, operator, rightOperand))

    # last element in the stack should be the answer
    return expStack.pop()

def evaluate(leftOperand, operator, rightOperand):
    # make sure they are casted as numbers
    leftOperand = float(leftOperand)
    rightOperand = float(rightOperand)
    
    if operator == '+':
        return leftOperand + rightOperand
    elif operator == '-':
        return leftOperand - rightOperand
    elif operator == '*':
        return leftOperand * rightOperand
    elif operator == '/':
        return leftOperand / rightOperand
    else:
        # unknown operator
        raise Exception('invalid character in expression')

print(iterateExpression())