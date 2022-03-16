import sys
import pygame as pg
from time import sleep
from random import shuffle, choice
from pygame.locals import *

# Terminate the game
def terminate():
    pg.quit()
    sys.exit()

# Sets up the starting page features
def start():
    global game_state
    BLACK = (0, 0, 0)
    ###################### Start-up page background ##########################
    start_page = pg.image.load('cover_page_normal.png')
    start_loc = (0, 0)
    game_display.blit(start_page, start_loc)
    textsize = 35
    textfont = 'arial'
    ##########################################################################

    ###################### Start button ######################################
    start_button_topleft_x = 760
    start_button_topleft_y = 255
    start_button_width = 150
    start_button_height = 50
    start_ptlist = ((start_button_topleft_x, start_button_topleft_y), \
                    (start_button_topleft_x + start_button_width, start_button_topleft_y), \
                    (start_button_topleft_x + start_button_width, start_button_topleft_y + start_button_height), \
                    (start_button_topleft_x, start_button_topleft_y + start_button_height))
    start_poly_wid = 3
    pg.draw.polygon(game_display, BLACK, start_ptlist, start_poly_wid)
    start_txt_font = pg.font.SysFont(textfont, textsize)
    start_txt_surf_obj = start_txt_font.render("START", True, BLACK)
    start_txt_rect = start_txt_surf_obj.get_rect()
    start_txt_rect.center = (start_button_topleft_x + (start_button_width // 2), \
                             start_button_topleft_y + (start_button_height // 2) + 1)
    game_display.blit(start_txt_surf_obj, start_txt_rect)
    ##########################################################################

    ###################### Quit button ######################################
    quit_button_topleft_x = 760
    quit_button_topleft_y = 365
    quit_button_width = 150
    quit_button_height = 50
    quit_ptlist = ((quit_button_topleft_x, quit_button_topleft_y), \
                   (quit_button_topleft_x + quit_button_width, quit_button_topleft_y), \
                   (quit_button_topleft_x + quit_button_width, quit_button_topleft_y + quit_button_height), \
                   (quit_button_topleft_x, quit_button_topleft_y + quit_button_height))
    quit_poly_wid = 3
    pg.draw.polygon(game_display, BLACK, quit_ptlist, quit_poly_wid)

    quit_txt_font = pg.font.SysFont(textfont, textsize)
    quit_txt_surf_obj = quit_txt_font.render('QUIT', True, BLACK)
    quit_txt_rect = quit_txt_surf_obj.get_rect()
    quit_txt_rect.center = (quit_button_topleft_x + (quit_button_width // 2), \
                            quit_button_topleft_y + (quit_button_height // 2) + 1)
    game_display.blit(quit_txt_surf_obj, quit_txt_rect)
    ##########################################################################

    ###################### Mouse Events ######################################
    if event.type == MOUSEMOTION:
        mousex, mousey = event.pos
        if mousex in range(760, 910) and mousey in range(255, 305):
            pg.draw.polygon(game_display, GOLD, start_ptlist, start_poly_wid)

        if mousex in range(760, 910) and mousey in range(365, 410):
            pg.draw.polygon(game_display, GOLD, quit_ptlist, quit_poly_wid)

    if event.type == MOUSEBUTTONDOWN:
        mousex, mousey = event.pos
        # print("x = ", mousex, "y = ", mousey)
        if mousex in range(760, 910) and mousey in range(255, 305):
            pg.draw.polygon(game_display, GOLD, start_ptlist, start_poly_wid)
            pg.display.update()
            game_state = 3
            sleep(1)

        if mousex in range(760, 910) and mousey in range(365, 410):
            pg.draw.polygon(game_display, GOLD, quit_ptlist, quit_poly_wid)
            pg.display.update()
            sleep(1)
            pg.quit()
            sys.exit()

    pg.display.update()

# Sets up the preparing features:
def prepare():
    global current_card
    global current_colour
    global current_play
    global current_num
    global current_function
    global game_state
    global cards
    global player
    global computer_1
    global computer_2
    global computer_3
    #################################################################################
    #################################################################################
    cards = CardStack()
    cards.randomize()
    player = Player()
    computer_1 = Computer()
    computer_2 = Computer()
    computer_3 = Computer()
    player.player_draw(cards, 7)
    computer_1.computer_draw(cards, 7)
    computer_2.computer_draw(cards, 7)
    computer_3.computer_draw(cards, 7)
    ####################### give c1 cards ######################################################
    background = pg.image.load('background.png')
    background_loc = (0, 0)
    cardback = pg.image.load('cardback.png')
    textsize = 25
    textfont = 'arial'

    card1_back_loc = (815, 450)
    while card1_back_loc[1] > 230:
        game_display.blit(background, background_loc)
        x = card1_back_loc[0]
        y = card1_back_loc[1]
        card1_back_loc = (x, y - 40)
        game_display.blit(cardback, card1_back_loc)
        pg.display.update()

    while card1_back_loc[0] > 75:
        game_display.blit(background, background_loc)
        x = card1_back_loc[0]
        y = card1_back_loc[1]
        card1_back_loc = (x - 40, y)
        game_display.blit(cardback, card1_back_loc)
        pg.display.update()

    # print(card1_back_loc)
    card1_back_loc_fix = (55, 230)
    i = 1
    while i < 7:
        i += 1
        card1_back_loc = (815, 450)
        while card1_back_loc[1] > 230:
            game_display.blit(background, background_loc)
            game_display.blit(cardback, card1_back_loc_fix)
            x = card1_back_loc[0]
            y = card1_back_loc[1]
            card1_back_loc = (x, y - 40)
            game_display.blit(cardback, card1_back_loc)
            pg.display.update()

        while card1_back_loc[0] > 75:
            game_display.blit(background, background_loc)
            game_display.blit(cardback, card1_back_loc_fix)
            x = card1_back_loc[0]
            y = card1_back_loc[1]
            card1_back_loc = (x - 40, y)
            game_display.blit(cardback, card1_back_loc)
            pg.display.update()

    c1_card_x = 150
    c1_card_y = 270
    c1_txt_font = pg.font.SysFont(textfont, textsize)
    c1_txt_surf_obj = c1_txt_font.render('X %d' % len(computer_1.have), True, BLACK)
    c1_txt_rect = c1_txt_surf_obj.get_rect()
    c1_txt_rect.center = (c1_card_x, c1_card_y)
    game_display.blit(c1_txt_surf_obj, c1_txt_rect)
    pg.display.update()
    #########################################################################################
    ####################### give c2 cards ######################################################
    card2_back_loc = (815, 450)
    while card2_back_loc[1] > 55:
        game_display.blit(background, background_loc)
        game_display.blit(cardback, card1_back_loc_fix)
        game_display.blit(c1_txt_surf_obj, c1_txt_rect)
        x = card2_back_loc[0]
        y = card2_back_loc[1]
        card2_back_loc = (x, y - 40)
        game_display.blit(cardback, card2_back_loc)
        pg.display.update()

    while card2_back_loc[0] > 500:
        game_display.blit(background, background_loc)
        game_display.blit(cardback, card1_back_loc_fix)
        game_display.blit(c1_txt_surf_obj, c1_txt_rect)
        x = card2_back_loc[0]
        y = card2_back_loc[1]
        card2_back_loc = (x - 40, y)
        game_display.blit(cardback, card2_back_loc)
        pg.display.update()

    card2_back_loc_fix = (495, 50)
    # print(card2_back_loc_fix)
    i = 1
    while i < 7:
        i += 1
        card2_back_loc = (815, 450)
        while card2_back_loc[1] > 55:
            game_display.blit(background, background_loc)
            game_display.blit(cardback, card1_back_loc_fix)
            game_display.blit(c1_txt_surf_obj, c1_txt_rect)
            game_display.blit(cardback, card2_back_loc_fix)
            x = card2_back_loc[0]
            y = card2_back_loc[1]
            card2_back_loc = (x, y - 40)
            game_display.blit(cardback, card2_back_loc)
            pg.display.update()

        while card2_back_loc[0] > 500:
            game_display.blit(background, background_loc)
            game_display.blit(cardback, card1_back_loc_fix)
            game_display.blit(c1_txt_surf_obj, c1_txt_rect)
            game_display.blit(cardback, card2_back_loc_fix)
            x = card2_back_loc[0]
            y = card2_back_loc[1]
            card2_back_loc = (x - 40, y)
            game_display.blit(cardback, card2_back_loc)
            pg.display.update()

    c2_card_x = 580
    c2_card_y = 95
    c2_txt_font = pg.font.SysFont(textfont, textsize)
    c2_txt_surf_obj = c2_txt_font.render('X %d' % len(computer_2.have), True, BLACK)
    c2_txt_rect = c2_txt_surf_obj.get_rect()
    c2_txt_rect.center = (c2_card_x, c2_card_y)
    game_display.blit(c2_txt_surf_obj, c2_txt_rect)
    pg.display.update()
    #########################################################################################
    ####################### give c3 cards ######################################################
    card3_back_loc = (815, 450)
    while card3_back_loc[1] > 240:
        game_display.blit(background, background_loc)
        game_display.blit(cardback, card1_back_loc_fix)
        game_display.blit(c1_txt_surf_obj, c1_txt_rect)
        game_display.blit(cardback, card2_back_loc_fix)
        game_display.blit(c2_txt_surf_obj, c2_txt_rect)
        x = card3_back_loc[0]
        y = card3_back_loc[1]
        card3_back_loc = (x, y - 20)
        game_display.blit(cardback, card3_back_loc)
        pg.display.update()

    while card3_back_loc[0] > 910:
        game_display.blit(background, background_loc)
        game_display.blit(cardback, card1_back_loc_fix)
        game_display.blit(c1_txt_surf_obj, c1_txt_rect)
        game_display.blit(cardback, card2_back_loc_fix)
        game_display.blit(c2_txt_surf_obj, c2_txt_rect)
        x = card3_back_loc[0]
        y = card3_back_loc[1]
        card3_back_loc = (x - 20, y)
        game_display.blit(cardback, card3_back_loc)
        pg.display.update()

    card3_back_loc_fix = (815, 230)
    # print(card3_back_loc_fix)
    i = 1
    while i < 7:
        i += 1
        card3_back_loc = (815, 450)
        while card3_back_loc[1] > 240:
            game_display.blit(background, background_loc)
            game_display.blit(cardback, card1_back_loc_fix)
            game_display.blit(c1_txt_surf_obj, c1_txt_rect)
            game_display.blit(cardback, card2_back_loc_fix)
            game_display.blit(c2_txt_surf_obj, c2_txt_rect)
            game_display.blit(cardback, card3_back_loc_fix)
            x = card3_back_loc[0]
            y = card3_back_loc[1]
            card3_back_loc = (x, y - 20)
            game_display.blit(cardback, card3_back_loc)
            pg.display.update()

        while card3_back_loc[0] > 910:
            game_display.blit(background, background_loc)
            game_display.blit(cardback, card1_back_loc_fix)
            game_display.blit(c1_txt_surf_obj, c1_txt_rect)
            game_display.blit(cardback, card2_back_loc_fix)
            game_display.blit(c2_txt_surf_obj, c2_txt_rect)
            game_display.blit(cardback, card3_back_loc_fix)
            x = card3_back_loc[0]
            y = card3_back_loc[1]
            card3_back_loc = (x - 20, y)
            game_display.blit(cardback, card3_back_loc)
            pg.display.update()

    c3_card_x = 920
    c3_card_y = 250
    c3_txt_font = pg.font.SysFont(textfont, textsize)
    c3_txt_surf_obj = c3_txt_font.render('X %d' % len(computer_3.have), True, BLACK)
    c3_txt_rect = c3_txt_surf_obj.get_rect()
    c3_txt_rect.center = (c3_card_x, c3_card_y)
    game_display.blit(c3_txt_surf_obj, c3_txt_rect)
    pg.display.update()
    #####################################################################################################
    ####################### give player cards ######################################################
    game_display.blit(background, background_loc)
    game_display.blit(cardback, card1_back_loc_fix)
    game_display.blit(cardback, card2_back_loc_fix)
    game_display.blit(cardback, card3_back_loc_fix)
    game_display.blit(c1_txt_surf_obj, c1_txt_rect)
    game_display.blit(c2_txt_surf_obj, c2_txt_rect)
    game_display.blit(c3_txt_surf_obj, c3_txt_rect)
    pg.display.update()
    sleep(1)
    for slot, card in list(player.slot.items()):
        if card == None:
            continue
        image = pg.image.load(card + ".png")
        image_loc = slot
        game_display.blit(image, image_loc)
        pg.display.update()

    #####################################################################################################
    # draw the card at random that indicates where
    #   to start the game(initial colour and number)
    first_card = choice(cards.stack)
    while is_functional(first_card):
        first_card = choice(cards.stack)
    current_card = first_card
    update_state()
    now = pg.image.load(current_card + ".png")
    now_loc = (530, 240)
    game_display.blit(now, now_loc)
    sleep(1)
    pg.display.update()
    # select the player at random that will
    #   be the first to play
    player_list = ["p", "c1", "c2", "c3"]
    current_play = choice(player_list)
    # current_play = "p"
    game_state = 1
    return "Prepare Finished"

# is_functional(card) consumes a single Uno card
#   and determines whether the card is functional,
#   the name of the function will be returned, otherwise
#   returned False
def is_functional(card):
    return (card.endswith("reverse") or card.endswith("draw2") or card.endswith("skip") or \
            card.startswith("wild"))

# Determine whether a card can be played
def can_play(card):
    global current_card
    global current_colour
    global current_num
    global current_function
    if card.startswith("wild"):
        return True

    elif get_colour(card) == current_colour:
        return True

    elif get_number(card) == current_num:
        return True

    else:
        if not is_functional(card):
            return False
        else:
            return card.endswith(current_function) if (current_function is not None) else False

# next_player() gives the name of the
#   the next player, given the name of
#   the current player
def next_player():
    global current_play
    global order
    if order == 0:
        if current_play == "p":
            return "c1"
        elif current_play == "c1":
            return "c2"
        elif current_play == "c2":
            return "c3"
        else:
            return "p"
    else:
        if current_play == "p":
            return "c3"
        elif current_play == "c3":
            return "c2"
        elif current_play == "c2":
            return "c1"
        else:
            return "p"

# update_state() updates the constants that indicates the
#   state of the game
def update_state():

    global current_card
    global current_colour
    global current_num
    global current_function
    global order

    if is_functional(current_card):
        current_num = None
        if current_card == "wild" or current_card == "wilddraw4":
            current_function = "wild"

        for colour in ["red", "green", "yellow", "blue"]:
            if current_card.startswith(colour):
                current_colour = colour
                break

        for function in ["draw2", "reverse", "skip"]:
            if current_card.endswith(function):
                current_function = function
                break
    else:
        current_function = None

        for colour in ["red", "green", "yellow", "blue"]:
            if current_card.startswith(colour):
                current_colour = colour
                break

        for number in range(0, 10):
            if current_card.endswith(str(number)):
                current_num = str(number)
                break

# comp_valid_card(computer) consumes the name of
#   a computer player and produces a list of all
#   cards that can be played in the current round)
def comp_valid(computer):
    global current_colour
    global current_num
    global current_function
    global computer_1
    global computer_2
    global computer_3
    return list(filter(can_play, computer.have))

# get_colour(card) will give the colour of card
def get_colour(card):
    if card.startswith("wild"):
        return "-9999"
    else:
        if card.startswith("red"):
            return "red"
        elif card.startswith("blue"):
            return "blue"
        elif card.startswith("green"):
            return "green"
        else:
            return "yellow"

# get_number(card) will give the number of card
def get_number(card):
    if is_functional(card):
        return "-9999"
    else:
        last = len(card) - 1
        return card[last]

# animate_support() supports the animation when necessary
def animate_support():
    now = pg.image.load(current_card + ".png")
    now_loc = (530, 240)
    game_display.blit(now, now_loc)
    game_display.blit(background, background_loc)
    game_display.blit(cardback, card1_back_loc_fix)
    game_display.blit(cardback, card2_back_loc_fix)
    game_display.blit(cardback, card3_back_loc_fix)
    game_display.blit(c1_txt_surf_obj, c1_txt_rect)
    game_display.blit(c2_txt_surf_obj, c2_txt_rect)
    game_display.blit(c3_txt_surf_obj, c3_txt_rect)
    game_display.blit(now, now_loc)
    for slot, card in list(player.slot.items()):
        if card is None:
            continue
        image = pg.image.load(card + ".png")
        image_loc = slot
        game_display.blit(image, image_loc)
    if current_function is not None:
        if current_function.startswith("wild"):
            indicate_colour()
            pg.display.update()
    pg.display.update()

# play_card_animate(computer, card) supports the animation when necessary
#   to visualize the action of playing a card by the computer
def play_card_animate(card):
    global current_play
    image = pg.image.load(card + ".png")
    if current_play == "c1":
        card_loc = (55, 230)
        game_display.blit(image, card_loc)
        pg.display.update()
        while card_loc[1] < 240:
            animate_support()
            x = card_loc[0]
            y = card_loc[1]
            card_loc = (x, y + 5)
            game_display.blit(image, card_loc)
            pg.display.update()
        while card_loc[0] < 530:
            animate_support()
            x = card_loc[0]
            y = card_loc[1]
            card_loc = (x + 10, y)
            game_display.blit(image, card_loc)
            pg.display.update()
    elif current_play == "c2":
        card_loc = (495, 50)
        game_display.blit(image, card_loc)
        pg.display.update()
        while card_loc[1] < 240:
            animate_support()
            x = card_loc[0]
            y = card_loc[1]
            card_loc = (x, y + 10)
            game_display.blit(image, card_loc)
            pg.display.update()
        while card_loc[0] < 530:
            animate_support()
            x = card_loc[0]
            y = card_loc[1]
            card_loc = (x + 5, y)
            game_display.blit(image, card_loc)
            pg.display.update()
    else:
        card_loc = (815,230)
        game_display.blit(image, card_loc)
        pg.display.update()
        while card_loc[1] < 240:
            animate_support()
            x = card_loc[0]
            y = card_loc[1]
            card_loc = (x, y + 5)
            game_display.blit(image, card_loc)
            pg.display.update()
        while card_loc[0] > 530:
            animate_support()
            x = card_loc[0]
            y = card_loc[1]
            card_loc = (x - 10, y)
            game_display.blit(image, card_loc)
            pg.display.update()

# draw_card_animate(computer, card) supports the animation when necessary
#   to visualize the action of drawing a card by the computer
def draw_card_animate(computer, times):
    global current_card
    now = pg.image.load(current_card + ".png")
    now_loc = (530, 240)
    game_display.blit(now, now_loc)
    pg.display.update()
    i = 1
    while i <= times:
        i += 1
        image = pg.image.load("cardback.png")
        image_loc = (815, 450)
        if computer == "c1":
            card_loc = (55, 230)
            game_display.blit(image, card_loc)
            pg.display.update()
            while image_loc[1] > card_loc[1]:
                now = pg.image.load(current_card + ".png")
                now_loc = (530, 240)
                game_display.blit(now, now_loc)
                animate_support()
                x = image_loc[0]
                y = image_loc[1]
                image_loc = (x, y - 40)
                game_display.blit(image, image_loc)
                pg.display.update()
            while image_loc[0] > card_loc[0]:
                now = pg.image.load(current_card + ".png")
                now_loc = (530, 240)
                game_display.blit(now, now_loc)
                animate_support()
                x = image_loc[0]
                y = image_loc[1]
                image_loc = (x - 40, y)
                game_display.blit(image, image_loc)
                pg.display.update()
        elif computer == "c2":
            now = pg.image.load(current_card + ".png")
            now_loc = (530, 240)
            game_display.blit(now, now_loc)
            card_loc = (495, 50)
            game_display.blit(image, card_loc)
            pg.display.update()
            while image_loc[1] > card_loc[1]:
                now = pg.image.load(current_card + ".png")
                now_loc = (530, 240)
                game_display.blit(now, now_loc)
                animate_support()
                x = image_loc[0]
                y = image_loc[1]
                image_loc = (x, y - 30)
                game_display.blit(image, image_loc)
                pg.display.update()
            while image_loc[0] > card_loc[0]:
                now = pg.image.load(current_card + ".png")
                now_loc = (530, 240)
                game_display.blit(now, now_loc)
                animate_support()
                x = image_loc[0]
                y = image_loc[1]
                image_loc = (x - 30, y)
                game_display.blit(image, image_loc)
                pg.display.update()
        else:
            now = pg.image.load(current_card + ".png")
            now_loc = (530, 240)
            game_display.blit(now, now_loc)
            card_loc = (815, 230)
            game_display.blit(image, card_loc)
            pg.display.update()
            while image_loc[1] > card_loc[1]:
                now = pg.image.load(current_card + ".png")
                now_loc = (530, 240)
                game_display.blit(now, now_loc)
                animate_support()
                x = image_loc[0]
                y = image_loc[1]
                image_loc = (x, y - 10)
                game_display.blit(image, image_loc)
                pg.display.update()

# indicate_colour() indicates the colour chosen by the previous
#   who played a wild card
def indicate_colour():
    rect = (525, 235, 65, 97)
    wid = 5
    if current_colour == "red":
        pg.draw.rect(game_display, RED, rect, wid)
    if current_colour == "blue":
        pg.draw.rect(game_display, BLUE, rect, wid)
    if current_colour == "green":
        pg.draw.rect(game_display, GREEN, rect, wid)
    if current_colour == "yellow":
        pg.draw.rect(game_display, GOLD, rect, wid)

# indicate_player() indicates the current player
def indicate_player():
    global current_play
    outline = 5
    p1 = ((25, 105), (160, 105), (160, 125), (25, 125))
    p2 = ((375, 10), (515, 10), (515, 30), (375, 30))
    p3 = ((835, 85), (975, 85), (975, 110), (835, 110))
    if current_play == "c1":
        pg.draw.polygon(game_display, RED, p1, outline)
    if current_play == "c2":
        pg.draw.polygon(game_display, RED, p2, outline)
    if current_play == "c3":
        pg.draw.polygon(game_display, RED, p3, outline)
    pg.display.update()

# indicate_uno() indicates any of the players that
#  have less than two cards left
def indicate_uno():
    p1 = (150, 140)
    p2 = (300, 50)
    p3 = (760, 120)
    pp = (190, 380)
    uno_image = pg.image.load("biguno.png")
    if len(computer_1.have) <= 1:
        game_display.blit(uno_image, p1)
    if len(computer_2.have) <= 1:
        game_display.blit(uno_image, p2)
    if len(computer_3.have) <= 1:
        game_display.blit(uno_image, p3)
    if len(player.card_list) <= 1:
        game_display.blit(uno_image, pp)
    pg.display.update()

# highlight() indicates which card the mouse is currently hovering over
def highlight():
    mousex, mousey = event.pos
    if mousex in range(stack[0], stack[0] + card_height) and \
            mousey in range(stack[1], stack[1] + card_width):
        stack_ptlist = (stack, (stack[0] + card_height, stack[1]), \
                        (stack[0] + card_height, stack[1] + card_width), \
                        (stack[0], stack[1] + card_width))
        pg.draw.polygon(game_display, RED, stack_ptlist, card_outline_wid)

    if mousex in range(slot1[0], slot1[0] + card_width) and \
            mousey in range(slot1[1], slot1[1] + card_height):
        slot_ptlist = ((slot1[0], slot1[1]), (slot1[0] + card_width, slot1[1]), \
                       (slot1[0] + card_width, slot1[1] + card_height), \
                       (slot1[0], slot1[1] + card_height))
        if not player.slot.get(slot1) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot2[0], slot2[0] + card_width) and \
            mousey in range(slot2[1], slot2[1] + card_height):
        slot_ptlist = ((slot2[0], slot2[1]), (slot2[0] + card_width, slot2[1]), \
                       (slot2[0] + card_width, slot2[1] + card_height), \
                       (slot2[0], slot2[1] + card_height))
        if not player.slot.get(slot2) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot3[0], slot3[0] + card_width) and \
            mousey in range(slot3[1], slot3[1] + card_height):
        slot_ptlist = ((slot3[0], slot3[1]), (slot3[0] + card_width, slot3[1]), \
                       (slot3[0] + card_width, slot3[1] + card_height), \
                       (slot3[0], slot3[1] + card_height))
        if not player.slot.get(slot3) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot4[0], slot4[0] + card_width) and \
            mousey in range(slot4[1], slot4[1] + card_height):
        slot_ptlist = ((slot4[0], slot4[1]), (slot4[0] + card_width, slot4[1]), \
                       (slot4[0] + card_width, slot4[1] + card_height), \
                       (slot4[0], slot4[1] + card_height))
        if not player.slot.get(slot4) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot5[0], slot5[0] + card_width) and \
            mousey in range(slot5[1], slot5[1] + card_height):
        slot_ptlist = ((slot5[0], slot5[1]), (slot5[0] + card_width, slot5[1]), \
                       (slot5[0] + card_width, slot5[1] + card_height), \
                       (slot5[0], slot5[1] + card_height))
        if not player.slot.get(slot5) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot6[0], slot6[0] + card_width) and \
            mousey in range(slot6[1], slot6[1] + card_height):
        slot_ptlist = ((slot6[0], slot6[1]), (slot6[0] + card_width, slot6[1]), \
                       (slot6[0] + card_width, slot6[1] + card_height), \
                       (slot6[0], slot6[1] + card_height))
        if not player.slot.get(slot6) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot7[0], slot7[0] + card_width) and \
            mousey in range(slot7[1], slot7[1] + card_height):
        slot_ptlist = ((slot7[0], slot7[1]), (slot7[0] + card_width, slot7[1]), \
                       (slot7[0] + card_width, slot7[1] + card_height), \
                       (slot7[0], slot7[1] + card_height))
        if not player.slot.get(slot7) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot8[0], slot8[0] + card_width) and \
            mousey in range(slot8[1], slot8[1] + card_height):
        slot_ptlist = ((slot8[0], slot8[1]), (slot8[0] + card_width, slot8[1]), \
                       (slot8[0] + card_width, slot8[1] + card_height), \
                       (slot8[0], slot8[1] + card_height))
        if not player.slot.get(slot8) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot9[0], slot9[0] + card_width) and \
            mousey in range(slot9[1], slot9[1] + card_height):
        slot_ptlist = ((slot9[0], slot9[1]), (slot9[0] + card_width, slot9[1]), \
                       (slot9[0] + card_width, slot9[1] + card_height), \
                       (slot9[0], slot9[1] + card_height))
        if not player.slot.get(slot9) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot10[0], slot10[0] + card_width) and \
            mousey in range(slot10[1], slot10[1] + card_height):
        slot_ptlist = ((slot10[0], slot10[1]), (slot10[0] + card_width, slot10[1]), \
                       (slot10[0] + card_width, slot10[1] + card_height), \
                       (slot10[0], slot10[1] + card_height))
        if not player.slot.get(slot10) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot11[0], slot11[0] + card_width) and \
            mousey in range(slot11[1], slot11[1] + card_height):
        slot_ptlist = ((slot11[0], slot11[1]), (slot11[0] + card_width, slot11[1]), \
                       (slot11[0] + card_width, slot11[1] + card_height), \
                       (slot11[0], slot11[1] + card_height))
        if not player.slot.get(slot11) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot12[0], slot12[0] + card_width) and \
            mousey in range(slot12[1], slot12[1] + card_height):
        slot_ptlist = ((slot12[0], slot12[1]), (slot12[0] + card_width, slot12[1]), \
                       (slot12[0] + card_width, slot12[1] + card_height), \
                       (slot12[0], slot12[1] + card_height))
        if not player.slot.get(slot12) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot13[0], slot13[0] + card_width) and \
            mousey in range(slot13[1], slot13[1] + card_height):
        slot_ptlist = ((slot13[0], slot13[1]), (slot13[0] + card_width, slot13[1]), \
                       (slot13[0] + card_width, slot13[1] + card_height), \
                       (slot13[0], slot13[1] + card_height))
        if not player.slot.get(slot13) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot14[0], slot14[0] + card_width) and \
            mousey in range(slot14[1], slot14[1] + card_height):
        slot_ptlist = ((slot14[0], slot14[1]), (slot14[0] + card_width, slot14[1]), \
                       (slot14[0] + card_width, slot14[1] + card_height), \
                       (slot14[0], slot14[1] + card_height))
        if not player.slot.get(slot14) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot15[0], slot15[0] + card_width) and \
            mousey in range(slot15[1], slot15[1] + card_height):
        slot_ptlist = ((slot15[0], slot15[1]), (slot15[0] + card_width, slot15[1]), \
                       (slot15[0] + card_width, slot15[1] + card_height), \
                       (slot15[0], slot15[1] + card_height))
        if not player.slot.get(slot15) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot16[0], slot16[0] + card_width) and \
            mousey in range(slot16[1], slot16[1] + card_height):
        slot_ptlist = ((slot16[0], slot16[1]), (slot16[0] + card_width, slot16[1]), \
                       (slot16[0] + card_width, slot16[1] + card_height), \
                       (slot16[0], slot16[1] + card_height))
        if not player.slot.get(slot16) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot17[0], slot17[0] + card_width) and \
            mousey in range(slot17[1], slot17[1] + card_height):
        slot_ptlist = ((slot17[0], slot17[1]), (slot17[0] + card_width, slot17[1]), \
                       (slot17[0] + card_width, slot17[1] + card_height), \
                       (slot17[0], slot17[1] + card_height))
        if not player.slot.get(slot17) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot18[0], slot18[0] + card_width) and \
            mousey in range(slot18[1], slot18[1] + card_height):
        slot_ptlist = ((slot18[0], slot18[1]), (slot18[0] + card_width, slot18[1]), \
                       (slot18[0] + card_width, slot18[1] + card_height), \
                       (slot18[0], slot18[1] + card_height))
        if not player.slot.get(slot18) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot19[0], slot19[0] + card_width) and \
            mousey in range(slot19[1], slot19[1] + card_height):
        slot_ptlist = ((slot19[0], slot19[1]), (slot19[0] + card_width, slot19[1]), \
                       (slot19[0] + card_width, slot19[1] + card_height), \
                       (slot19[0], slot19[1] + card_height))
        if not player.slot.get(slot19) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

    if mousex in range(slot20[0], slot20[0] + card_width) and \
            mousey in range(slot20[1], slot20[1] + card_height):
        slot_ptlist = ((slot20[0], slot20[1]), (slot20[0] + card_width, slot20[1]), \
                       (slot20[0] + card_width, slot20[1] + card_height), \
                       (slot20[0], slot20[1] + card_height))
        if not player.slot.get(slot20) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)

