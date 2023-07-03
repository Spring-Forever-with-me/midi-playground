from utils import *
from menu import Menu
from game import Game
from configpage import ConfigPage
from songselector import SongSelector
from os import startfile, getcwd
from config import save_to_file
import debuginfo
import webbrowser
import pygame


def main():

    # pygame and other boilerplate
    n_frames = 0
    pygame.init()
    pygame.mixer.music.load("./assets/mainmenu.mp3")
    pygame.mixer.music.set_volume(Config.volume/100)
    pygame.mixer.music.play(loops=-1, start=2)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
        [Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT],
        pygame.FULLSCREEN | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED,
        vsync=1
    )

    # noinspection PyBroadException
    try:
        pygame.display.set_caption("Midi Playground")
        pygame.display.set_icon(pygame.image.load("./assets/icon.png").convert_alpha())
    except Exception as e:
        print(e)

    # the big guns
    menu = Menu()
    song_selector = SongSelector()
    config_page = ConfigPage()
    game = Game()

    # game loop
    running = True
    while running:
        n_frames += 1
        # thanks to TheCodingCrafter for the implementation
        if Config.theme == "rainbow":
            to_set_as_rainbow = pygame.Color((0, 0, 0))
            to_set_as_rainbow2 = pygame.Color((0, 0, 0))
            to_set_as_rainbow.hsva = (((pygame.time.get_ticks()/1000)*Config.rainbow_speed) % 360, 100, 75, 100)
            to_set_as_rainbow2.hsva = ((((pygame.time.get_ticks()/1000)*Config.rainbow_speed)+180) % 360, 100, 75, 100)
            get_colors()["background"] = to_set_as_rainbow
            get_colors()["hallway"] = to_set_as_rainbow2
            get_colors()["square"][0] = to_set_as_rainbow

        screen.fill(get_colors()["background"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # artificial lag spike for debugging purposes
                if event.key == pygame.K_F12:
                    total = 0
                    for _ in range(10_000_000):
                        total += 1
                if event.key == pygame.K_F3:
                    debuginfo.print_debug_info()
                if event.key == pygame.K_ESCAPE:
                    if song_selector.active:
                        song_selector.active = False
                        menu.active = True
                        if song_selector.selected_index+1:
                            pygame.mixer.music.load("./assets/mainmenu.mp3")
                            pygame.mixer.music.set_volume(Config.volume/100)
                            pygame.mixer.music.play(loops=-1, start=2)
                            song_selector.selected_index = -1
                        continue
                    if game.active:
                        game.active = False
                        song_selector.active = True
                        pygame.mixer.music.load("./assets/mainmenu.mp3")
                        pygame.mixer.music.set_volume(Config.volume/100)
                        pygame.mixer.music.play(loops=-1, start=2)
                        song_selector.selected_index = -1
                        continue
                    if config_page.active:
                        config_page.active = False
                        menu.active = True
                        continue
                    running = False

            # handle menu events
            option_id = menu.handle_event(event)
            if option_id:
                if option_id == "open-songs-folder":
                    startfile(join(getcwd(), "songs"))
                    continue
                if option_id == "contribute":
                    webbrowser.open("https://github.com/quasar098/midi-playground")
                    continue
                menu.active = False
                if option_id == "config":
                    config_page.active = True
                if option_id == "play":
                    song_selector.active = True
                    song_selector.reload_songs()
                if option_id == "quit":
                    running = False
                continue

            # handle song selector events
            song = song_selector.handle_event(event)
            if song:
                if isinstance(song, bool):
                    menu.active = True
                    if song_selector.selected_index+1:
                        pygame.mixer.music.load("./assets/mainmenu.mp3")
                        pygame.mixer.music.set_volume(Config.volume/100)
                        pygame.mixer.music.play(loops=-1, start=2)
                        song_selector.selected_index = -1
                    continue
                # starting song now
                Config.current_song = song
                game.active = True
                if game.start_song(screen):
                    game.active = False
                    song_selector.active = True
                    pygame.mixer.music.load("./assets/mainmenu.mp3")
                    pygame.mixer.music.set_volume(Config.volume/100)
                    pygame.mixer.music.play(loops=-1, start=2)

            # handle config page events
            if config_page.handle_event(event):
                config_page.active = False
                menu.active = True

            # handle game events
            if game.handle_event(event):
                game.active = False
                song_selector.active = True

        # draw stuff here
        game.draw(screen, n_frames)
        song_selector.draw(screen)
        config_page.draw(screen)
        menu.draw(screen, n_frames)

        pygame.display.flip()
        Config.dt = clock.tick(FRAMERATE)/1000
    pygame.quit()
    save_to_file()


if __name__ == '__main__':
    main()
