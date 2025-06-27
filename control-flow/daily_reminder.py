task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print(f"'{task}' is a high priority task that requires immediate attention today!")
    case "medium":
        print(f"'{task}' is a medium priority task. Consider completing it soon.") 
    case "low":
        print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Invalid priority level: '{priority}'. Please use high/medium/low.")
if time_bound == "yes":
    print(f"'{task}' is time-bound. Consider completing it while you still have time.")
elif time_bound !="no":
    print(f"Invalid time-bound response: '{time_bound}' Please use yes/no.")
    