# click() will play a card when the mouse is clicked while
#   hovering over a card
def click():
    global current_card
    mousex, mousey = event.pos
    if mousex in range(stack[0], stack[0] + card_height) and \
            mousey in range(stack[1], stack[1] + card_width):
        # print("Player drew a card")
        player.drew = True
        player.drew_pos, player.drew_card = player.player_draw(cards, 1)

    if mousex in range(slot1[0], slot1[0] + card_width) and \
            mousey in range(slot1[1], slot1[1] + card_height):
        slot_ptlist = ((slot1[0], slot1[1]), (slot1[0] + card_width, slot1[1]), \
                       (slot1[0] + card_width, slot1[1] + card_height), \
                       (slot1[0], slot1[1] + card_height))
        if not player.slot.get(slot1) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot1)):
                current_card = player.slot.get(slot1)
                player.play_hand(slot1)
                player.played = True

    if mousex in range(slot2[0], slot2[0] + card_width) and \
            mousey in range(slot2[1], slot2[1] + card_height):
        slot_ptlist = ((slot2[0], slot2[1]), (slot2[0] + card_width, slot2[1]), \
                       (slot2[0] + card_width, slot2[1] + card_height), \
                       (slot2[0], slot2[1] + card_height))
        if not player.slot.get(slot2) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot2)):
                current_card = player.slot.get(slot2)
                player.play_hand(slot2)
                player.played = True

    if mousex in range(slot3[0], slot3[0] + card_width) and \
            mousey in range(slot3[1], slot3[1] + card_height):
        slot_ptlist = ((slot3[0], slot3[1]), (slot3[0] + card_width, slot3[1]), \
                       (slot3[0] + card_width, slot3[1] + card_height), \
                       (slot3[0], slot3[1] + card_height))
        if not player.slot.get(slot3) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot3)):
                current_card = player.slot.get(slot3)
                player.play_hand(slot3)
                player.played = True

    if mousex in range(slot4[0], slot4[0] + card_width) and \
            mousey in range(slot4[1], slot4[1] + card_height):
        slot_ptlist = ((slot4[0], slot4[1]), (slot4[0] + card_width, slot4[1]), \
                       (slot4[0] + card_width, slot4[1] + card_height), \
                       (slot4[0], slot4[1] + card_height))
        if not player.slot.get(slot4) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot4)):
                current_card = player.slot.get(slot4)
                player.play_hand(slot4)
                player.played = True

    if mousex in range(slot5[0], slot5[0] + card_width) and \
            mousey in range(slot5[1], slot5[1] + card_height):
        slot_ptlist = ((slot5[0], slot5[1]), (slot5[0] + card_width, slot5[1]), \
                       (slot5[0] + card_width, slot5[1] + card_height), \
                       (slot5[0], slot5[1] + card_height))
        if not player.slot.get(slot5) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot5)):
                current_card = player.slot.get(slot5)
                player.play_hand(slot5)
                player.played = True

    if mousex in range(slot6[0], slot6[0] + card_width) and \
            mousey in range(slot6[1], slot6[1] + card_height):
        slot_ptlist = ((slot6[0], slot6[1]), (slot6[0] + card_width, slot6[1]), \
                       (slot6[0] + card_width, slot6[1] + card_height), \
                       (slot6[0], slot6[1] + card_height))
        if not player.slot.get(slot6) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot6)):
                current_card = player.slot.get(slot6)
                player.play_hand(slot6)
                player.played = True

    if mousex in range(slot7[0], slot7[0] + card_width) and \
            mousey in range(slot7[1], slot7[1] + card_height):
        slot_ptlist = ((slot7[0], slot7[1]), (slot7[0] + card_width, slot7[1]), \
                       (slot7[0] + card_width, slot7[1] + card_height), \
                       (slot7[0], slot7[1] + card_height))
        if not player.slot.get(slot7) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot7)):
                current_card = player.slot.get(slot7)
                player.play_hand(slot7)
                player.played = True

    if mousex in range(slot8[0], slot8[0] + card_width) and \
            mousey in range(slot8[1], slot8[1] + card_height):
        slot_ptlist = ((slot8[0], slot8[1]), (slot8[0] + card_width, slot8[1]), \
                       (slot8[0] + card_width, slot8[1] + card_height), \
                       (slot8[0], slot8[1] + card_height))
        if not player.slot.get(slot8) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot8)):
                current_card = player.slot.get(slot8)
                player.play_hand(slot8)
                player.played = True

    if mousex in range(slot9[0], slot9[0] + card_width) and \
            mousey in range(slot9[1], slot9[1] + card_height):
        slot_ptlist = ((slot9[0], slot9[1]), (slot9[0] + card_width, slot9[1]), \
                       (slot9[0] + card_width, slot9[1] + card_height), \
                       (slot9[0], slot9[1] + card_height))
        if not player.slot.get(slot9) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot9)):
                current_card = player.slot.get(slot9)
                player.play_hand(slot9)
                player.played = True

    if mousex in range(slot10[0], slot10[0] + card_width) and \
            mousey in range(slot10[1], slot10[1] + card_height):
        slot_ptlist = ((slot10[0], slot10[1]), (slot10[0] + card_width, slot10[1]), \
                       (slot10[0] + card_width, slot10[1] + card_height), \
                       (slot10[0], slot10[1] + card_height))
        if not player.slot.get(slot10) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot10)):
                current_card = player.slot.get(slot10)
                player.play_hand(slot10)
                player.played = True

    if mousex in range(slot11[0], slot11[0] + card_width) and \
            mousey in range(slot11[1], slot11[1] + card_height):
        slot_ptlist = ((slot11[0], slot11[1]), (slot11[0] + card_width, slot11[1]), \
                       (slot11[0] + card_width, slot11[1] + card_height), \
                       (slot11[0], slot11[1] + card_height))
        if not player.slot.get(slot11) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot11)):
                current_card = player.slot.get(slot11)
                player.play_hand(slot11)
                player.played = True

    if mousex in range(slot12[0], slot12[0] + card_width) and \
            mousey in range(slot12[1], slot12[1] + card_height):
        slot_ptlist = ((slot12[0], slot12[1]), (slot12[0] + card_width, slot12[1]), \
                       (slot12[0] + card_width, slot12[1] + card_height), \
                       (slot12[0], slot12[1] + card_height))
        if not player.slot.get(slot12) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot12)):
                current_card = player.slot.get(slot12)
                player.play_hand(slot12)
                player.played = True

    if mousex in range(slot13[0], slot13[0] + card_width) and \
            mousey in range(slot13[1], slot13[1] + card_height):
        slot_ptlist = ((slot13[0], slot13[1]), (slot13[0] + card_width, slot13[1]), \
                       (slot13[0] + card_width, slot13[1] + card_height), \
                       (slot13[0], slot13[1] + card_height))
        if not player.slot.get(slot13) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot13)):
                current_card = player.slot.get(slot13)
                player.play_hand(slot13)
                player.played = True

    if mousex in range(slot14[0], slot14[0] + card_width) and \
            mousey in range(slot14[1], slot14[1] + card_height):
        slot_ptlist = ((slot14[0], slot14[1]), (slot14[0] + card_width, slot14[1]), \
                       (slot14[0] + card_width, slot14[1] + card_height), \
                       (slot14[0], slot14[1] + card_height))
        if not player.slot.get(slot14) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot14)):
                current_card = player.slot.get(slot14)
                player.play_hand(slot14)
                player.played = True

    if mousex in range(slot15[0], slot15[0] + card_width) and \
            mousey in range(slot15[1], slot15[1] + card_height):
        slot_ptlist = ((slot15[0], slot15[1]), (slot15[0] + card_width, slot15[1]), \
                       (slot15[0] + card_width, slot15[1] + card_height), \
                       (slot15[0], slot15[1] + card_height))
        if not player.slot.get(slot15) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot15)):
                current_card = player.slot.get(slot15)
                player.play_hand(slot15)
                player.played = True

    if mousex in range(slot16[0], slot16[0] + card_width) and \
            mousey in range(slot16[1], slot16[1] + card_height):
        slot_ptlist = ((slot16[0], slot16[1]), (slot16[0] + card_width, slot16[1]), \
                       (slot16[0] + card_width, slot16[1] + card_height), \
                       (slot16[0], slot16[1] + card_height))
        if not player.slot.get(slot16) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot16)):
                current_card = player.slot.get(slot16)
                player.play_hand(slot16)
                player.played = True

    if mousex in range(slot17[0], slot17[0] + card_width) and \
            mousey in range(slot17[1], slot17[1] + card_height):
        slot_ptlist = ((slot17[0], slot17[1]), (slot17[0] + card_width, slot17[1]), \
                       (slot17[0] + card_width, slot17[1] + card_height), \
                       (slot17[0], slot17[1] + card_height))
        if not player.slot.get(slot17) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot17)):
                current_card = player.slot.get(slot17)
                player.play_hand(slot17)
                player.played = True

    if mousex in range(slot18[0], slot18[0] + card_width) and \
            mousey in range(slot18[1], slot18[1] + card_height):
        slot_ptlist = ((slot18[0], slot18[1]), (slot18[0] + card_width, slot18[1]), \
                       (slot18[0] + card_width, slot18[1] + card_height), \
                       (slot18[0], slot18[1] + card_height))
        if not player.slot.get(slot18) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot18)):
                current_card = player.slot.get(slot18)
                player.play_hand(slot18)
                player.played = True

    if mousex in range(slot19[0], slot19[0] + card_width) and \
            mousey in range(slot19[1], slot19[1] + card_height):
        slot_ptlist = ((slot19[0], slot19[1]), (slot19[0] + card_width, slot19[1]), \
                       (slot19[0] + card_width, slot19[1] + card_height), \
                       (slot19[0], slot19[1] + card_height))
        if not player.slot.get(slot19) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot19)):
                current_card = player.slot.get(slot19)
                player.play_hand(slot19)
                player.played = True

    if mousex in range(slot20[0], slot20[0] + card_width) and \
            mousey in range(slot20[1], slot20[1] + card_height):
        slot_ptlist = ((slot20[0], slot20[1]), (slot20[0] + card_width, slot20[1]), \
                       (slot20[0] + card_width, slot20[1] + card_height), \
                       (slot20[0], slot20[1] + card_height))
        if not player.slot.get(slot20) is None:
            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
            if can_play(player.slot.get(slot20)):
                current_card = player.slot.get(slot20)
                player.play_hand(slot20)
                player.played = True

