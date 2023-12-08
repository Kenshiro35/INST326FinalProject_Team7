import json
import random
import os

#absolute file path
script_dir = os.path.dirname(os.path.abspath(__file__))

""Construct the absolute path to the JSON file""

filepath = os.path.join(script_dir, "LostintheJungle.json")

class Weapon:
    """A class representing a weapon in the game.
    Attributes:
        n˚†ame (str): The name of the weapon.
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
    """A class representing a text-based adventure game engine.
    This class allows the user to create and play through their own adventure stories defined in a JSON file.
    Managing story's progression, player attributes, and an items inventory player has to their disposal.

    Attributes:
        gamestory_file (str): The path to the JSON file containing the adventure story.
    """
    def __init__(self):
        """Initialize the Create_your_own_Adventure_game class to run the JSON file containing the story with options to play.

        Args:
            gamestory_file (str): Path to the JSON File which contains the actual options for the game, to run through this engine code.
        """
        self.story = self.load_story("/Users/kesiharford/Downloads/LostintheJungle.json")
        self.player = {"name": "", "inventory": [], "attributes": {}}
        self.current_level = "start"

    def load_story(self, filepath):
        """Load the adventure story from the provided JSON file.

        Args:
            filepath (str): Path to JSON file containing the adventure story.

        Returns:
            dict: A dictionary representing the loaded story data from the JSON file.
        """
        with open(filepath, "r") as gamestory_file:
            return json.load(gamestory_file)
