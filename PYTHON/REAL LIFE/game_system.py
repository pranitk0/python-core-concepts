print("Game Score System")

score = 0

score = int(input("Enter score earned in the game: "))

if score >= 100:
    print("Excellent! High Score 🎉")

elif score >= 50:
    print("Good Job 👍")

else:
    print("Keep Trying 💪")

print("Your Final Score:", score)
