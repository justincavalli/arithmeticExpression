import sys

class listStack():
    def __init__(self):
        # a python list stores the data in the stack
        self._stack = []

    def push(self, x):
        # pushes x in the stack
        self._stack.append(x)

    def pop(self):
        # pops i.e. removes the last element from the stack and returns it

        if(self.__is_empty__()):
            # error if the stack is empty
            raise Exception('the stack is empty')
        else:
            return self._stack.pop()


    def peep(self):
        # returns the latest element from the stack without removing it from the list

        if(self.__is_empty__()):
            # error if the stack is empty
            raise Exception('the stack is empty')
        else:
            return self._stack[self.size()-1]

    def size(self):
        # returns the size of the stack
        return len(self._stack)

    def __is_empty__(self):
        # returns true if the stack is empty
        return len(self._stack) == 0
         
def iterateExpression():
    # loop through the expression and evaulate utlizing a stack
    expression = sys.argv[1]
    expStack = listStack()

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
            if(index + 1 == len(expression) or [index+1] not in digits):
                # push the number or evaluate now if the operator is *, /
                if(expStack.peep() == '*' or expStack.peep() == '/'):
                    # evaluate and push back on the stack
                    operator = expStack.pop()
                    leftOperand = expStack.pop()
                    expStack.push(leftOperand, operator, num)
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

if __name__ == "__iterateExpression__":
    iterateExpression()