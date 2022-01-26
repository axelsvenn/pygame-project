import pygame
import pygame_menu

pygame.init()

surface = pygame.display.set_mode((800, 400), pygame.RESIZABLE)
pygame.display.set_caption("Лабиринт")
ABOUT = [f'Игра была разработана компанией "SusheniyHren.Intertamend"',
         'Авторы: "Turbosvin2005" и "Mulgach2005"']
HELP = ['Смысл игры заключается в том, чтобы убегать от хитманов,', 'попутно убивая их и зарабатывая тем самым очков']

menu = pygame_menu.Menu(
    height=100,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Добро пожаловать!',
    width=100
)

help_menu = pygame_menu.Menu(
    height=400,  #Полный экран
    title='Помощь',
    width=800
)

settings = pygame_menu.Menu(
    height=400,  # Полный экран
    title='Настройки',
    width=800
)

about_menu = pygame_menu.Menu(
    center_content=False,
    height=400,
    title='Об игре',
    width=800
)

play = pygame_menu.Menu(
    center_content=False,
    height=400,
    title='Выберите имя',
    width=800
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

user_name = play.add.text_input('Имя игрока: ', default='', maxchar=15)
play.add.selector('Карта: ', [('Лабиринт с лысыми', 1)])
play.add.button('Приступить к игре', foo())

settings.add.selector('Скорость хитманов: ', [('Медленная', 1), ('Норма', 2), ('Быстро', 3)])
settings.add.selector('Разрешение: ', [('800x600', 1), ('1280x1024', 2), ('1920x1080', 3)])

menu.enable()
on_resize()  # обновить размер
for m in HELP:
    help_menu.add.label(m, align=pygame_menu.locals.ALIGN_LEFT)
for m in ABOUT:
    about_menu.add.label(m, margin=(0, 0), align=pygame_menu.locals.ALIGN_LEFT)

if __name__ == '__main__':
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEORESIZE:
                # обновить surface
                surface = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                # вызвать ивент меню
                on_resize()

        # нарисовать меню
        surface.fill((25, 0, 50))

        menu.update(events)
        menu.draw(surface)

        pygame.display.flip()
