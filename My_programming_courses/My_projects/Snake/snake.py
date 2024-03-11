import pygame
from pygame.math import Vector2

cell_size = 40
cell_number = 20

screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))


class Snake():
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        # importing the body of the snake
        self.head_up = pygame.image.load(
            "Graphics/head_up.png").convert_alpha()
        self.head_down = pygame.image.load(
            "Graphics/head_down.png").convert_alpha()
        self.head_right = pygame.image.load(
            "Graphics/head_right.png").convert_alpha()
        self.head_left = pygame.image.load(
            "Graphics/head_left.png").convert_alpha()

        self.tail_up = pygame.image.load(
            "Graphics/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load(
            "Graphics/tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load(
            "Graphics/tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load(
            "Graphics/tail_left.png").convert_alpha()

        self.body_vertical = pygame.image.load(
            "Graphics/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load(
            "Graphics/body_horizontal.png").convert_alpha()

        self.body_tr = pygame.image.load(
            "Graphics/body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load(
            "Graphics/body_tl.png").convert_alpha()
        self.body_br = pygame.image.load(
            "Graphics/body_br.png").convert_alpha()
        self.body_bl = pygame.image.load(
            "Graphics/body_bl.png").convert_alpha()

        # import the music
        self.crunch_sound = pygame.mixer.Sound("Sound/Crunch.wav")

    def draw_snake(self):
        for index, block in enumerate(self.body):
            # updating the head direction
            self.update_head_graphic()
            self.update_tail_graphic()

            #  rect for positioning
            x_position = int(block.x * cell_size)
            y_position = int(block.y * cell_size)
            block_rectangle = pygame.Rect(
                x_position, y_position, cell_size, cell_size)

            # what direction is the face heading
            if index == 0:
                screen.blit(self.head, block_rectangle)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rectangle)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rectangle)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rectangle)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rectangle)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rectangle)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rectangle)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rectangle)

    def update_head_graphic(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphic(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()