# c1_play() simulates the behaviour of computer 1
def c1_play():
    global current_card
    global current_colour
    global current_play
    global current_num
    global current_function
    global order
    if not comp_valid(computer_1):
        card1_back_loc = (815, 450)
        computer_1.computer_draw(cards, 1)
        pg.display.update()
        current_play = next_player()
        while card1_back_loc[1] > 230:
            animate_support()
            x = card1_back_loc[0]
            y = card1_back_loc[1]
            card1_back_loc = (x, y - 40)
            game_display.blit(cardback, card1_back_loc)
            pg.display.update()
        while card1_back_loc[0] > 75:
            animate_support()
            x = card1_back_loc[0]
            y = card1_back_loc[1]
            card1_back_loc = (x - 40, y)
            game_display.blit(cardback, card1_back_loc)
            pg.display.update()
        pg.display.update()

    else:
        comp_played = computer_1.play_hand(choice(comp_valid(computer_1)))
        current_card = comp_played
        now = pg.image.load(current_card + ".png")
        now_loc = (530, 240)
        game_display.blit(now, now_loc)
        play_card_animate(comp_played)
        pg.display.update()
        if is_functional(comp_played):
            if not comp_played.startswith("wild"):
                current_num = None
                if comp_played.endswith("reverse"):
                    order = 1 if order == 0 else 0
                    current_colour = get_colour(comp_played)
                    current_function = "reverse"
                    current_play = next_player()
                    pg.display.update()
                elif comp_played.endswith("skip"):
                    current_colour = get_colour(comp_played)
                    current_function = "skip"
                    current_play = next_player()
                    current_play = next_player()
                    pg.display.update()
                elif comp_played.endswith("draw2"):
                    current_colour = get_colour(comp_played)
                    current_function = "draw2"
                    current_play = next_player()
                    now = pg.image.load(current_card + ".png")
                    now_loc = (530, 240)
                    game_display.blit(now, now_loc)
                    pg.display.update()
                    if current_play == "c2":
                        computer_2.computer_draw(cards, 2)
                        draw_card_animate("c2", 2)
                    else:
                        player.player_draw(cards, 2)
                    current_play = next_player()
                    pg.display.update()

            else:
                if comp_played == "wild":
                    current_num = None
                    current_function = "wild"
                    current_colour = choice(["green", "yellow", "blue", "red"])
                    current_play = next_player()
                    indicate_colour()
                    pg.display.update()

                # comp_played == "wilddraw4"
                else:
                    current_num = None
                    current_function = "wilddraw4"
                    current_colour = choice(["green", "yellow", "blue", "red"])
                    current_play = next_player()
                    now = pg.image.load(current_card + ".png")
                    now_loc = (530, 240)
                    game_display.blit(now, now_loc)
                    pg.display.update()
                    if current_play == "c2":
                        computer_2.computer_draw(cards, 4)
                        draw_card_animate("c2", 4)
                    else:
                        player.player_draw(cards, 4)
                    current_play = next_player()
                    indicate_colour()
                    pg.display.update()

        # otherwise pure number card
        else:
            current_function = None
            current_colour = get_colour(comp_played)
            current_num = get_number(comp_played)
            current_play = next_player()
            pg.display.update()

