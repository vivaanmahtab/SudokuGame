
import pygame
from constants import *
from sudokuReader import SudokuReader
import time


def homeScreen(screen, hover):

    font1 = pygame.font.Font(pygame.font.get_default_font(), 60)
    font2 = pygame.font.Font(pygame.font.get_default_font(), 30)

    color1 = (5, 181, 43)
    color2 = (0, 99, 21)

    colors = [color1, color1, color1, color1]
    if hover is not None:
        colors[hover] = color2

    main_title = font1.render("Sudoku", 1, color1)

    easy = font2.render("easy", 1, colors[0])
    medium = font2.render("medium", 1, colors[1])
    hard = font2.render("hard", 1, colors[2])
    extreme = font2.render("extreme", 1, colors[3])

    screen.blit(main_title, main_title.get_rect(center=(1000/2, 100)))

    screen.blit(easy, easy.get_rect(center=(1000/2, 250)))
    screen.blit(medium, medium.get_rect(center=(1000 / 2, 325)))
    screen.blit(hard, hard.get_rect(center=(1000 / 2,  400)))
    screen.blit(extreme, extreme.get_rect(center=(1000 / 2, 475)))



def drawBoard(screen):

    # draw white background and border
    pygame.draw.rect(screen, WHITE, pygame.Rect(30, 30, WIDTH, HEIGHT))
    pygame.draw.rect(screen, BLACK, pygame.Rect(30, 30, WIDTH, HEIGHT), 5)

    # horizontal lines
    for row in range(1, 9):
        thickness = 1 if row % 3 != 0 else 3
        pygame.draw.line(screen, BLACK, (KERNING, KERNING + HEIGHT/9*row),
                         (KERNING+WIDTH, KERNING + HEIGHT/9*row), thickness)

    # vertical lines
    for col in range(1, 9):
        thickness = 1 if col % 3 != 0 else 3
        pygame.draw.line(screen, BLACK, (KERNING + WIDTH/9 * col, KERNING),
                         (KERNING + WIDTH/9 * col, KERNING + HEIGHT), thickness)


def drawButtons(screen):
    positions = []
    font = pygame.font.Font(pygame.font.get_default_font(), 30)
    panel_width = 1000 - WIDTH
    fill_color = (102, 0, 255)
    for i in range(0, 3):
        for j in range(-1, 2):
            val = font.render(str(j + 2 + i*3), 1, fill_color)
            positions.append((WIDTH + panel_width/2 - 25 + j * 100, 200 + 100*i))
            pygame.draw.rect(screen, WHITE, pygame.Rect(WIDTH + panel_width/2 - 25 + j * 100, 200 + 100*i, 75, 75))
            pygame.draw.rect(screen, fill_color,
                             pygame.Rect(WIDTH + panel_width / 2 - 25 + j * 100, 200 + 100 * i, 75, 75), 1)

            screen.blit(val, val.get_rect(center=(WIDTH + panel_width/2 + 25/2 + j * 100, 240 + 100*i)))

    check = font.render("check answer", 1, fill_color)
    pygame.draw.rect(screen, WHITE, pygame.Rect(WIDTH + panel_width / 2 - 100, 515, 235, 50))
    pygame.draw.rect(screen, fill_color, pygame.Rect(WIDTH + panel_width / 2 - 100, 515, 235, 50), 1)
    screen.blit(check, check.get_rect().move(WIDTH + panel_width/2 - 85, 525))

    back = font.render("Exit", 1, BLACK)
    screen.blit(back, back.get_rect().move(1000 - 100, 30))

    return positions

def displayElapsedTime(screen, startTime, endTime):
    if endTime is None:
        endTime = int(time.time())

    font = pygame.font.Font(pygame.font.get_default_font(), 40)
    elapsed = endTime - startTime

    seconds = str(elapsed%60)
    if len(seconds)==1:
        seconds = f"0{seconds}"
    minutes = str(elapsed//60)
    if len(minutes)==1:
        minutes = f"0{minutes}"
    time_display = font.render(f"{minutes}:{seconds}", 1, BLACK)
    screen.blit(time_display, time_display.get_rect(center=(WIDTH + (1000 - WIDTH)/2 + 10, 150)))



def checkAnswer(tiles):

    solved = True

    # none are wrong
    for row in tiles:
        for tile in row:
            if not tile.checkCorrect():
                solved = False

    return solved


def main():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1000, 600))
    running = True
    playing = False
    won = False

    font = pygame.font.Font(pygame.font.get_default_font(), 50)

    tiles = []
    current_number = 0
    startTime = None
    duration = None

    while running:

        positions = []
        screen.fill((255, 246, 161))

        if playing:
            positions = drawButtons(screen)

        pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:

            if not playing:

                if 460 <= pos[0] <= 535 and 240 <= pos[1] <= 260:
                    reader = SudokuReader("easy")
                    tiles = reader.getTiles()
                    playing = True
                    startTime = int(time.time())
                elif 440 <= pos[0] <= 560 and 310 <= pos[1] <= 335:
                    reader = SudokuReader("medium")
                    playing = True
                    startTime = int(time.time())
                    tiles = reader.getTiles()
                elif 465 <= pos[0] <= 540 and 385 <= pos[1] <= 410:
                    reader = SudokuReader("hard")
                    tiles = reader.getTiles()
                    playing = True
                    startTime = int(time.time())
                elif 430 <= pos[0] <= 565 and 460 <= pos[1] <= 485:
                    reader = SudokuReader("extreme")
                    tiles = reader.getTiles()
                    playing = True
                    startTime = int(time.time())



            else:

                # SELECTING NUMBER
                if 645 <= pos[0] <= 945 and 200 <= pos[1] <= 475:
                        for i in range(len(positions)):
                            print(f"[{pos} $ {positions[i]}")
                            if 0 <= pos[0] - positions[i][0] < 75 and 0 <= pos[1] - positions[i][1] < 75:
                                current_number = i + 1
                                break

                # PLACING NUMBER IN GRID
                elif 30 <= pos[0] < 570 and 30 <= pos[1] < 570 and not won:
                    tiles[(pos[1]-30)//60][(pos[0]-30)//60].setValue(current_number)

                # CHECK ANSWeRS
                elif 670 <= pos[0] <= 900 and 515 <= pos[1] <= 560 and not won:
                    print("check")
                    if checkAnswer(tiles):
                        duration = int(time.time())
                        won = True

                # EXIT
                elif 900 <= pos[0] <= 960 and 30 <= pos[1] <= 55:
                    playing = False

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        if not playing:
            hover = None

            if 460 <= pos[0] <= 535 and 240 <= pos[1] <= 260:
                hover = 0
            elif 440 <= pos[0] <= 560 and 310 <= pos[1] <= 335:
                hover = 1
            elif 465 <= pos[0] <= 540 and 385 <= pos[1] <= 410:
                hover = 2
            elif 430 <= pos[0] <= 565 and 460 <= pos[1] <= 485:
                hover = 3

            homeScreen(screen, hover)

        if playing:
            drawBoard(screen)
            for row in tiles:
                for tile in row:
                    tile.draw(screen, font)
            displayElapsedTime(screen, startTime, duration)

        pygame.display.flip()
        clock.tick(30)

main()

