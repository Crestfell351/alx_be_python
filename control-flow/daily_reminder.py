task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = f"Reminder: '{task}' is a "

match priority:
    case "high":
        reminder = reminder + "high priority task"
        if time_bound == "yes":
                reminder = reminder + " that requires immediate attention today!"
        else:
            reminder = reminder + " that needs to be done soon."
    case "medium":
        reminder = reminder + "medium priority task"
        if time_bound == "yes":
            reminder = reminder + " that should be addressed today."
        else:
            reminder = reminder + " that you should complete soon."
    case "low":
        reminder = reminder + "low priority task"
        if time_bound == "yes":
            reminder = reminder + " but you have time to complete it."
        else:
            reminder = reminder + ". Consider completing it when you have free time."
print(reminder)
