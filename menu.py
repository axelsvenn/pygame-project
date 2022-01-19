import pygame
import pygame_menu

pygame.init()

surface = pygame.display.set_mode((800, 400), pygame.RESIZABLE)
pygame.display.set_caption("МунчиАвтансем!")
ABOUT = [f'pygame-menu {pygame_menu.version}',
         'попрыгай на моём fat cock е']
HELP = ['Потрогай моего петуха']

menu = pygame_menu.Menu(
    height=100,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Добро пожаловать!',
    width=100
)

help_menu = pygame_menu.Menu(
    height=300,  # Fullscreen
    title='Помощь',
    width=800
)

settings = pygame_menu.Menu(
    height=300,  # Fullscreen
    title='Настройки',
    width=800
)

about_menu = pygame_menu.Menu(
    center_content=False,
    height=400,
    title='Об игре',
    width=600
)

play = pygame_menu.Menu(
    center_content=False,
    height=400,
    title='Выберите имя',
    width=600
)


def on_resize() -> None:
    window_size = surface.get_size()
    new_w, new_h = 0.75 * window_size[0], 0.7 * window_size[1]
    menu.resize(new_w, new_h)
    print(f'New menu size: {menu.get_size()}')


def foo():
    print('...')


menu.add.button('Играть', play)
menu.add.button('Об игре', about_menu)
menu.add.button('Помощь', help_menu)
menu.add.button('Настройки', settings)
menu.add.button('Выход', pygame_menu.events.EXIT)

user_name1 = play.add.text_input('Имя игрока1: ', default='', maxchar=15)
user_name2 = play.add.text_input('Имя игрока2: ', default='', maxchar=15)
play.add.selector('Карта: ', [('Адская дорога к мунче', 1), ('Райская дорога к мунче', 2)])
play.add.button('Приступить к игре', foo())

settings.add.selector('Скорость петухов: ', [('Медленная', 1), ('Норма', 2), ('Быстро', 3)])
settings.add.selector('Разрешение петухов: ', [('800x600', 1), ('1280x1024', 2), ('1920x1080', 3)])


menu.enable()
on_resize()  # Set initial size
for m in HELP:
    help_menu.add.label(m, align=pygame_menu.locals.ALIGN_CENTER)
for m in ABOUT:
    about_menu.add.label(m, margin=(0, 0))

if __name__ == '__main__':
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                # Update the surface
                surface = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                # Call the menu event
                on_resize()

        # Draw the menu
        surface.fill((25, 0, 50))

        menu.update(events)
        menu.draw(surface)

        pygame.display.flip()
