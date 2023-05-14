# R4WD4WG on GitHub

import tkinter as tk, random

current_callback = None


###############################################################################################
### Game classes ##############################################################################
###############################################################################################


# Location class
class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
locations = {
    "location_1": Location("Forest", "You are in a forest. There are trees all around you."),
    "location_2": Location("Village", "A small village with friendly people."),
    "location_3": Location("Mountain", "You are at the base of a towering mountain range."),
    "location_4": Location("River", "A swift river courses through here."),
    "location_5": Location("Castle", "A majestic castle stands in the distance."),
}


# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.max_health = 100
        self.level = 1
        self.xp = 0
        self.xp_to_level = 100
        self.gold = 0
        self.equipment = {}
        self.equipment["head"] = None
        self.equipment["chest"] = None
        self.equipment["legs"] = None
        self.equipment["feet"] = None
        self.equipment["hands"] = None
        self.equipment["weapon"] = None
        self.equipment["shield"] = None
        self.equipment["ring"] = None
        self.equipment["amulet"] = None
        self.equipment["back"] = None
        self.equipment["belt"] = None
        self.equipment["trinket"] = None
        self.attack = 1
        self.defense = 1
        self.magic = 1
        self.speed = 1
        self.luck = 1
        self.hp = 10
        self.mp = 3
        self.skill_points = 0

    def add_item(self, item):
        if len(self.inventory) < 30:
            self.inventory.append(item)
        else:
            display_message("Your inventory is full!")
            display_message("Do you wish to drop something?")

    def remove_item(self, item):
        self.inventory.remove(item)


###############################################################################################
### Game utility functions ####################################################################
###############################################################################################


def ask_question(prompt, callback):
    global current_callback
    current_callback = callback
    display_message(prompt)
    button.config(command=lambda: submit_message(callback))

def submit_message(callback=None):
    global current_callback
    message = text_box2.get("1.0", "end-1c").strip()
    text_box2.delete("1.0", "end")
    
    if message and current_callback:
        current_callback(message)

def display_message(message):
    text_box1.config(state="normal")
    text_box1.insert("end", message + "\n")
    text_box1.config(state="disabled")
    text_box1.yview("end")


###############################################################################################
### Main game functions #######################################################################
###############################################################################################


def set_player_name(message=None):
    global player_name, current_callback
    
    def confirm_name(choice):
        if choice.lower() == "yes":
            display_message("Welcome to the game, " + player_name + "!")
            start_game_intro()
        elif choice.lower() == "no":
            display_message("Please enter your name again and press submit.")
            button.config(command=lambda: submit_message())  # Configure the button to call submit_message again
        else:
            display_message("Invalid choice. Please type 'yes' or 'no' and press submit.")
            ask_question("Is " + player_name + " your desired name? (yes/no):", confirm_name)

    if message is None:  # If message is None, it means the function was called as a callback without a message
        current_callback = set_player_name
        return

    player_name = message
    current_callback = confirm_name

    ask_question("Is " + player_name + " your desired name? (yes/no):", confirm_name)

def handle_game_choice(choice):
    if choice == "1":
        display_message("You chose to explore the world.")
        explore_world()
    elif choice == "2":
        display_message("You have decided to join the adventurer's guild.")
    elif choice == "3":
        display_message("You went to study at the magic academy.")
    else:
        display_message("Invalid choice. Please try again.")
        start_game_intro()

def handle_explore_choice(choice):
    if choice == "1":
        display_message("You decided to explore further.")
        explore_world()  # Call explore_world again to go to a new location
    elif choice == "2":
        display_message("You have decided to rest for a while.")
        # Maybe add some code here to restore the player's health or other stats
    elif choice == "3":
        display_message("You have decided to return to the crossroads.")
        start_game_intro()
    else:
        display_message("Invalid choice. Please try again.")
        explore_world()  # Ask the question again

def explore_world():
    # Randomly select a location
    location_key = random.choice(list(locations.keys()))
    location = locations[location_key]

    # Display the location's name and description
    display_message("You have arrived at a new location: " + location.name)
    display_message(location.description)

    # Ask the player what they want to do
    display_message("What would you like to do?")
    display_message("1. Explore further")
    display_message("2. Rest for a while")
    display_message("3. Return to the crossroads")
    ask_question("Enter the number corresponding to your choice:", handle_explore_choice)

def handle_game_choice(choice):
    if choice == "1":
        display_message("You chose to explore the world.")
        explore_world()
    elif choice == "2":
        display_message("You have decided to join the adventurer's guild.")
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


###############################################################################################
### Tkinter Window Intialize ##################################################################
###############################################################################################


# Create the main window
root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)

# Bind the Enter/Return key to the submit_message function
root.bind("<Return>", lambda event=None: submit_message())

# Create the read-only text box taking up 75% of the screen height and 100% width, anchored North
text_box1 = tk.Text(root, height=int(0.75 * 600 / 17), state="disabled")
text_box1.pack(fill="both", padx=5, pady=5)

# Create a frame to hold the input text box and the button
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)

# Create the input text box taking up 25% of the screen height, 75% of the width, anchored South West
text_box2 = tk.Text(bottom_frame, height=int(0.25 * 600 / 17), width=int(0.75 * 800 / 8))
text_box2.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Create the button taking up 25% of the screen height, 25% of the width, anchored South East
button = tk.Button(bottom_frame, text="Submit", height=int(0.25 * 600 / 17), width=int(0.25 * 800 / 8), command=lambda: submit_message(set_player_name))
button.pack(side="right", padx=5, pady=5)

# Initialize game
player_name = ""
hero = Player("Hero")
display_message("Welcome to the game!")
display_message("What is your name?")
display_message("Enter your name below and press submit to begin.")
current_callback = set_player_name

# Run the main loop
root.mainloop()