# c2_play() simulates the behaviour of computer 2
def c2_play():
    global current_card
    global current_colour
    global current_play
    global current_num
    global current_function
    global order
    if not comp_valid(computer_2):
        card2_back_loc = (815, 450)
        computer_2.computer_draw(cards, 1)
        pg.display.update()
        current_play = next_player()
        while card2_back_loc[1] > 55:
            animate_support()
            x = card2_back_loc[0]
            y = card2_back_loc[1]
            card2_back_loc = (x, y - 40)
            game_display.blit(cardback, card2_back_loc)
            pg.display.update()
        while card2_back_loc[0] > 500:
            animate_support()
            x = card2_back_loc[0]
            y = card2_back_loc[1]
            card2_back_loc = (x - 40, y)
            game_display.blit(cardback, card2_back_loc)
            pg.display.update()
        pg.display.update()

    else:
        comp_played = computer_2.play_hand(choice(comp_valid(computer_2)))
        current_card = comp_played
        now = pg.image.load(current_card + ".png")
        now_loc = (530, 240)
        game_display.blit(now, now_loc)
        play_card_animate(comp_played)
        pg.display.update()
        if is_functional(comp_played):
            if not comp_played.startswith("wild"):
                current_num = None
                if comp_played.endswith("reverse"):
                    order = 1 if order == 0 else 0
                    current_colour = get_colour(comp_played)
                    current_function = "reverse"
                    current_play = next_player()
                    pg.display.update()

                elif comp_played.endswith("skip"):
                    current_colour = get_colour(comp_played)
                    current_function = "skip"
                    current_play = next_player()
                    current_play = next_player()
                    pg.display.update()

                elif comp_played.endswith("draw2"):
                    current_colour = get_colour(comp_played)
                    current_function = "draw2"
                    current_play = next_player()
                    now = pg.image.load(current_card + ".png")
                    now_loc = (530, 240)
                    game_display.blit(now, now_loc)
                    pg.display.update()
                    if current_play == "c3":
                        computer_3.computer_draw(cards, 2)
                        draw_card_animate("c3", 2)
                    else:
                        computer_1.computer_draw(cards, 2)
                        draw_card_animate("c1", 2)
                    current_play = next_player()
                    pg.display.update()

            else:
                if comp_played == "wild":
                    current_num = None
                    current_function = "wild"
                    current_colour = choice(["green", "yellow", "blue", "red"])
                    current_play = next_player()
                    indicate_colour()
                    pg.display.update()

                # comp_played == "wilddraw4"
                else:
                    current_num = None
                    current_function = "wilddraw4"
                    current_colour = choice(["green", "yellow", "blue", "red"])
                    current_play = next_player()
                    now = pg.image.load(current_card + ".png")
                    now_loc = (530, 240)
                    game_display.blit(now, now_loc)
                    pg.display.update()
                    if current_play == "c3":
                        computer_3.computer_draw(cards, 4)
                        draw_card_animate("c3", 4)
                    else:
                        computer_1.computer_draw(cards, 4)
                        draw_card_animate("c1", 4)
                    current_play = next_player()
                    indicate_colour()
                    pg.display.update()

        # otherwise pure number card
        else:
            current_function = None
            current_colour = get_colour(comp_played)
            current_num = get_number(comp_played)
            current_play = next_player()
            pg.display.update()

