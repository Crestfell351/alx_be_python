task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound =input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        print(f"Reminder: {task} is a high priority task ", end="")
        if time_bound == "yes":
            print(f"that requires immediate attention today!")
    case "medium":
        print(f"Note: {task} is a medium priority task ", end="")
        if time_bound == "yes":
            print(f"that requires immediate attention today!")
    case "low":
        print(f"Note: {task} is a low priority task ", end="")
        if time_bound == "yes":
            print(f"that requires immediate attention today!")
