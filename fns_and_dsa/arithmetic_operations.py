def perform_operation(num1, num2, operation):
  
  match operation:
    case'+':
        add = num1 + num2
        res = add 
    case'-':
        subract = num1 - num2  
        res = subract
    case'*':
        multiply = num1 * num2
        res = multiply 
    case'/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            res = num1 / num2
  return res