# c3_play() simulates the behaviour of computer 3
def c3_play():
    global current_card
    global current_colour
    global current_play
    global current_num
    global current_function
    global order
    if not comp_valid(computer_3):
        card3_back_loc = (815, 450)
        computer_3.computer_draw(cards, 1)
        pg.display.update()
        current_play = next_player()
        while card3_back_loc[1] > 240:
            animate_support()
            x = card3_back_loc[0]
            y = card3_back_loc[1]
            card3_back_loc = (x, y - 20)
            game_display.blit(cardback, card3_back_loc)
            pg.display.update()
        while card3_back_loc[0] > 910:
            animate_support()
            x = card3_back_loc[0]
            y = card3_back_loc[1]
            card3_back_loc = (x - 20, y)
            game_display.blit(cardback, card3_back_loc)
            pg.display.update()
        pg.display.update()

    else:
        comp_played = computer_3.play_hand(choice(comp_valid(computer_3)))
        current_card = comp_played
        now = pg.image.load(current_card + ".png")
        now_loc = (530, 240)
        game_display.blit(now, now_loc)
        play_card_animate(comp_played)
        pg.display.update()
        #sleep(2)
        if is_functional(comp_played):
            if not comp_played.startswith("wild"):
                current_num = None
                if comp_played.endswith("reverse"):
                    order = 1 if order == 0 else 0
                    current_colour = get_colour(comp_played)
                    current_function = "reverse"
                    current_play = next_player()
                    pg.display.update()

                elif comp_played.endswith("skip"):
                    current_colour = get_colour(comp_played)
                    current_function = "skip"
                    current_play = next_player()
                    current_play = next_player()
                    pg.display.update()

                elif comp_played.endswith("draw2"):
                    current_colour = get_colour(comp_played)
                    current_function = "draw2"
                    current_play = next_player()
                    now = pg.image.load(current_card + ".png")
                    now_loc = (530, 240)
                    game_display.blit(now, now_loc)
                    pg.display.update()
                    if current_play == "c2":
                        computer_2.computer_draw(cards, 2)
                        draw_card_animate("c2", 2)
                    else:
                        player.player_draw(cards, 2)
                    current_play = next_player()
                    pg.display.update()

            else:
                if comp_played == "wild":
                    current_num = None
                    current_function = "wild"
                    current_colour = choice(["green", "yellow", "blue", "red"])
                    current_play = next_player()
                    indicate_colour()
                    pg.display.update()

                # comp_played == "wilddraw4"
                else:
                    current_num = None
                    current_function = "wilddraw4"
                    current_colour = choice(["green", "yellow", "blue", "red"])
                    current_play = next_player()
                    now = pg.image.load(current_card + ".png")
                    now_loc = (530, 240)
                    game_display.blit(now, now_loc)
                    pg.display.update()
                    if current_play == "c2":
                        computer_2.computer_draw(cards, 4)
                        draw_card_animate("c2", 4)
                    else:
                        player.player_draw(cards, 4)
                    current_play = next_player()
                    indicate_colour()
                    pg.display.update()

        # otherwise pure number card
        else:
            current_function = None
            current_colour = get_colour(comp_played)
            current_num = get_number(comp_played)
            current_play = next_player()
            pg.display.update()

