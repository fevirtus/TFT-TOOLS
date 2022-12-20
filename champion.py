"""
Contains all information related to an individual board slot used by the bot
"""


class Champion:
    """Champion class that contains information about a single unit on the board or bench"""

    def __init__(self, name: str, coords: tuple, build, slot: int, size: int, final_comp: bool) -> None:
        self.name: str = name
        self.coords: tuple = coords
        self.build = build
        self.index: int = slot
        self.size: int = size
        self.completed_items: list = []
        self.current_building: list = []
        self.final_comp: bool = final_comp
