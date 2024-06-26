first = int (input("Enter the first number:"))
second = int(input("Enter the second number:"))
operations = input("Choose the operation (+, -, *, /):")
match operations:
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
print("The result is",res)
