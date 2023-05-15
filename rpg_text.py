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
    "childhood_small_village": Location("Small Village", "Small Village"),
    "childhood_capital": Location("Capital", "Capital"),
    "childhood_wolves": Location("Wolves", "Wolves"),
    "childhood_slums": Location("Slums", "Slums"),
    "childhood_wealthy": Location("Wealthy", "Wealthy"),
    "childhood_royalty": Location("Royalty", "Royalty"),
    "childhood_monks": Location("Monks", "Monks"),
    "childhood_clowns": Location("Clowns", "Clowns"),
    "childhood_brothel": Location("Brothel", "Brothel"),
    "childhood_prison": Location("Prison", "Prison"),
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
        self.charisma = 1
        self.stealth = 1
        self.hp = 10
        self.mp = 3
        self.skill_points = 0
        self.role = None # warrior, mage, rogue, bard, beastmaster
        hero.background = None # childhood background, determines starting location

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


# assign skill points function
def assign_skill_points():
    display_message("You have " + str(hero.skill_points) + " skill points to assign.")
    display_message("Your current stats are:")
    display_message("Attack: " + str(hero.attack))
    display_message("Defense: " + str(hero.defense))
    display_message("Magic: " + str(hero.magic))
    display_message("Speed: " + str(hero.speed))
    display_message("Luck: " + str(hero.luck))
    display_message("Charisma: " + str(hero.charisma))
    display_message("Stealth: " + str(hero.stealth))
    display_message("HP: " + str(hero.hp))
    display_message("MP: " + str(hero.mp))
    while hero.skill_points > 0:
        display_message("Which skill would you like to increase?")
        display_message("1. Attack")
        display_message("2. Defense")
        display_message("3. Magic")
        display_message("4. Speed")
        display_message("5. Luck")
        display_message("6. Charisma")
        display_message("7. Stealth")
        display_message("8. HP")
        display_message("9. MP")
    
    display_message("You have no more skill points to assign.")
    display_message("You are level " + str(hero.level) + " & your stats are:")
    display_message("Attack: " + str(hero.attack))
    display_message("Defense: " + str(hero.defense))
    display_message("Magic: " + str(hero.magic))
    display_message("Speed: " + str(hero.speed))
    display_message("Luck: " + str(hero.luck))
    display_message("Charisma: " + str(hero.charisma))
    display_message("Stealth: " + str(hero.stealth))
    display_message("HP: " + str(hero.hp))
    display_message("MP: " + str(hero.mp))


# calculates XP needed for each level (level 100 cap)
# Makes XP needed for each level to be 100 times the square of the level.
# Example: Reaching level 2 would require 200 XP, level 3 requires 900 XP & level 4 requires 1600 XP.
# By level 100, the player needs to accumulate 1,000,000 XP to level up.
def xp_for_level(level):
    return 100 * level**2


# Recursive Level Up Function
def level_up(hero):
    if xp_for_level(hero.level + 1) <= hero.xp:
        old_xp = xp_for_level(hero.level)
        hero.level += 1
        hero.xp -= old_xp
        level_up(hero)  # Check if the hero can level up again
    hero.skill_points += 3
    assign_skill_points()



# xp gain function
def xp_gain(xp):
    hero.xp += xp
    level_up(hero.level)



###############################################################################################
### Main game functions #######################################################################
###############################################################################################



# Set player name function
def set_player_name(message=None):
    global player_name, current_callback
    
    # confirm player name function
    def confirm_name(choice):
        if choice.lower() == "yes":
            display_message("Welcome to the game, " + player_name + "!")
            start_game_intro()
        elif choice.lower() == "no":
            display_message("Please enter your name again and press submit.")
            button.config(command=lambda: submit_message(set_player_name))  # Configure the button to call submit_message again
        else:
            display_message("Invalid choice. Please type 'yes' or 'no' and press submit.")
            ask_question("Is " + player_name + " your desired name? (yes/no):", confirm_name)

    if message is None:  # If message is None, it means the function was called as a callback without a message
        current_callback = set_player_name
    else:
        player_name = message
        current_callback = confirm_name
        ask_question("Is " + player_name + " your desired name? (yes/no)", confirm_name)





