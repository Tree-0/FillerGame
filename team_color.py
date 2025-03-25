from enum import Enum

class TeamColor(Enum):
    RED    = (0, 'R', (247, 52, 82))
    BLUE   = (1, 'B', (52, 168, 245))
    GREEN  = (2, 'G', (157, 208, 77))
    YELLOW = (3, 'Y', (255, 224, 27))
    GRAY   = (4, 'Gy', (88, 88, 88))
    PURPLE = (5, 'P', (105, 75, 161))

    def __new__(cls, color_id, shorthand, rgb):
        # Create a new member instance
        obj = object.__new__(cls)
        # Set the member's value to just the color id
        obj._value_ = color_id
        # Store additional attributes
        obj.shorthand = shorthand
        obj.rgb = rgb
        return obj
