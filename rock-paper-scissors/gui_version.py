import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import random

# sakht panjere
window = tk.Tk()
#title panjere
window.title("Rock Paper Scissors")
#andaze panjere
window.geometry("500x550")

# panjere pop up dorost mishe ke beporse chand rond mikhy bazi koni?
rounds_total = simpledialog.askinteger("Rounds", "How many rounds do you want to play?")
current_round = 0
# tarif maghadir
choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

#aksa amadei ke gozashtm
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))

images = {
    'rock': rock_img,
    'paper': paper_img,
    'scissors': scissors_img
}

#ghiafe zaheri mesl font 
tk.Label(window, text="You", font=("Arial", 12, "bold")).pack()
user_img_label = tk.Label(window)
user_img_label.pack(pady=5)

tk.Label(window, text="Computer", font=("Arial", 12, "bold")).pack()
computer_img_label = tk.Label(window)
computer_img_label.pack(pady=5)

# namayesh natije 
result_label = tk.Label(window, text="Choose rock, paper or scissors!", font=("Arial", 14))
result_label.pack(pady=10)

score_label = tk.Label(window, text="You: 0  |  Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

round_label = tk.Label(window, text=f"Round: 0 / {rounds_total}", font=("Arial", 11))
round_label.pack(pady=5)

# tavabe bazi ghesmat logical
def play(user_choice):
    global user_score, computer_score, current_round

    if current_round >= rounds_total:
        return  #be rooz kardan etelat

    current_round += 1
    round_label.config(text=f"Round: {current_round} / {rounds_total}")

    computer_choice = random.choice(choices)

    user_img_label.config(image=images[user_choice])
    user_img_label.image = images[user_choice]

    computer_img_label.config(image=images[computer_choice])
    computer_img_label.image = images[computer_choice]

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win this round!"
        user_score += 1
    else:
        result = "Computer wins this round!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"You: {user_score}  |  Computer: {computer_score}")

    # akharin rand 
    if current_round == rounds_total:
        if user_score > computer_score:
            messagebox.showinfo("Game Over", "🎉 You won the game!")
        elif user_score < computer_score:
            messagebox.showinfo("Game Over", "💻 Computer won the game!")
        else:
            messagebox.showinfo("Game Over", "🤝 It's a draw!")

#dokme bazi ba zadan ro harkodom tavabe uno mizane 
btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", width=10, command=lambda: play('rock')).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play('paper')).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play('scissors')).grid(row=0, column=2, padx=5)

# ye loop grafigi vajebe ke bashe ta barname baste nashe 
window.mainloop()
