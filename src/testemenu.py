"""
pygame-menu
https://github.com/ppizarror/pygame-menu
EXAMPLE - SIMPLE
Super simple example of pygame-menu usage, featuring a selector and a button.
"""

import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('Example - Simple', (600, 400))


def set_difficulty(selected: Tuple, value: Any) -> None:
    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0]} ({value})')


def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    global user_name
    print(f'{user_name.get_value()}, Do the job here!')


menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_DARK,
    title='Battle game!',
    width=400
)

user_name = menu.add.text_input('Nome: ', default='Pedrin', maxchar=10)
menu.add.selector('Dificuldade: ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Jogar', start_the_game)
menu.add.button('Sair', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)