# Prompt for the task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
reminder = f"Reminder: '{task}' is a {priority} priority task"

match priority:
    case "high":
        reminder += " that requires immediate attention!"
        if time_bound == "yes":
            reminder += " It is time-sensitive and needs to be done today!"
    case "medium":
        reminder += ". Try to complete it soon."
        if time_bound == "yes":
            reminder += " It is time-sensitive and needs to be done today!"
    case "low":
        reminder += ". Consider completing it when you have free time."
        if time_bound == "yes":
            reminder += " It is time-sensitive and needs to be done today!"

# Provide a customized reminder
print(reminder)
