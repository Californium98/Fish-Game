import pygame
import random
import math

import time

pygame.init()
#Hello and welcome to my first game!
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fish Game')
icon = pygame.image.load('animalright.png')
pygame.display.set_icon(icon)

background = pygame.image.load('ocean.png')
playerFISHright = pygame.image.load('animalright.png')
direction = 'left'


pyramid = []
pyramidx = []
pyramidy = []
pyramidx_change = []
pyramidy_change_random = []
pyramidy_change = []

num_of_enemies = 15

for i in range(num_of_enemies):
    pyramid.append(pygame.image.load('bin.png'))
    pyramidx.append(random.randint(-10, 910))
    pyramidy.append(5)
    pyramidx_change.append(0)
    pyramidy_change.append(random.uniform(0.5, 2))


#bubbles

bubble = []
bubblex = []
bubbley = []
bubblex_change = []
bubbley_change = []

num_of_bubbles = 5
for z in range(num_of_bubbles):
    bubble.append(pygame.image.load('clean.png'))
    bubblex.append(random.randint(100, 700))
    bubbley.append(600)
    bubblex_change.append(0)
    bubbley_change.append(random.uniform(-0.2, -0.1))
score = 5
movement = True

#button
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

def player(x, y):
    screen.blit(playerFISHright, (x, y))


def SpriteP1(x, y, i):
    screen.blit(pyramid[i], (x, y))

def bubble1(x, y, z):
    screen.blit(bubble[z], (x, y))


def Collision(pyramidx, pyramidy, Playerx, Playery):
    distance = math.sqrt((math.pow(pyramidx - Playerx, 2)) + (math.pow(Playery - pyramidy, 2)))
    if distance < 27:
        return True
    else:
        return False



score_value = 0
font = pygame.font.Font('freesansbold.ttf', 50)
font2 = pygame.font.Font('freesansbold.ttf', 10)


textX = 10
textY = 10
gamex = 0
gamey = 150

over_font = pygame.font.Font('freesansbold.ttf', 32)
def show_score(x, y):
    score = font.render("Lives : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text(x, y):
    over_text = over_font.render("GAME OVER: Press Space to Restart!", True, (255, 0, 0))
    screen.blit(over_text, (x, y))
def credit(x, y):
    credit = font2.render("Game made by: Victor", True, (0, 0, 0))
    screen.blit(credit, (x, y))

restarting = True
while restarting:

    screen.blit(background, (0, 0))
    credx = 290
    credy = 380
    startButton = button((76, 153, 0), 265, 250, 300, 100, 'Start Fish Game')
    startCredit = credit(credx, credy)
    score_value = 5
    Playerx = 400
    Playery = 300
    playerxleft_change = 0
    playerxright_change = 0
    playeryup_change = 0
    playerydown_change = 0

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            restarting = False

            continue
    buttonloop = False
    running = True
    while running:

        screen.fill((0, 128, 225))
        screen.blit(background, (0, 0))
        startButton.draw(screen, (0, 0, 0))
        credit(credx, credy)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                restarting = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.isOver(pos):
                    startButton.x = 900
                    startButton.y = 900
                    buttonloop = True
                    running = False
            if event.type == pygame.MOUSEMOTION:
                if startButton.isOver(pos):
                    startButton.color = (76, 153, 0)
                else:
                    startButton.color = (0, 255, 0)
            pygame.display.update()

    while buttonloop:
        screen.fill((0, 128, 225))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                buttonloop = False
                restarting = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    playeryup_change = -2
                if event.key == pygame.K_DOWN:
                    playerydown_change = 2
                if event.key == pygame.K_LEFT:
                    playerxleft_change = -2
                if event.key == pygame.K_RIGHT:
                    playerxright_change = 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    playerxleft_change = 0
                if event.key == pygame.K_RIGHT:
                    playerxright_change = 0
                if event.key == pygame.K_UP:
                    playeryup_change = 0
                if event.key == pygame.K_DOWN:
                    playerydown_change = 0


        if Playerx <= 0:
            Playerx = 0
        elif Playerx >= 736:
            Playerx = 736
        if Playery <= 0:
            Playery = 0
        elif Playery > 545:
            Playery = 545
        for z in range(num_of_bubbles):
            bubbley[z] += bubbley_change[z]
            if bubbley[z] < 0:
                bubbley[z] = 600
                bubblex[z] = random.randint(10, 790)
            bubble1(bubblex[z], bubbley[z], z)
        for i in range(num_of_enemies):
            pyramidy[i] += pyramidy_change[i]
            collision = Collision(pyramidx[i], pyramidy[i], Playerx, Playery)
            if collision:
                score_value -= 1
                if score_value < 1:
                    game_over_text(gamex, gamey)
                    score_value = 999999
                    time.sleep(1)
                    buttonloop = False
                    running = False
                    continue
                pyramidx[i] = random.randint(100, 700)
                pyramidy[i] = 5
            if pyramidy[i] > 600:
                pyramidx[i] = random.randint(100, 700)
                pyramidy[i] = 5
            SpriteP1(pyramidx[i], pyramidy[i], i)

        Playerx += playerxleft_change
        Playerx += playerxright_change

        Playery += playeryup_change
        Playery += playerydown_change


        player(Playerx, Playery)
        show_score(textX,textY)


   #     if score_value < 1:
    #        time.sleep(3)



        pygame.display.update()