# winner_exists() will check to see if there is a winner
def winner_exists():
    global game_state
    if game_state == 1:
        if not computer_1.have or not computer_2.have or not computer_3.have or not player.card_list:
            return True
    else:
        return False

# win_or_lose() will indicate whether the player won or not
def win_or_lose():
    if not computer_1.have or not computer_2.have or not computer_3.have:
        return "lose"
    if not player.card_list:
        return "win"



# The following sets up the game

# This section sets up the classes UnoCard that represents all the cards in Uno,
#   CardStack that represents the card stack during the game,
#   Player that represents the real player,
#   and Computer that represents the computer

class UnoCard:

    # The cards are stored in lists, where the coloured cards are stored
    #   in two-element list, where the first element represents the colour
    #   and the second element represents the number or the function; the
    #   wild cards are stored as strings which are the names of the card
    # Examples: "red", 1              => a red card of number 1
    #           "green", 5            => a green card of number 5
    #           "yellowreverse"   => a yellow card of reverse
    #           "wild draw"                  => a wild-draw-4 card
    # Notes: there are a total of 108 colour cards, 25 in each colour
    #        and 8 wild cards
    def __init__(self):
        self.red = ["red0", "red1", "red1", "red2",
                    "red2", "red3", "red3", "red4",
                    "red4", "red5", "red5", "red6",
                    "red6", "red7", "red7", "red8",
                    "red8", "red9", "red9", "redskip",
                    "redskip", "redreverse", "redreverse",
                    "reddraw2", "reddraw2"]

        self.blue = ["blue0", "blue1", "blue1", "blue2",
                     "blue2", "blue3", "blue3", "blue4",
                     "blue4", "blue5", "blue5", "blue6",
                     "blue6", "blue7", "blue7", "blue8",
                     "blue8", "blue9", "blue9", "blueskip",
                     "blueskip", "bluereverse", "bluereverse",
                     "bluedraw2", "bluedraw2"]

        self.green = ["green0", "green1", "green1", "green2",
                      "green2", "green3", "green3", "green4",
                      "green4", "green5", "green5", "green6",
                      "green6", "green7", "green7", "green8",
                      "green8", "green9", "green9", "greenskip",
                      "greenskip", "greenreverse", "greenreverse",
                      "greendraw2", "greendraw2"]

        self.yellow = ["yellow0", "yellow1", "yellow1", "yellow2",
                       "yellow2", "yellow3", "yellow3", "yellow4",
                       "yellow4", "yellow5", "yellow5", "yellow6",
                       "yellow6", "yellow7", "yellow7", "yellow8",
                       "yellow8", "yellow9", "yellow9", "yellowskip",
                       "yellowskip", "yellowreverse", "yellowreverse",
                       "yellowdraw2", "yellowdraw2"]

        self.wild = ["wild", "wild", "wild", "wild",
                     "wilddraw4", "wilddraw4", "wilddraw4", "wilddraw4"]


class CardStack:
    def __init__(self):
        self.stack = []
        card = UnoCard()
        self.stack.extend(card.red)
        self.stack.extend(card.blue)
        self.stack.extend(card.green)
        self.stack.extend(card.yellow)
        self.stack.extend(card.wild)

    # length() gives the number of cards (elements)
    #   in the card stack
    def length(self):
        return len(self.stack)

    # show_stack() prints out the entire card stack
    # effects: print => produces output
    def show(self):
        print(self.stack)

    # randomize() reorders all cards in card stack
    def randomize(self):
        return shuffle(self.stack)

    # draw() draws the card at the top of the stack (the last element)
    def draw(self):
        if not self.stack:
            card = UnoCard()
            self.stack.extend(card.red)
            self.stack.extend(card.blue)
            self.stack.extend(card.green)
            self.stack.extend(card.yellow)
            self.stack.extend(card.wild)
        return self.stack.pop()


