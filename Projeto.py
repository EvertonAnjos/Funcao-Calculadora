def calculadora(num1, num2, operação):
    if operação == 1:
        return num1 + num2
    elif operação == 2:
        return num1 - num2
    elif operação == 3:
        return num1 / num2
    elif operação == 4:
        return num1 * num2
    else:
        print(0)
# teste da função:
               
print(calculadora(2,3,3))