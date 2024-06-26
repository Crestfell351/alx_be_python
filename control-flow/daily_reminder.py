task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = f"Reminder: '{task}' is a "

match priority:
    case "high":
        reminder += "high priority task"
        if time_bound == "yes":
                reminder += " that requires immediate attention today!"
        else:
            reminder += " that needs to be done soon."
    case "medium":
        reminder += "medium priority task"
        if time_bound == "yes":
            reminder += " that should be addressed today."
        else:
            reminder += " that you should complete soon."
    case "low":
        reminder += "low priority task"
        if time_bound == "yes":
            reminder += " but you have time to complete it."
        else:
            reminder += ". Consider completing it when you have free time."
print(reminder)
