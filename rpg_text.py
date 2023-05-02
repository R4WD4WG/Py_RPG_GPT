import tkinter as tk
from functools import partial

player_name = ""

# Ask Question function
def ask_question(prompt, callback):
    display_message(prompt)
    button.config(command=lambda: submit_message(callback))

# Submit Message function
def submit_message(callback=None):
    message = text_box2.get("1.0", "end-1c").strip()
    text_box2.delete("1.0", "end")
    
    if message and callback:
        callback(message)

# Display Message function
def display_message(message):
    text_box1.config(state="normal")
    text_box1.insert("end", message + "\n")
    text_box1.config(state="disabled")
    text_box1.yview("end")

def set_player_name():
    global player_name
    player_name = text_box2.get("1.0", "end").strip().capitalize()
    text_box2.delete("1.0", "end")
    display_message("Welcome to the game, " + player_name + "!")
    start_game_intro()

def handle_game_choice(choice):
    if choice == "1":
        display_message("You chose to explore the world.")
    elif choice == "2":
        display_message("You decided to join the adventurer's guild.")
    elif choice == "3":
        display_message("You went to study at the magic academy.")
    else:
        display_message("Invalid choice. Please try again.")
        start_game_intro()

def start_game_intro():
    display_message("You find yourself at a crossroads. What will you do?")
    display_message("1. Explore the world")
    display_message("2. Join the adventurer's guild")
    display_message("3. Study at the magic academy")
    ask_question("Enter the number corresponding to your choice:", handle_game_choice)

root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)

text_box1 = tk.Text(root, height=int(0.75 * 600 / 17), state="disabled")
text_box1.pack(fill="both", padx=5, pady=5)

text_box2 = tk.Text(root, height=int(0.25 * 600 / 17), width=int(0.75 * 800 / 8))
text_box2.pack(side="left", fill="both", expand=True, padx=5, pady=5)
text_box2.bind('<Return>', lambda event: submit_message())

button = tk.Button(root, text="Submit", height=int(0.25 * 600 / 17), width=int(0.25 * 800 / 8), command=set_player_name)
button.pack(side="right", padx=5, pady=5)

display_message("Welcome to the game!")
display_message("What is your name?")
display_message("Enter your name below and press submit to begin.")

root.mainloop()
