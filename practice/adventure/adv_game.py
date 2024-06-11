clues = [
    "There is a faded photograph of a grand ballroom filled with elegantly dressed people.",
    "There is a scorched mark on the floor, hinting at a past fire.",
    "There is a worn-out diary with entries dating back to the 1800s.",
    "There is a shattered mirror, its pieces scattered around the room.",
    "There is a dusty old map with a route marked in red ink.",
    "There is a cryptic message etched into the wooden floorboards.",
    "There is a painting of a stormy sea hanging crooked on the wall.",
    "There is a rusty key hidden under a loose floor tile.",
    "There is a mysterious symbol painted on the ceiling.",
    "There is a broken clock, its hands frozen at midnight."
]

sense_exp = [
    "You see a flickering candle casting long shadows on the stone walls.",
    "You hear the distant echo of footsteps in the empty hallways.",
    "You smell the musty scent of old books and parchment.",
    "You touch the cold, rough surface of a stone wall.",
    "You intuit a sense of foreboding as you step into the dimly lit room.",
    "You see a cobweb-draped chandelier swaying gently in the draft.",
    "You hear the soft, eerie whisper of the wind through the cracks in the walls.",
    "You smell the faint, lingering scent of a wood fire long extinguished.",
    "You touch the worn velvet of a centuries-old throne.",
    "You intuit a feeling of being watched, though you see no one.",
    "You see the moonlight filtering through a cracked stained glass window.",
    "You hear the distant tolling of a bell from the castle tower."
]

import random

class RandomItemSelector:
    def __init__(self, items):
        self.items = items
        self.used_items = []

    def add_item(self, item):
        self.items.append(item)

    def pull_random_item(self):
        if not self.items:
            print("No items to select.")
            return None
        if len(self.used_items) == len(self.items):
            self.reset()
        while True:
            item = random.choice(self.items)
            if item not in self.used_items:
                self.used_items.append(item)
                return item

    def reset(self):
        self.used_items = []



class SenseClueGenerator:
    _instance = None

    def __new__(cls, clues, sense_exp):
        if cls._instance is None:
            cls._instance = super(SenseClueGenerator, cls).__new__(cls)
            cls._instance.clue_selector = RandomItemSelector(clues)
            cls._instance.sense_selector = RandomItemSelector(sense_exp)
        return cls._instance

    def get_senseclue(self):
        clue = self.clue_selector.pull_random_item()
        sense = self.sense_selector.pull_random_item()
        return f"{clue} {sense}"
    

from enum import Enum

class EncounterOutcome(Enum):
    CONTINUE = 1
    END = 2

from abc import ABC, abstractmethod

class Encounter(ABC):
    @abstractmethod
    def run_encounter(self):
        pass


class DefaultEncounter(Encounter):
    def __init__(self, clues, sense_exp):
        self.sense_clue_generator = SenseClueGenerator(clues, sense_exp)

    def run_encounter(self):
        sense_clue = self.sense_clue_generator.get_senseclue()
        print(sense_clue)
        return EncounterOutcome.CONTINUE


class Room:
    def __init__(self, name, encounter):
        self.name = name
        self.encounter = encounter

    def visit_room(self):
        return self.encounter.run_encounter()
    
rooms = [
    Room("Throne Room", DefaultEncounter(clues, sense_exp)),
    Room("Library", DefaultEncounter(clues, sense_exp)),
    Room("Dungeon", DefaultEncounter(clues, sense_exp)),
    Room("Observatory", DefaultEncounter(clues, sense_exp)),
    Room("Armory", DefaultEncounter(clues, sense_exp)),
    Room("Secret Passage", DefaultEncounter(clues, sense_exp))
]

class TreasureEncounter(Encounter):
    def run_encounter(self):
        print("Congratulations! You found the treasure and won the game!")
        return EncounterOutcome.ENDclass
    def run_encounter(self):
        print("Congratulations! You found the treasure and won the game!")
        return EncounterOutcome.END
    
# add a Treasure Room with a Treasure Encounter to the rooms list
rooms.append(Room("Treasure Room", TreasureEncounter()))

class RedWizardEncounter(Encounter):
    def run_encounter(self):
        game_rules = {
            "Fireball": ["Ice Shard", "Lightning Bolt"],
            "Ice Shard": ["Wind Gust", "Earthquake"],
            "Wind Gust": ["Lightning Bolt", "Fireball"],
            "Lightning Bolt": ["Earthquake", "Ice Shard"],
            "Earthquake": ["Fireball", "Wind Gust"]
        }

        while True:
            print("You are challenged by the Red Wizard to a spell battle!")
            user_spell = input("Choose your spell: Fireball, Ice Shard, Wind Gust, Lightning Bolt, or Earthquake: ")
            wizard_spell = random.choice(list(game_rules.keys()))
            print(f"The Red Wizard casts {wizard_spell}.")

            if user_spell == wizard_spell:
                print("It's a draw! Play again.")
            elif user_spell in game_rules[wizard_spell]:
                print("You have been vanquished from this castle by the Red Wizard!")
                return EncounterOutcome.END
            else:
                print("You have vanquished the Red Wizard from this castle!")
                return EncounterOutcome.CONTINUE
            
# create a room called “The Red Wizard’s Lair” with the Red Wizard Encounter and add it to the rooms list
rooms.append(Room("The Red Wizard's Lair", RedWizardEncounter()))



class Castle:
    def __init__(self, rooms):
        self.room_selector = RandomItemSelector(rooms)

    def select_door(self):
        while True:
            num_doors = random.randint(2, 4)
            print(f"There are {num_doors} doors. Which door do you choose?")
            door = input()
            if door.isdigit() and 1 <= int(door) <= num_doors:
                return int(door)
            else:
                print("Invalid input. Please enter a valid door number.")

    def next_room(self):
        self.select_door()
        room = self.room_selector.pull_random_item()
        print(f"You have entered the {room.name}.")
        return room.visit_room()

    def reset(self):
        self.room_selector.reset()


class Game:
    def __init__(self, rooms):
        self.castle = Castle(rooms)

    def play_game(self):
        print("Welcome to the Castle Adventure Game! Your objective is to navigate through the castle and find the treasure.")
        while True:
            outcome = self.castle.next_room()
            if outcome == EncounterOutcome.END:
                self.castle.reset()
                print("Game Over.")
                play_again = input("Would you like to explore a different castle? (yes/no) ")
                if play_again.lower() != "yes":
                    break

# run the game
game = Game(rooms)
game.play_game()