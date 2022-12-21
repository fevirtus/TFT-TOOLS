"""
Handles tasks that happen each game round
"""

from time import sleep
import json
import win32gui
import game_functions
from arena import Arena
from vec4 import Vec4
from vec2 import Vec2


class Game:
    """Game class that handles game logic such as round tasks"""

    def __init__(self, tool: str) -> None:
        self.arena = Arena(tool)
        self.found_window = False
        self.tool = tool

        print("\n[!] Searching for game window")
        while not self.found_window:
            print("  Did not find window, trying again...")
            win32gui.EnumWindows(self.callback, None)
            sleep(1)

        self.auto_buy_champs_tool()

    def callback(self, hwnd, extra) -> None:
        """Function used to find the game window and get its size"""
        if "League of Legends (TM) Client" not in win32gui.GetWindowText(hwnd):
            return

        rect = win32gui.GetWindowRect(hwnd)

        x_pos = rect[0]
        y_pos = rect[1]
        width = rect[2] - x_pos
        height = rect[3] - y_pos

        if width < 200 or height < 200:
            return

        print(f"  Window {win32gui.GetWindowText(hwnd)} found")
        print(f"    Location: ({x_pos}, {y_pos})")
        print(f"    Size:     ({width}, {height})")
        Vec4.setup_screen(x_pos, y_pos, width, height)
        Vec2.setup_screen(x_pos, y_pos, width, height)
        self.found_window = True

    def auto_buy_champs_tool(self) -> None:
        """This tool loop every round and buy selected champs"""
        while game_functions.check_alive():
            with open('D:\\dam coding\\TFT-TOOLS\\auto_buy_champs.json', 'r') as file:
                data = json.load(file)
            print(f"List champions auto buy: {data['AUTO_BUY_CHAMPS']}")
            self.arena.auto_buy_champs()
