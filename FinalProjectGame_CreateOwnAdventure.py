import json
import random
class Weapon:
    """A class representing a weapon in the game.
    Attributes:
        name (str): The name of the weapon.
        damage (int): The damage dealt by the weapon.
    """
    def __init__(self, name, damage):
        """Initialize the Weapon class.
        Args:
            name (str): The name of the weapon.
            damage (int): The damage dealt by the weapon.
        """
        self.name = name
        self.damage = damage

    def __str__(self):
        """Return a string representation of the weapon."""
        return self.name 
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
adventure = Create_your_own_Adventure_game("LostintheJungle.json")

while adventure.current_level != "end":
    adventure.display_current_level()
    choice = int(input("Enter your choice: ")) - 1  #to match list index

    adventure.handle_player_choice(choice)

print("Yay, You managed to end your thrilling adventure.")