import json

class Adventure:
    """
    A class representing our adventure game.
    """

    def __init__(self, story):
        """
        Initializes an Adventure instance with the provided story and sets the initial state.

        Parameters:
        - story (list): A list representing the story data.
        """
        self.story = story
        self.current_level = 1
        self.inventory = {'sword': 0, 'axe': 0}

    def display_current_level(self):
        """
        Displays the text of the current level in the story.
        """
        level = self.story[self.current_level - 1]
        print(level['text'])

    def get_user_choice(self, num_options=2):
        """
        Gets the user's choice as input and validates it.

        Returns:
        - int: The user's choice (1 or 2).
        """
        while True:
            try:
                choice = int(input("Enter your choice (1 to {num_options}): "))  # Accept 1 or 2
                if 1 <= choice <= num_options:
                    return choice
                else:
                    raise ValueError("Invalid choice. Please enter 1 or 2.")
            except ValueError as e:
                print(e)

    def update_inventory(self, item):
        """Updates the inventory based on the chosen item.

        Parameters:
        - item (dict): The item dictionary containing information about the chosen item.
        """
        if item['type'] == 'weapon':
           if item['text'] == 'Ebony Blade':
               self.inventory['sword'] += 1
        elif item['text'] == 'Axe of the Accuser':
           self.inventory['axe'] += 1

    def load_story_from_json(self, file_path):
        """
        Loads the story data from a JSON file.

        Parameters:
        - file_path (str): The path to the JSON file.
        """
        with open(file_path, 'r') as json_file:
            self.story = json.load(json_file)
            
        if self.story and len(self.story) > 0:
            player_name = input("Enter the name of your character:  ")
            self.story[0]["text"] = self.story[0]["text"].replace("<player_name>", player_name)
            
            
    def evaluate_attribute_points(self):
        """
        Evaluates the overall performance of the character based on attribute points.
        Returns:
        - str: The evaluation result.
        """
        total_points = sum(self.story[2]['attributes'].values())
        result = "Excellent" if total_points >= 35 else "Good" if total_points >= 20 else "Needs Improvement"
        return f"Character's attribute points evaluation: {result}"

    
    def enter_temple(self, name, location="Jungle Temple"):
        """
        Enters a temple at a specified location.

        Parameters:
        - name (str): The name of the character.
        - location (str, optional): The location of the temple. Defaults to "Jungle Temple".

        Returns:
        - str: A message indicating the character's entry into the temple.
        """
        entry_line = self.story[0]["text"].replace('<player_name>', name)
        return f"{name} enters the {location}. The air inside is thick with mystery and anticipation."

    def manage_inventory(self, item):
        """
        Updates the inventory based on the chosen item.

        Parameters:
        - item (dict): The item dictionary containing information about the chosen item.
        """
        if item['type'] == 'weapon':
           self.update_inventory(item)
        elif item['type'] == 'utility':
           self.update_inventory(item)

    def play(self):
        """
        Plays through the adventure story, allowing the user to make choices.
        """
        player_name = input("Enter the name of your character: ")
        
        while self.current_level <= len(self.story):
            self.display_current_level()
            choice = self.get_user_choice()

            if 'options' in self.story[self.current_level - 1]:
                next_level_id = self.story[self.current_level - 1]['options'][choice - 1]['next_id']
                next_level = next((level for level in self.story if level['id'] == next_level_id), None)

                if 'text' in next_level and 'options' not in next_level:
                    print(next_level['text'])
                    break  # End of the game
                elif 'text' in next_level:
                    self.current_level = next_level_id
                else:
                    raise ValueError("Invalid story structure.")
                if 'text' in next_level:
                    print(next_level['text'])
                if 'text' in next_level and 'options' in next_level:
                    for i, option in enumerate(next_level['options'], start=1):
                        print(f"{i}. {option['text']}")

                if 'text' in next_level and 'options' in next_level:
                    choice = self.get_user_choice()
                    next_level_id = next_level['options'][choice - 1]['next_id']
                    self.current_level = next_level_id

            else:
                print("Congratulations! You completed the adventure.")
                break

        print(f"{player_name}, here's what is in your inventory:")
        print(f'{player_name} has {self.inventory["sword"]} in their inventory.')
        print(f'{player_name} has {self.inventory["axe"]} in their inventory.')


json_file_path = 'jungle.json'
adventure = Adventure([])
adventure.load_story_from_json(json_file_path)
adventure.play()
adventure.update_inventory()
