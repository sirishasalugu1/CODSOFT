from tkinter import *
import random
def play_game(user_choice):
    choices = ["rock","paper","scissors"]
    computer_choice = random.choice(choices) 
    label2.config(text="Computer choose: " + computer_choice)
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            result = "YaY You Win!"
        else:
            result = "Computer wins!"
    elif user_choice == "paper":
        if computer_choice == "rock":
            result = "YaY You Win!"
        else:
            result = "Computer wins!"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            result = "YaY You Win!"
        else:
           result = "Computer wins!"
    label3.config(text=result)
    play_again_button.pack()
def play_again():
    label2.config(text="")
    label3.config(text="")
    play_again_button.pack_forget()
root = Tk()
root.title("Rock Paper Scissors Game")
label = Label(root, text="Choose:")
label.pack()
button1 = Button(root, text="rock", command=lambda: play_game("rock"))
button1.pack(side="left")
button2 = Button(root, text="paper", command=lambda: play_game("paper"))
button2.pack(side="right")
button3 = Button(root, text="scissors", command=lambda: play_game("scissors"))
button3.pack(side="top")
label2 = Label(root, text="")
label2.pack()
label3 = Label(root, text="")
label3.pack()
play_again_button = Button(root, text="Play Again", command=play_again)
root.mainloop()