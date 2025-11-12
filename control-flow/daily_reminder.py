
Task=input("Enter a task: ")
Priority=input("Priority (high/medium/low)")
Time_Bound=input("Is it time bound? (yes/no)")
match Priority:
    case "high":
        if Time_Bound=="yes":
            print(f"'{Task}' is a high priority task that requires immediate attention today!")
        elif Time_Bound=="no":
            print(f"'{Task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if Time_Bound=="yes":
            print(f"'{Task}' is a medium priority task that requires some attention today!")
        elif Time_Bound=="no":
            print(f"'{Task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if Time_Bound=="yes":
            print(f"'{Task}' is a low priority task. Consider completing it when you have free time.")
        if Time_Bound=="no":
            print(f"'{Task}' is a low priority task. Consider completing it when you have free time.")