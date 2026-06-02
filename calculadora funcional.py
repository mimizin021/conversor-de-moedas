num1 = float(input('digite um numero'))
operacao = input('digite o operador')
num2 = float(input('digite o proximo numero'))

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
else:
    resultado = 'operador inválido'

print('O resultado é:', resultado)