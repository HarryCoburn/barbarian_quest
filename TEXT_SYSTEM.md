# Game Text System

The Barbarian Quest text management system provides a centralized, organized way to store and retrieve all game narrative text.

## Overview

All game text is stored in `src/common/game_text.py` using the `GameText` class. Text is organized into categories using the `TextCategory` enum.

## Text Categories

- **INTRO**: Introduction and opening narrative
- **EVENT**: Game events (new day, food consumption, game over, victory)
- **LOCATION**: Location descriptions (forest, plains, mountains, village)
- **ENCOUNTER**: NPC and creature encounters
- **COMBAT**: Combat-related messages
- **MERCHANT**: Merchant interaction text
- **QUEST**: Quest-related narrative
- **FLAVOR**: General flavor text

## Usage

### Basic Text Retrieval

```python
from src.common.game_text import GameText, TextCategory

# Get a specific text
intro = GameText.get_text(TextCategory.INTRO, "opening")
```

### Text with Variable Substitution

```python
# Format text with variables
day_text = GameText.format_text(TextCategory.EVENT, "new_day", day=5)
# Returns: "A new day begins. Day 5."
```

### Get All Texts in a Category

```python
# Get all intro texts
all_intros = GameText.get_category(TextCategory.INTRO)
# Returns: {"opening": "...", "game_start": "..."}
```

## Integration with View

The View class can display game text using the `update_info()` method:

```python
from src.view.view import View
from src.common.game_text import GameText, TextCategory

view = View(game_state)
intro = GameText.get_text(TextCategory.INTRO, "opening")
view.update_info(intro)
```

## Adding New Text

To add new game text:

1. Choose the appropriate `TextCategory` or add a new one if needed
2. Add your text to the `_texts` dictionary in `GameText`
3. Use `{variable_name}` for any values that need to be substituted

Example:
```python
TextCategory.EVENT: {
    "treasure_found": "You found {amount} gold pieces!",
}

# Usage:
GameText.format_text(TextCategory.EVENT, "treasure_found", amount=50)
```

## Design Principles

- **Centralized**: All text in one location makes editing and translation easier
- **Organized**: Categories keep related text together
- **Flexible**: Variable substitution allows dynamic text
- **Type-safe**: Enum-based categories prevent typos
- **Testable**: Easy to unit test text retrieval