class Player:
    def __init__(self):
        self.drew = False
        self.drew_pos = None
        self.drew_card = None
        self.played = False
        self.slot = {(30, 410): None, (90, 410): None, (150, 410): None, (210, 410): None, (270, 410): None, \
                     (330, 410): None, (390, 410): None, (450, 410): None, (510, 410): None, (570, 410): None, \
                     (30, 500): None, (90, 500): None, (150, 500): None, (210, 500): None, (270, 500): None, \
                     (330, 500): None, (390, 500): None, (450, 500): None, (510, 500): None, (570, 500): None}
        self.card_list = []

    def player_draw(self, stack, times):
        while times > 0:
            add = stack.draw()
            pos = None
            times -= 1
            for key, val in self.slot.items():
                if not val is None:
                    continue
                pos = key
                self.slot.update({key: add})
                self.card_list.append(add)
                break
            if times == 0:
                return pos, add

    # show_have() shows all the player's cards
    def show_slot(self):
        print(self.slot)

    # play_hand(card) plays the given card
    def play_hand(self, key):
        to_remove = self.slot.get(key)
        self.slot.update({key: None})
        self.card_list.remove(to_remove)
        return key


class Computer:
    def __init__(self):
        self.have = []  # the cards that the player is curtently holding

    # computer_draw(stack) draws a card from stack for the given number of times
    def computer_draw(self, stack, times):
        while times > 0:
            self.have.append(stack.draw())
            times -= 1

    # show_have() shows all the computer's cards
    def show_have(self):
        print(self.have)

    # play_hand(valid) plays the given card(namely valid)
    def play_hand(self, valid):
        self.have.remove(valid)
        return valid


###########################################################################################################
###########################################################################################################

# the game initializes
pg.init()

# The name of the card that was played
current_card = None

# game_state indicates the state of the game
# Notes: 0 => game not started
#        1 => game started
#        2 => game finished
#        3 => preparing
#        4 => Ending (Freezing)
game_state = 0

# cards represent the remaining cards
#   that are not drew
cards = CardStack()

# player represents the real player
player = Player()

# computer_1, computer_2, computer_3
#   represents the computer
computer_1 = Computer()
computer_2 = Computer()
computer_3 = Computer()

# current_colour represents the colour
#   on the card after a player has played
#   a card, if the card is a function card
#   then a value of None is given
# Notes: "red"    => red card
#        "blue"   => blue card
#        "green"  => green card
#        "yellow" => yellow card
current_colour = None

# current_num represents the number on the
#   card as string after a player has played
#   a card, if the card is a function card
#   then a value of None is given
current_num = None

# current_play represents the player
#   that will play the card in the
#   current round, before the game
#   started, a value of None is given
# Notes: "p"  => real player
#        "c1" => computer_1
#        "c2" => computer_2
#        "c3" => computer_3
current_play = None

# current_play represents the function of
#   the played card from last round
# Notes:  None     => not a functional card
#        "reverse" => a reverse card
#        "skip"    => a skip card
#        "draw 2"  => a draw 2
#        "wild"    => a wild
#        "wild draw 4" => a wild-draw-4
current_function = None

# order indicates the order in which the
#  the players play the game
# Notes: 0 => clockwise, default
#        1 => counter-clockwise
order = 0

# Set up frame per second in the game
FPS = 15
fpsClock = pg.time.Clock()

# Set up the gaming window
game_display = pg.display.set_mode((1000, 600), 0, 32)

# Colour in RGB format
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
RED = (238, 44, 44)
BLUE = (0, 0, 205)
GREEN = (154, 205, 50)

