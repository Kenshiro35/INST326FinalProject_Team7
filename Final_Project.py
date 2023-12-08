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
        - int: The user's choice (1 or 2).
        """
        while True:
            try:
                choice = int(input("Enter your choice (1 or 2): "))  # Accept 1 or 2
                if choice not in [1, 2]:
                    raise ValueError("Invalid choice. Please enter 1 or 2.")
                return choice
            except ValueError as e:
                print(e)

    def update_inventory(self, item):
        """
        Updates the inventory based on the chosen item.

        Parameters:
        - item (dict): The item dictionary containing information about the chosen item.
        """
        if item['text'] == 'Sword':
            self.inventory['swords'] += 1
        elif item['text'] == 'Axe':
            self.inventory['axes'] += 1

    def play(self):
        """
        Plays through the adventure story, allowing the user to make choices.
        """
        while self.current_level <= len(self.story):
            self.display_current_level()
            choice = self.get_user_choice()

            if 'options' in self.story[self.current_level - 1]:
                next_level_id = self.story[self.current_level - 1]['options'][choice - 1]['next_id']
                next_level = next((level for level in self.story if level['id'] == next_level_id), None)

                if 'text' in next_level and 'options' not in next_level:
                    print(next_level['text'])
                    break
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

        print("Here's what is in your inventory:")
        print(f'You have {self.inventory["swords"]} swords in your inventory.')
        print(f'You have {self.inventory["axes"]} axes in your inventory.')


def load_story_from_json(filepath):
    """
    Loads the story data from a JSON file.

    Parameters:
    - filepath (str): The path to the JSON file.

    Returns:
    - list: A list representing the loaded story data from the JSON file.
    """
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


json_file_path = '/Users/kesiharford/Downloads/LostintheJungle.json'
story = load_story_from_json(json_file_path)
adventure = Adventure(story)
adventure.play()

