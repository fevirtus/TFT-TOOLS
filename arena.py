"""
Handles the board / bench state inside of the game and
other variables used by the bot to make decisions
"""

import game_assets
import mk_functions
import screen_coords
import arena_functions
import json


class Arena:
    """Arena class that handles game logic such as board and bench state"""

    def __init__(self, tool: str) -> None:
        self.tool = tool

    def auto_buy_champs(self) -> None:
        """auto buy selected champs in shop"""
        while True:
            shop: list = arena_functions.get_shop()
            with open('D:\\dam coding\\TFT-TOOLS\\auto_buy_champs.json', 'r') as file:
                data = json.load(file)
            for champion in shop:
                if (champion[1] in data['AUTO_BUY_CHAMPS'] and arena_functions.get_gold() -
                        game_assets.CHAMPIONS[champion[1]]["Gold"] >= 0 and arena_functions.empty_slot() != -1):
                    mk_functions.left_click(
                        screen_coords.BUY_LOC[champion[0]].get_coords())