# Confirms starting location
def start_location(choice):
    def confirm_start_location(choice):
        if choice.lower() == "yes":
            pass
        ### TO CONTINUE ###

    if choice == 1:
        hero.background = "Small Village"
        display_message("You grew up in a small village?")
        ask_question("Is this correct? (yes/no):", confirm_start_location)
    elif choice == 2:
        hero.background = "Kingdom's Capital"
        display_message("You grew up in the kingdom's capital?")
        ask_question("Is this correct? (yes/no):", confirm_start_location)
    elif choice == 3:
        hero.background = "Raised by Wolves"
        display_message("You were raised by wolves, you grew up in the forest?")
        ask_question("Is this correct? (yes/no):", confirm_start_location)
    elif choice == 4:
        hero.background = "Slums"
        display_message("You grew up in poverty in the slums?")
        ask_question("Is this correct? (yes/no):", confirm_start_location)
    elif choice == 5:
        hero.background = "Wealthy Family"
        display_message("You grew up in a wealthy family?")
        ask_question("Is this correct? (yes/no):", confirm_start_location)
    elif choice == 6:
        hero.background = "Royalty"
        display_message("You come from royalty?")
        ask_question("Is this correct? (yes/no):", confirm_start_location)
    elif choice == 7:
        hero.background = "Raised by Monks"
        display_message("You were raised by monks after your parents abandoned you?")
        ask_question("Is this correct? (yes/no):", confirm_start_location)
    elif choice == 8:
        hero.background = "Traveling Circus"
        display_message("Your parents were traveling clowns, you grew up on the road circus show?")
        ask_question("Is this correct? (yes/no):", confirm_start_location)
    elif choice == 9:
        hero.background = "Raised by prostitutes"
        display_message("You grew up in a brothel?")
        ask_question("Is this correct? (yes/no):", confirm_start_location)
    elif choice == 10:
        hero.background = "Prison"
        display_message("You grew up in a prison?")
        ask_question("Is this correct? (yes/no):", confirm_start_location)
    else:
        display_message("Invalid choice. Please choose a number between 1 and 10.")
        choose_start()


# Set starting location
def choose_start():
    hero.background = None
    display_message("What was your childhood like?")
    display_message("1. You grew up in a small village.")
    display_message("2. You grew up in the kingdom's capital.")
    display_message("3. You were raised by wolves, you grew up in the forest.")
    display_message("4. You grew up in poverty in the slums.")
    display_message("5. You grew up in a wealthy family.")
    display_message("6. You come from royalty.")
    display_message("7. You were raised by monks after your parents abandoned you.")
    display_message("8. Your parents were traveling clowns, you grew up on the road circus show.")
    display_message("9. You grew up in a brothel.")
    display_message("10. You grew up in a prison.")
    ask_question("So, do any of these describe your childhood?", start_location())


# Increase class base stats function
def class_stats():
    def read_stats():
        display_message("You are a " + str(hero.role))
        display_message("Your starting stats are: ")
        display_message("Attack: " + str(hero.attack))
        display_message("Defense: " + str(hero.defense))
        display_message("Health Points: " + str(hero.hp))
        display_message("Speed: " + str(hero.speed))
        display_message("Luck: " + str(hero.luck))
        display_message("Charisma: " + str(hero.charisma))
        display_message("Stealth: " + str(hero.stealth))
        display_message("Magic: " + str(hero.magic))
        display_message("Mana: " + str(hero.mp))
        display_message("Skill Points to Assign: " + str(hero.skill_points))
        display_message("You gain skill points every time you level.")

    if hero.role == 'warrior':
        hero.attack = 5
        hero.defense = 5
        hero.hp += 5
        hero.speed = 3
        hero.luck = 3
        read_stats()
    elif hero.role == 'mage':
        hero.magic = 5
        hero.mp += 2
        hero.luck = 3
        hero.charisma = 2
        read_stats()
    elif hero.role == 'rogue':
        hero.speed = 5
        hero.stealth = 5
        hero.luck = 4
        hero.attack = 3
        hero.charisma = 3
        read_stats()
    elif hero.role == 'bard':
        hero.magic = 5
        hero.mp += 2
        hero.charisma = 5
        hero.speed = 3
        hero.luck = 3
        hero.hp += 2
        read_stats()
    elif hero.role == 'beastmaster':
        hero.attack = 5
        hero.charisma = 5
        hero.hp += 3
        hero.speed = 3
        hero.defense = 3
        read_stats()
    else:
        submit_message("How did you get here?")


# Confirm class choice function
def handle_class_choice(choice):
    def confirm_choice(choice):
        if choice.lower() == 'yes':
            class_stats()
        elif choice.lower() == 'no':
            start_game_intro()
        else:
            ask_question("Invalid choice. Please try again.", confirm_choice) # Add the missing callback function

    if choice == "1":
        hero.role = "warrior"
        ask_question("You are a warrior? (yes/no)", confirm_choice)
    elif choice == "2":
        hero.role = "mage"
        ask_question("You are a mage? (yes/no)", confirm_choice)
    elif choice == "3":
        hero.role = "rogue"
        ask_question("You are a rogue? (yes/no)", confirm_choice)
    elif choice == "4":
        hero.role = "bard"
        ask_question("You are a bard? (yes/no)", confirm_choice)
    elif choice == "5":
        hero.role = "beastmaster"
        ask_question("You are a beastmaster? (yes/no)", confirm_choice)
    else:
        ask_question("Invalid choice. Please try again.", confirm_choice) # Add the missing callback function


# Choose class function
def start_game_intro():
    hero.role = None
    display_message("What is your class?")
    display_message("1. Warrior")
    display_message("2. Mage")
    display_message("3. Rogue")
    display_message("4. Bard")
    display_message("5. Beastmaster")
    ask_question("Enter the number corresponding to your choice:", handle_class_choice)




###############################################################################################
### Tkinter Window Intialize ##################################################################
###############################################################################################



# Create the main window
root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Text Adventure Game")


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
