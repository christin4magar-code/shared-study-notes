# Semester Grade & Points Calculator
print("--- 🎓 Semester Points Calculator ---")

total_points = 0
target_points = 1000 # Example target for an A

while True:
    class_name = input("\nEnter Class Name (or 'exit' to finish): ")
    if class_name.lower() == 'exit':
        break
    
    points = float(input(f"How many points have you earned in {class_name}?: "))
    total_points += points
    
    print(f"Current Total: {total_points} points.")
    
    remaining = target_points - total_points
    if remaining > 0:
        print(f"You need {remaining} more points to hit your goal of {target_points}!")
    else:
        print("Congrats! You've hit your goal!")

print("\nStay focused and finish the semester strong!")