while True:
    if winner_exists():
        pg.display.update()
        sleep(3)
        game_state = 2
    if game_state == 2:
        c1_txt_surf_obj = c1_txt_font.render('X %d' % len(computer_1.have), True, BLACK)
        c2_txt_surf_obj = c2_txt_font.render('X %d' % len(computer_2.have), True, BLACK)
        c3_txt_surf_obj = c3_txt_font.render('X %d' % len(computer_3.have), True, BLACK)
        animate_support()
        message_loc = (300, 200)
        if win_or_lose() == "win":
            win_message = pg.image.load("win.png")
            game_display.blit(win_message, message_loc)
        if win_or_lose() == "lose":
            lose_message = pg.image.load("lose.png")
            game_display.blit(lose_message, message_loc)
        pg.display.update()
        game_state = 4
    if game_state == 4:
        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN:
                sleep(1)
                terminate()
    for event in pg.event.get():
        if event.type == QUIT:
            terminate()
        if not cards:
            cards = CardStack()
            cards.randomize()
        if game_state == 0:
            start()
            pg.display.update()
        elif game_state == 3:
            prepare()
            sleep(2)
        if game_state == 2:
            c1_txt_surf_obj = c1_txt_font.render('X %d' % len(computer_1.have), True, BLACK)
            c2_txt_surf_obj = c2_txt_font.render('X %d' % len(computer_2.have), True, BLACK)
            c3_txt_surf_obj = c3_txt_font.render('X %d' % len(computer_3.have), True, BLACK)
            animate_support()
            message_loc = (300, 200)
            if win_or_lose() == "win":
                win_message = pg.image.load("win.png")
                game_display.blit(win_message, message_loc)
            if win_or_lose() == "lose":
                lose_message = pg.image.load("lose.png")
                game_display.blit(lose_message, message_loc)
            pg.display.update()
            game_state = 4
        elif game_state == 4:
            if event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN:
                sleep(1)
                terminate()
        if game_state == 1 and current_play == "p":
            background = pg.image.load('background.png')
            background_loc = (0, 0)
            cardback = pg.image.load('cardback.png')
            textsize = 25
            textfont = 'arial'
            card1_back_loc_fix = (55, 230)
            card2_back_loc_fix = (495, 50)
            card3_back_loc_fix = (815, 230)
            c1_card_x = 150
            c1_card_y = 270
            c1_txt_font = pg.font.SysFont(textfont, textsize)
            c1_txt_surf_obj = c1_txt_font.render('X %d' % len(computer_1.have), True, BLACK)
            c1_txt_rect = c1_txt_surf_obj.get_rect()
            c1_txt_rect.center = (c1_card_x, c1_card_y)
            c2_card_x = 580
            c2_card_y = 95
            c2_txt_font = pg.font.SysFont(textfont, textsize)
            c2_txt_surf_obj = c2_txt_font.render('X %d' % len(computer_2.have), True, BLACK)
            c2_txt_rect = c2_txt_surf_obj.get_rect()
            c2_txt_rect.center = (c2_card_x, c2_card_y)
            c3_card_x = 920
            c3_card_y = 250
            c3_txt_font = pg.font.SysFont(textfont, textsize)
            c3_txt_surf_obj = c3_txt_font.render('X %d' % len(computer_3.have), True, BLACK)
            c3_txt_rect = c3_txt_surf_obj.get_rect()
            c3_txt_rect.center = (c3_card_x, c3_card_y)
            now = pg.image.load(current_card + ".png")
            now_loc = (530, 240)
            animate_support()
            if player.played and current_card.startswith("wild"):
                asksize = 20
                ask_card_x = 270
                ask_card_y = 330
                ask_wid = 80
                ask_height = 45
                txt_font = pg.font.SysFont(textfont, asksize)
                ask_txt_surf_obj = txt_font.render('Please select colour by pressing on the keyboard:', True, BLACK,
                                                   WHITE)
                ans_txt_surf_obj = txt_font.render('<R>: RED  <B>: BLUE  <G>: GREEN  <Y>: YELLOW', True, BLACK, WHITE)
                ask_txt_rect = ask_txt_surf_obj.get_rect()
                ask_txt_rect.center = (ask_card_x, ask_card_y)
                ans_txt_rect = ask_txt_surf_obj.get_rect()
                ans_txt_rect.center = (ask_card_x - 20, ask_card_y + ask_height)
                game_display.blit(ask_txt_surf_obj, ask_txt_rect)
                game_display.blit(ans_txt_surf_obj, ans_txt_rect)
                pg.display.update()
            if player.drew and can_play(player.drew_card):
                asksize = 20
                ask_card_x = 270
                ask_card_y = 320
                ask_wid = 80
                ask_height = 50
                txt_font = pg.font.SysFont(textfont, asksize)
                ask_txt_surf_obj = txt_font.render('Play now?', True, BLACK, WHITE)
                ans_txt_surf_obj = txt_font.render('<ENTER/RETURN>: YES |  <SPACE>: NO', True, BLACK, WHITE)
                ask_txt_rect = ask_txt_surf_obj.get_rect()
                ask_txt_rect.center = (ask_card_x, ask_card_y)
                ans_txt_rect = ask_txt_surf_obj.get_rect()
                ans_txt_rect.center = (ask_card_x - 20, ask_card_y + ask_height)
                game_display.blit(ask_txt_surf_obj, ask_txt_rect)
                game_display.blit(ans_txt_surf_obj, ans_txt_rect)
                just_drew = pg.image.load(player.drew_card + ".png")
                game_display.blit(just_drew, (ask_card_x, ask_card_y - 1.5 * card_height))
                pg.display.update()
            if current_function is not None:
                if current_function.startswith("wild"):
                    indicate_colour()
                    pg.display.update()
            indicate_uno()
            pg.display.update()
            if not player.drew and not player.played:
                card_width = 54
                card_height = 83
                slot1 = (30, 410)
                slot2 = (90, 410)
                slot3 = (150, 410)
                slot4 = (210, 410)
                slot5 = (270, 410)
                slot6 = (330, 410)
                slot7 = (390, 410)
                slot8 = (450, 410)
                slot9 = (510, 410)
                slot10 = (570, 410)
                slot11 = (30, 500)
                slot12 = (90, 500)
                slot13 = (150, 500)
                slot14 = (210, 500)
                slot15 = (270, 500)
                slot16 = (330, 500)
                slot17 = (390, 500)
                slot18 = (450, 500)
                slot19 = (510, 500)
                slot20 = (570, 500)
                stack = (780, 470)
                card_outline_wid = 5
                if event.type == MOUSEMOTION:
                    highlight()
                    pg.display.update()
                    continue
                if event.type == MOUSEBUTTONDOWN:
                    click()
                continue

            if player.played:
                now = pg.image.load(current_card + ".png")
                now_loc = (530, 240)
                game_display.blit(now, now_loc)
                pg.display.update()
                if current_card == "wild" or current_card == "wilddraw4":
                    asksize = 20
                    ask_card_x = 270
                    ask_card_y = 330
                    ask_wid = 80
                    ask_height = 45
                    txt_font = pg.font.SysFont(textfont, asksize)
                    ask_txt_surf_obj = txt_font.render('Please select colour by pressing on the keyboard:', True, BLACK, WHITE)
                    ans_txt_surf_obj = txt_font.render('<R>: RED  <B>: BLUE  <G>: GREEN  <Y>: YELLOW', True, BLACK, WHITE)
                    ask_txt_rect = ask_txt_surf_obj.get_rect()
                    ask_txt_rect.center = (ask_card_x, ask_card_y)
                    ans_txt_rect = ask_txt_surf_obj.get_rect()
                    ans_txt_rect.center = (ask_card_x - 20, ask_card_y + ask_height)
                    game_display.blit(ask_txt_surf_obj, ask_txt_rect)
                    game_display.blit(ans_txt_surf_obj, ans_txt_rect)
                    pg.display.update()
                    if event.type == MOUSEMOTION:
                        continue
                    if event.type == KEYDOWN:
                        slot_ptlist = ((530, 240), (585, 240), (585, 330), (530, 330))
                        if event.key == K_r:
                            player.played = False
                            update_state()
                            current_colour = "red"
                            pg.draw.polygon(game_display, RED, slot_ptlist, card_outline_wid)
                            pg.display.update()
                            current_play = next_player()
                        elif event.key == K_b:
                            player.played = False
                            update_state()
                            current_colour = "blue"
                            pg.draw.polygon(game_display, BLUE, slot_ptlist, card_outline_wid)
                            pg.display.update()
                            current_play = next_player()
                        elif event.key == K_g:
                            player.played = False
                            update_state()
                            current_colour = "green"
                            pg.draw.polygon(game_display, GREEN, slot_ptlist, card_outline_wid)
                            pg.display.update()
                            current_play = next_player()
                        elif event.key == K_y:
                            player.played = False
                            update_state()
                            current_colour = "yellow"
                            pg.draw.polygon(game_display, YELLOW, slot_ptlist, card_outline_wid)
                            pg.display.update()
                            current_play = next_player()

                        if current_card.endswith("draw4"):
                            now = pg.image.load(current_card + ".png")
                            now_loc = (530, 240)
                            game_display.blit(now, now_loc)
                            if current_play == "c1":
                                computer_1.computer_draw(cards, 4)
                                draw_card_animate("c1", 4)
                            else:
                                computer_3.computer_draw(cards, 4)
                                draw_card_animate("c3", 4)
                            pg.display.update()
                            current_play = next_player()

                elif current_card.endswith("reverse"):
                    order = 1 if order == 0 else 0
                    player.played = False
                    update_state()
                    pg.display.update()
                    current_play = next_player()


                elif current_card.endswith("skip"):
                    player.played = False
                    update_state()
                    pg.display.update()
                    current_play = next_player()
                    current_play = next_player()


                elif current_card.endswith("draw2"):
                    player.played = False
                    current_play = next_player()
                    if current_play == "c1":
                        computer_1.computer_draw(cards, 2)
                        draw_card_animate("c1", 2)
                    else:
                        computer_3.computer_draw(cards, 2)
                        draw_card_animate("c3", 2)
                    update_state()
                    pg.display.update()
                    current_play = next_player()


                else:
                    player.played = False
                    update_state()
                    pg.display.update()
                    current_play = next_player()
                indicate_player()
                indicate_uno()

            if player.drew:
                if can_play(player.drew_card):
                    asksize = 20
                    ask_card_x = 270
                    ask_card_y = 320
                    ask_wid = 80
                    ask_height = 50
                    txt_font = pg.font.SysFont(textfont, asksize)
                    ask_txt_surf_obj = txt_font.render('Play now?', True, BLACK, WHITE)
                    ans_txt_surf_obj = txt_font.render('<ENTER/RETURN>: YES |  <SPACE>: NO', True, BLACK, WHITE)
                    ask_txt_rect = ask_txt_surf_obj.get_rect()
                    ask_txt_rect.center = (ask_card_x, ask_card_y)
                    ans_txt_rect = ask_txt_surf_obj.get_rect()
                    ans_txt_rect.center = (ask_card_x - 20, ask_card_y + ask_height)
                    game_display.blit(ask_txt_surf_obj, ask_txt_rect)
                    game_display.blit(ans_txt_surf_obj, ans_txt_rect)
                    just_drew = pg.image.load(player.drew_card + ".png")
                    game_display.blit(just_drew, (ask_card_x, ask_card_y - 1.5 * card_height))
                    pg.display.update()
                    if event.type == MOUSEMOTION:
                        continue
                    if event.type == KEYDOWN:
                        # play the card
                        if event.key == K_RETURN:
                            player.played = True
                            current_card = player.drew_card
                            player.drew_card = None
                            player.play_hand(player.drew_pos)
                            player.drew_pos = None
                            player.drew = False

                        # do not play the card
                        if event.key == K_SPACE:
                            animate_support()
                            player.drew_card = None
                            player.drew_pos = None
                            player.drew = False
                            update_state()
                            current_play = next_player()
                            pg.display.update()
                            indicate_player()
                            indicate_uno()

                else:
                    player.drew_card = None
                    player.drew_pos = None
                    update_state()
                    player.drew = False
                    pg.display.update()
                    current_play = next_player()
                    indicate_player()
                    indicate_uno()

            if current_function is not None:
                if current_function.startswith("wild"):
                    indicate_colour()
                    pg.display.update()
            indicate_uno()
            pg.display.update()
            if winner_exists():
                sleep(3)
                game_state = 2
                continue

    if game_state == 1 and not current_play == "p":
        background = pg.image.load('background.png')
        background_loc = (0, 0)
        cardback = pg.image.load('cardback.png')
        textsize = 25
        textfont = 'arial'
        card1_back_loc_fix = (55, 230)
        card2_back_loc_fix = (495, 50)
        card3_back_loc_fix = (815, 230)
        c1_card_x = 150
        c1_card_y = 270
        c1_txt_font = pg.font.SysFont(textfont, textsize)
        c1_txt_surf_obj = c1_txt_font.render('X %d' % len(computer_1.have), True, BLACK)
        c1_txt_rect = c1_txt_surf_obj.get_rect()
        c1_txt_rect.center = (c1_card_x, c1_card_y)
        c2_card_x = 580
        c2_card_y = 95
        c2_txt_font = pg.font.SysFont(textfont, textsize)
        c2_txt_surf_obj = c2_txt_font.render('X %d' % len(computer_2.have), True, BLACK)
        c2_txt_rect = c2_txt_surf_obj.get_rect()
        c2_txt_rect.center = (c2_card_x, c2_card_y)
        c3_card_x = 920
        c3_card_y = 250
        c3_txt_font = pg.font.SysFont(textfont, textsize)
        c3_txt_surf_obj = c3_txt_font.render('X %d' % len(computer_3.have), True, BLACK)
        c3_txt_rect = c3_txt_surf_obj.get_rect()
        c3_txt_rect.center = (c3_card_x, c3_card_y)
        now = pg.image.load(current_card + ".png")
        now_loc = (530, 240)
        animate_support()
        indicate_player()
        indicate_uno()
        pg.display.update()
        sleep(3)
        if current_function is not None:
            if current_function.startswith("wild"):
                indicate_colour()
                pg.display.update()
        if current_play == "c1":
            c1_play()
            pg.display.update()
            if current_function is not None:
                if current_function.startswith("wild"):
                    indicate_colour()
                    pg.display.update()
            if not current_play == "p":
                continue
        if current_play == "c2":
            c2_play()
            pg.display.update()
            if current_function is not None:
                if current_function.startswith("wild"):
                    indicate_colour()
                    pg.display.update()
            if not current_play == "p":
                continue
        if current_play == "c3":
            c3_play()
            pg.display.update()
            if current_function is not None:
                if current_function.startswith("wild"):
                    indicate_colour()
                    pg.display.update()
            if not current_play == "p":
                continue

        if current_function is not None:
            if current_function.startswith("wild"):
                indicate_colour()
                pg.display.update()
        c1_txt_surf_obj = c1_txt_font.render('X %d' % len(computer_1.have), True, BLACK)
        c2_txt_surf_obj = c2_txt_font.render('X %d' % len(computer_2.have), True, BLACK)
        c3_txt_surf_obj = c3_txt_font.render('X %d' % len(computer_3.have), True, BLACK)
        now = pg.image.load(current_card + ".png")
        animate_support()
        indicate_player()
        indicate_uno()
        pg.display.update()


    fpsClock.tick(FPS)
###########################################################################################################
###########################################################################################################







