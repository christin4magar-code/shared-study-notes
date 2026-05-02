# ✨ SEMESTER DAY PLANNER ✨
import datetime

# Get today's date automatically
today = datetime.date.today()

print(f"--- 📅 PLANNER FOR: {today} ---")
print("What are your top 3 missions for today?")

# Collect 3 goals from the user
missions = []
for i in range(1, 4):
    goal = input(f"Mission {i}: ")
    missions.append(goal)

# Print the final checklist
print("\n" + "="*30)
print("🚀 TODAY'S FOCUS LIST:")
for mission in missions:
    print(f"[ ] {mission}")
print("="*30)

print("\nStay focused and drink water! ☕✨")
