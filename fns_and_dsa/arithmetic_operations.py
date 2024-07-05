def perform_operation(num1,num2,operation):
  
  match operation:
    case'+':
        res = first + second
    case'-':
        res = first - second    
    case'*':
        res = first * second
    case'/':
        if second == 0:
            print("Cannot divide by zero.")
        else:
            res = first / second
  return res
