"""
Where the bot execution starts & contains the game loop that keeps the bot running indefinitely
"""

from game import Game
import multiprocessing
import settings
import inquirer


def select_tools() -> str:
    """Select tool to action"""
    list_tools = ['Auto buy champs', 'abc', 'xyz']
    tools = {inquirer.Checkbox(
        'list_tool', message='Choose just ONE tool you need', choices=list_tools)}
    result = inquirer.prompt(tools).get('list_tool')
    return result[0]


def game_loop() -> None:
    """Keeps the program running in a loop"""
    tool = select_tools()
    print(f'Tool: {tool}')
    while True:
        Game(tool)


def check_path() -> None:
    """Check path of LOL client"""
    if settings.LEAGUE_CLIENT_PATH is None:
        raise Exception(
            "No league client path specified. Please set the path in settings.py")


if __name__ == "__main__":
    """Main function"""
    print("Close this window to terminate the overlay window & program")
    game_thread = multiprocessing.Process(target=game_loop)
    game_thread.start()
