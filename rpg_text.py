# R4WD4WG on GitHub

import tkinter as tk

# Submit Message function
def submit_message():
    # Get the user input
    message = text_box2.get("1.0", "end-1c")

    # Clear the input text box
    text_box2.delete("1.0", "end")

    # Format the message with the player name
    formatted_message = "Player: " + message + "\n"

    # Enable the read-only text box to insert the message
    text_box1.config(state="normal")
    text_box1.insert("end", formatted_message)

    # Disable the read-only text box again
    text_box1.config(state="disabled")


# Display Message function
def display_message(message):
    formatted_message = message + "\n"

    # Enable the read-only text box to insert the message
    text_box1.config(stat="normal")
    text_box1.insert("end", formatted_message)

    # Disable the read-only text box again
    text_box1.config(state="disabled")


# Display Delayed Message function
def delayed_display_message(message, delay=1000):
    # Display the message after a delay
    root.after(delay, display_message, message)
    # Default is 1000ms (1 second)
    # Changeable when called


# Create the main window
root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)

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
button = tk.Button(bottom_frame, text="Submit", height=int(0.25 * 600 / 17), width=int(0.25 * 800 / 8), command=submit_message)
button.pack(side="right", padx=5, pady=5)

# Create the player class
class Player:
    # declares all player stats
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

    def attack(self, target):
        # Implement attack logic here
        None

    def defend(self):
        # Implement defend logic here
        None

    def use_item(self, item):
        # Implement use item logic here
        None

    def level_up(self):
        # Increase the player's level
        self.level += 1

    def add_item(self, item):
        # Check's if player's inventory is full (30 items)
        if len(self.inventory) < 30:
            self.inventory.append(item)
        else:
            display_message("Your inventory is full!")
            display_message("Do you wish to drop something?")

    def remove_item(self, item):
        # Removes an item from the player's inventory
        self.inventory.remove(item)

# Create the Location class
class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
# locations dictionary
locations = {
    "location_1": Location("Forest", "You are in a forest. There are trees all around you."),
    "location_2": Location("Village", "A small village with friendly people."),
    # Add more locations as needed
    }

hero = Player("Hero")
display_message("Welcome to the game!")
display_message("What is your name?")
display_message("Enter your name below and press submit to begin.")
submit_message()

# Run the main loop
root.mainloop()



