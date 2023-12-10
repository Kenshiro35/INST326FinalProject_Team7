import json

class Adventure:
    def __init__(self, story):
        """
        Initializes an Adventure instance with the provided story and sets the initial state.
        
        Parameters:
        - story (list): A list representing the story data.
        """
        self.story = story
        self.current_level = 1
        self.inventory = {'swords': 0, 'axes': 0}

    def display_current_level(self):
        """
        Displays the text of the current level in the story.
        """
        level = self.story[self.current_level - 1]
        print(level['text'])

    def get_user_choice(self):
        """
        Gets the user's choice as input and validates it.

        Returns:
            dict: A dictionary representing the loaded story data from the JSON file.
            
        """
        with open(filepath, "r") as gamestory_file: #used with statement method/function
            return json.load(gamestory_file)  #used json.load() method to load a json file 
    
    
    def display_current_level(self):
        """Display the description and options for the current ongoing level of the adventure game.
        If the current level exist in the loaded story, it prints the description and given options.
        
        
        """
        level = self.story.get(self.current_level, None)
        if level:
            description, options = level.get("description", ""), level.get("options", [])
            print(description)
            for i, option in enumerate(options, start=1):  #conditional expression in sequence unpacking
                print(f"{i}. {option['text']}")
    

    def handle_player_choice(self, choice):
        """Handles the player's choice in the adventure game. 
        Checks if the specified choice is valid for the current level, updates the game state, and handles random events associated.
        
        Args:
            choice (int): The player's chosen option (index) from the options available.
        
        
        """
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
        """Handle a random event in the adventure game.
        Currently supports dice roll events, Rolls a 6 sided dice and prints the according result.
        
        Args:
            random_event (dict): A dictionary representing the random event.
        
        
        """
        if random_event.get("type") == "dice_roll":
            sides = random_event.get("sides", 6)
            consequence = random.randint(1, sides)
            print(f"You roll a {sides}-sided dice and get a {consequence}.")


class Player:
    """ This is a player in the game.
    """
    def __init__(self, name):
        """Initialize the Player class.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.inventory = []
        
    def manage_inventory(self, item):
        """Add a new item to the inventory when the player picks something up.

        Args:
            item (str): A new item the player acquires. It could be a weapon, health item, armor, etc.
        
        Side Effects:
            The player will have the item in their inventory indefinitely.
        """
        self.inventory.append(item)
        print(f"{item} is now in {self.name}'s inventory.")
    
    def display_inventory(self):
        """Show the contents of the inventory to the player."""
        if not self.inventory:
            print(f"Hey, {self.name}, your inventory is empty.")
        else:
            print(f"{self.name}, here's what is in your inventory:")
            for item in self.inventory:
                print(item)              
            
    def count_items(self, item_name):
        """This will count the number of items with a specific name in the player's inventory.

        Args:
            item_name (str): The name of the item. A weapon, health item, clothing item, armor, etc.
        """
        items = [item for item in self.inventory if item['name'] == item_name]
        num_of_item = len(items) 
        print(f"Ok {self.name} you have {num_of_item} swords in your inventory.")

player = Player("LeBron")
player.manage_inventory({"name": "Axe", "Damage": 15})
player.display_inventory()
amount_of_axes = player.count_items("Axe")
print(f"Okay {player.name}, you have {amount_of_axes} axes in your inventory.")

sword = Weapon("Sword", 10)
shield = Weapon("Shield", 5)

#example test #still incomplete 
adventure = Create_your_own_Adventure_game("gamestory_file.json")

while adventure.current_level != "":
    adventure.display_current_level()
    choice = int(input("Enter your choice: ")) - 1  #to match list index

    adventure.handle_player_choice(choice)

print("Yay, You managed to end your thrilling adventure.")