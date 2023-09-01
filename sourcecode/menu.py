import initialization
from pygame_menu import themes
from time import sleep


def set_players():
    pass

def start_game():
    pass


def main_menu():
    menu = pygame_menu.Menu(300,400,'Welcome',
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Name:',default='user')
    menu.add.selector('PLAYERS:', [('SINGLE',1),('DOUBLE',2)],onchange=set_players)
    menu.add.button('PLAY',start_game)
    menu.add.button('QUIT',pygame_menu.events.EXIT)

    menu.mainloop(screen)


main_menu()



