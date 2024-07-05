def perform_operation(num1, num2, operation):
  
  match operation:
    case'+':
        add = num1 + num2
        res = add 
    case'-':
        subtract = num1 - num2  
        res = subtract
    case'*':
        multiply = num1 * num2
        res = multiply 
    case'/':
        if num2 == 0:
            print("Cannot divide by zero.")
        elif num2 != 0:
            res = num1 / num2
  return res
