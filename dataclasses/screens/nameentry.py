import pygame

from dataclasses.gamestage import GameStage
from dataclasses.screens.screen import Screen, exit_check

white = (255, 255, 255)


class NameEntry(Screen):

    def __init__(self, game):
        super().__init__(game)
        self.input_rect = None
        self.user_text = ''

    def show(self):
        # basic font for user typed
        base_font = pygame.font.Font(None, 32)

        # create rectangle
        self.input_rect = pygame.Rect(self.screen_dim[0] / 2, 200, 180, 32)

        # color stores color(lightskyblue3) which
        # gets active when input box is clicked by user
        color = pygame.Color('lightskyblue3')

        # it will set background color of screen
        self.display.fill((0, 0, 0))

        font_small = pygame.font.Font('freesansbold.ttf', 32)
        text_name_line = font_small.render('Name of Player ' + str(self.game.player_name_entry + 1) + ":", True, white)
        text_rect_name_line = text_name_line.get_rect(topleft=(self.screen_dim[0] / 2 - 300, 200))
        self.display.blit(text_name_line, text_rect_name_line)
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(self.display, color, self.input_rect)

        # draw text in box
        text_surface = base_font.render(self.user_text, True, (255, 255, 255))

        # render at position stated in arguments
        self.display.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

        # set width of textfield so that text cannot get
        # outside of user's text input
        self.input_rect.w = max(100, text_surface.get_width() + 10)

    def listen(self):
        for event in pygame.event.get():

            # if user types QUIT then the screen will close
            exit_check(event)

            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    self.user_text = self.user_text[:-1]

                # Unicode standard is used for string
                # formation

                if event.key == pygame.K_RETURN:
                    # Create Player
                    self.game.add_player(self.user_text)

                    # Increase the player indicator
                    self.game.player_name_entry += 1
                    # clear user_text
                    self.user_text = ''
                    # check if we need to move on to the next stage.
                    if self.game.player_name_entry == self.game.get_number_of_players():
                        for i in range(self.game.get_number_of_players(), 1, -1):
                            self.game.get_players()[i - 2].add_next_player(self.game.get_players()[i - 1])
                        self.game.game_stage = GameStage.ROUND_BEGIN

                else:
                    self.user_text += event.unicode
