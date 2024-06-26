size = int(input("Enter the size of the pattern:"))
counter = size
while counter>0:
    for i in range(size):
        print("*",end="")
    print("")
    counter=counter-1
