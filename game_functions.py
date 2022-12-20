"""
Functions used by the Game class to retrieve relevant data
"""

from time import sleep
from PIL import ImageGrab
import screen_coords
import ocr
import game_assets
import mk_functions


def get_round() -> str:
    """Gets the current game round"""
    screen_capture = ImageGrab.grab(bbox=screen_coords.ROUND_POS.get_coords())
    round_two = screen_capture.crop(screen_coords.ROUND_POS_TWO.get_coords())
    game_round: str = ocr.get_text_from_image(
        image=round_two, whitelist=ocr.ROUND_WHITELIST)
    if game_round in game_assets.ROUNDS:
        return game_round

    round_one = screen_capture.crop(screen_coords.ROUND_POS_ONE.get_coords())
    game_round: str = ocr.get_text_from_image(
        image=round_one, whitelist=ocr.ROUND_WHITELIST)
    return game_round


def check_alive() -> bool:  # Refactor this function to use API
    """Checks the screen to see if player is still alive"""
    if ocr.get_text(screenxy=screen_coords.EXIT_NOW_POS.get_coords(), scale=3, psm=7) == 'EXIT NOW':
        return False
    if ocr.get_text(screenxy=screen_coords.VICTORY_POS.get_coords(), scale=3, psm=7) == 'CONTINUE':
        return False
    return True


def select_shop() -> None:
    """Clicks the take all button on special round"""
    mk_functions.left_click(screen_coords.TAKE_ALL_BUTTON.get_coords())


def default_pos() -> None:
    """Moves the mouse to a default position to ensure no data is being blocked from OCR"""
    mk_functions.left_click(screen_coords.DEFAULT_LOC.get_coords())
