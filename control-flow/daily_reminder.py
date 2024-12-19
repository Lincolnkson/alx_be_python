# Prompt the user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task using a Match Case statement
match priority:
    case "high":
        priority_message = f"'{task}' is a high priority task."
    case "medium":
        priority_message = f"'{task}' is a medium priority task."
    case "low":
        priority_message = f"'{task}' is a low priority task."
    case _:
        priority_message = f"'{task}' has an undefined priority level. Please double-check."

# Add time-sensitivity information using an if statement
if time_bound == "yes":
    time_message = " It requires immediate attention today!"
else:
    time_message = " Consider completing it when you have free time."

# Combine messages and print the reminder
reminder = priority_message + time_message

print(f"Reminder:", reminder)