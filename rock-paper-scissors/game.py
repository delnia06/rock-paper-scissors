# entekhab random 
import random

choices = ['rock', 'paper', 'scissors']


user_score = 0
#emtiaz karbar save mikone az 0 shoro mishe 
computer_score = 0
#inm baraye computer
rounds = int(input("How many rounds do you want to play? "))
#tetad dafat bazi miporse

#halghe for az 0 ta add rand-1
for i in range(rounds):
    print(f"\n--- Round {i+1} ---")
    user_choice = input("Choose one (rock, paper, scissors): ").lower()
#lower agar ba horof bozorg type beshe kochik mikone khodkar
    if user_choice not in choices:
        print("Invalid choice! Round skipped.")
        continue
#agar entekhab karbar eshtebah bud ghabul nakon 
    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
#entekhab tasadofi computer
    if user_choice == computer_choice:
        print("It's a tie! 😐")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win this round! 😎")
        user_score += 1
    else:
        print("Computer wins this round! 😢")
        computer_score += 1


print("\n=== Game Over ===")
print(f"Your score: {user_score}")
print(f"Computer score: {computer_score}")
#ghanun haye sang kaghaz gheychi 
#neshun dadn be che natijei
if user_score > computer_score:
    print("🎉 You won the game!")
elif user_score < computer_score:
    print("💻 Computer won the game!")
else:
    print("🤝 It's a draw!")
