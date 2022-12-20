"""
Where the bot execution starts & contains the game loop that keeps the bot running indefinitely
"""

from ui import UI
from game import Game
import multiprocessing
import auto_queue
import settings
import inquirer


def select_tools() -> str:
    """Select tool to action"""
    list_tools = ['Auto buy champs', 'Bot farm', 'xyz']
    tools = {inquirer.Checkbox(
        'list_tool', message='Choose just ONE tool you need', choices=list_tools)}
    result = inquirer.prompt(tools).get('list_tool')
    return result[0]


def game_loop(ui_queue: multiprocessing.Queue) -> None:
    """Keeps the program running indefinetly by calling queue and game start in a loop"""
    tool = select_tools()
    print(f'tool: {tool}')
    while True:
        if tool == 'Bot farm':
            auto_queue.queue()
        Game(ui_queue, tool)


if __name__ == "__main__":
    if settings.LEAGUE_CLIENT_PATH is None:
        raise Exception(
            "No league client path specified. Please set the path in settings.py")
    message_queue = multiprocessing.Queue()
    overlay: UI = UI(message_queue)
    game_thread = multiprocessing.Process(
        target=game_loop, args=(message_queue,))

    print("Close this window to terminate the overlay window & program")
    game_thread.start()
    overlay.ui_loop()
