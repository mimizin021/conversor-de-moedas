num1=float(input('digite um numero'))
operador=input("digite o operador")
num2=float(input('digite o proximo numero'))


if operador== '+':
    resultado=num1+num2
elif operador== '-':
    resultado=num1-num2
elif operador=='*':
    resultado=num1*num2
elif operador=='/' or operador=='%':
    resultado=num1/num2
else: resultado='operador invalido'
print(resultado)