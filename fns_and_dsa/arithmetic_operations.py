def perform_operation(num1, num2, operation):
  
  match operation:
    case'+':
        res = num1 + num2
    case'-':
        res = num1 - num2    
    case'*':
        res = num1 * num2
    case'/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            res = num1 / num2
  return res
