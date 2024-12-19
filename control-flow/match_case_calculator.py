#Declearing number variables
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Choosing math operator
operation = input("Choose the operation (+, -, *, /): ")

match operation:
          case "+":
                print(num1 + num2)
          case "-":
                print(num1 - num2)
          case "*":
              print(num1 * num2)
          case "/":
              if num2 != 0:
                    print(num1 / num2)
              else:
                    print("Cannot divide by zero.")


            