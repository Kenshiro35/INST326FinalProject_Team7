import json
import random

class Create_your_own_Adventure_game:
    def __init__(self, gamestory_file):
        self.story = self.load_story(gamestory_file)
        self.player = {"name": "", "inventory": [], "attributes": {}}
        self.current_level = "start"
    

    def load_story(self, filepath):
        with open(filepath, "r") as gamestory_file: #used with statement method/function
            return json.load(gamestory_file)  #used json.load() method to load a json file 
    
    
    def display_current_level(self):
        level = self.story.get(self.current_level, None)
        if level:
            description, options = level.get("description", ""), level.get("options", [])
            print(description)
            for i, option in enumerate(options, start=1):  #conditional expression in sequence unpacking
                print(f"{i}. {option['text']}")
    

    def handle_player_choice(self, choice):
        level = self.story.get(self.current_level, None)
        if level:
            options = level.get("options", [])
            if 1 <= choice <= len(options):
                chosen_option = options[choice - 1]
                self.current_level = chosen_option.get("next_level", self.current_level)
                if "random_event" in chosen_option:
                    self.handle_random_event(chosen_option["random_event"])
            else:
                print("Not a possible choice, try again.")
        else:
            print("Gamecode is broken, invalid game state.")
    


    def handle_random_event(self, random_event):
        if random_event.get("type") == "dice_roll":
            sides = random_event.get("sides", 6)
            consequence = random.randint(1, sides)
            print(f"You roll a {sides}-sided dice and get a {consequence}.")





#example test #still incomplete 
adventure = Create_your_own_Adventure_game("LostintheJungle.json")

while adventure.current_level != "end":
    adventure.display_current_level()
    choice = int(input("Enter your choice: ")) - 1  #to match list index

    adventure.handle_player_choice(choice)

print("Yay, You managed to end your thrilling adventure.")


      
