from enum import Enum
from typing import Optional


class TextCategory(Enum):
    INTRO = "intro"
    EVENT = "event"
    LOCATION = "location"
    ENCOUNTER = "encounter"
    COMBAT = "combat"
    MERCHANT = "merchant"
    QUEST = "quest"
    FLAVOR = "flavor"


class GameText:
    _texts = {
        TextCategory.INTRO: {
            "opening": """
Evil events have overtaken your Northlands Kingdom. Your father, the old king, is dead - assassinated by rivals to the throne. These usurpers now hold the palace with their mercenary royal guard. You have escaped, and must collect 500 gold pieces to raise a force to smash them and retake your heritage. 
            
Furthermore, the usurpers have powerful friends overseas. If you can't return to take them out in ten weeks, their allies will arm and you will lose your kingdom forever.

To escape the mercenary and royal guard, your loyal body servant Ogab smuggled you into a merchant caravan to the southern border. Now, at dawn you roll out of the merchant wagons into a ditch, dust off your clothes, loosen your swordbelt, and get ready to start the first day of your adventure.""",
            "game_start": "Your adventure begins. You must gather 500 gold pieces within 10 weeks to reclaim your kingdom!",
        },
        TextCategory.EVENT: {
            "new_day": "A new day begins. Day {day}.",
            "food_consumed": "You consume 1 food ration.",
            "no_food": "You have no food! Your endurance decreases.",
            "game_over_time": "Ten weeks have passed. The usurpers' allies have arrived. Your kingdom is lost forever.",
            "game_over_endurance": "Your endurance has reached zero. You collapse and your quest ends.",
            "victory": "You have collected 500 gold pieces! You can now return to reclaim your kingdom!",
        },
        TextCategory.LOCATION: {
            "forest": "You are in a dense forest. Trees surround you on all sides.",
            "plains": "You stand on open plains. You can see for miles in every direction.",
            "mountains": "Steep mountains tower before you. The path is treacherous.",
            "village": "A small village lies ahead. Smoke rises from chimneys.",
        },
        TextCategory.ENCOUNTER: {
            "merchant": "A traveling merchant approaches, his cart laden with goods.",
            "bandit": "Bandits emerge from the shadows, weapons drawn!",
            "traveler": "A fellow traveler greets you on the road.",
        },
    }

    @classmethod
    def get_text(cls, category: TextCategory, key: str) -> Optional[str]:
        """
        Retrieve a specific text by category and key.

        Args:
            category: The TextCategory enum value
            key: The specific text key within that category

        Returns:
            The text string if found, None otherwise
        """
        if category in cls._texts:
            return cls._texts[category].get(key)
        return None

    @classmethod
    def get_category(cls, category: TextCategory) -> dict:
        """
        Retrieve all texts in a specific category.

        Args:
            category: The TextCategory enum value

        Returns:
            A dictionary of all texts in that category
        """
        return cls._texts.get(category, {})

    @classmethod
    def format_text(cls, category: TextCategory, key: str, **kwargs) -> Optional[str]:
        """
        Retrieve and format a text with variable substitution.

        Args:
            category: The TextCategory enum value
            key: The specific text key within that category
            **kwargs: Variables to substitute in the text using format()

        Returns:
            The formatted text string if found, None otherwise
        """
        text = cls.get_text(category, key)
        if text:
            return text.format(**kwargs)
        return None
