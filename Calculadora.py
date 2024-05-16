def main():  
    print("Calculadora!")  
  
    try:  
        num1 = float(input("Digite o primeiro número: "))  
        num2 = float(input("Digite o segundo número: "))  
  
        operation = input("Selecione uma das operações: (+, -, *, /): ")  
  
        if operation == '+':  
            result = num1 + num2  
        elif operation == '-':  
            result = num1 - num2  
        elif operation == '*':  
            result = num1 * num2  
        elif operation == '/':  
            result = num1 / num2  
        else:  
            print("Operação inválida")  
            return  
  
        print(f"O resultado é: {result}")  
  
    except ValueError:  
        print("Entrada inválida. Certifique-se de digitar números válidos.")  
  
if __name__ == "__main__":  
    main()  
