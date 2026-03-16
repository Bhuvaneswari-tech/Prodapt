#eval(expression, globals=None, locals=None)
'''
expression → String containing a Python expression
globals → Optional dictionary for global variables
locals → Optional dictionary for local variables
'''

x = 5
y = 3
print(eval('x+1'))

expression = '2 + 3 * 4'
result = eval(expression)
print(f"The result of the expression '{expression}' is: {result}")

num1 = input()
num2 = input()
operand = input()
result = eval(num1 + operand + num2) #eval(2 + '+' + 3) -> eval('2+3') -> 5
print(f"The result of {num1} {operand} {num2} is: {result}")

expression = "x+y"
result = eval(expression, globals(),locals={"y": 20})

#result = eval(expression, globals(),{"y": 20})

print(f"The result of the expression '{expression}' is: {result}")