# importing pygame and initializing it
import random
import pygame

import HandScore
import Player
import Deck
import Card
import time
pygame.init()

# defining max width, height
WIDTH = 1200
HEIGHT = 700

# defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YCP_GREEN = (99, 100, 7)
DARK_GREEN = (99, 135, 7)
BG_TEXT = (99, 125, 7)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def draw_star(decor, screen, title):
    """draws the stars around the title"""
    screen.blit(decor, (690 - title.get_width() // 2, 310 - title.get_height() // 2))  # the top of the arc
    screen.blit(decor, (690 - title.get_width() // 2, 418 - title.get_height() // 2))  # the bottom of the arc
    screen.blit(decor, (718 - title.get_width() // 2, 312 - title.get_height() // 2))  # next to the top 1
    screen.blit(decor, (745 - title.get_width() // 2, 316 - title.get_height() // 2))  # the next one -> 2
    screen.blit(decor, (774 - title.get_width() // 2, 324 - title.get_height() // 2))  # and the next one 3
    screen.blit(decor, (798 - title.get_width() // 2, 339 - title.get_height() // 2))  # and the next one 4
    screen.blit(decor, (812 - title.get_width() // 2, 364 - title.get_height() // 2))  # middle right
    screen.blit(decor, (798 - title.get_width() // 2,
                        392 - title.get_height() // 2))  # starting to go down to the bottom pos -4
    screen.blit(decor, (774 - title.get_width() // 2, 404 - title.get_height() // 2))  # pos -3
    screen.blit(decor, (745 - title.get_width() // 2, 412 - title.get_height() // 2))  # pos -2
    screen.blit(decor, (718 - title.get_width() // 2, 416 - title.get_height() // 2))  # pos -1
    # starting to go around the other half of the circle
    screen.blit(decor, (660 - title.get_width() // 2, 312 - title.get_height() // 2))  # pos -1
    screen.blit(decor, (630 - title.get_width() // 2, 316 - title.get_height() // 2))  # pos -2
    screen.blit(decor, (600 - title.get_width() // 2, 326 - title.get_height() // 2))  # pos -3
    screen.blit(decor, (575 - title.get_width() // 2, 342 - title.get_height() // 2))  # pos -4
    screen.blit(decor, (560 - title.get_width() // 2, 364 - title.get_height() // 2))  # middle left
    screen.blit(decor, (660 - title.get_width() // 2, 416 - title.get_height() // 2))  # pos 1
    screen.blit(decor, (630 - title.get_width() // 2, 412 - title.get_height() // 2))  # pos 2
    screen.blit(decor, (600 - title.get_width() // 2, 404 - title.get_height() // 2))  # pos 3
    screen.blit(decor, (575 - title.get_width() // 2, 389 - title.get_height() // 2))  # pos 4

def get_img_string_from_card(card):
    """ takes a card object and returns a string to match the library of card images """
    rank = card.get_rank()
    suit = card.get_suit()
    return "card_images/" + str(rank) + "_of_" + suit + ".png"

class button:
    """ button class for our numerous and voluminous buttons """
    def __init__(self, color, x, y, width, height, text):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            font = pygame.font.SysFont(None, 45)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, ((self.x + (self.width/2 - text.get_width()/2)), (self.y + (self.height / 2) - text.get_height()/2)))

    def is_over(self, pos):
        # pos is an x y pair
        if (pos[0] > self.x) and (pos[0] < self.x + self.width):
            if (pos[1] > self.y) and (pos[1] < self.y + self.height):
                return True

        return False


# open a window
size = (WIDTH, HEIGHT)  # dimensions for playable window
screen = pygame.display.set_mode(size)  # size is the parameter for the size of the screen
pygame.display.set_caption("Cards")
ellipse_rect = pygame.Rect(470, 292, 255,
                           110)  # rect object, it goes by (start point width, start point height, width,  and height
# sets up fonts
############################################
# ring around casino "*" font
font_title = pygame.font.SysFont(None, 72)
font_money = pygame.font.SysFont(None, 48)
title = font_title.render("CASINO", False, BG_TEXT)
font_decor = pygame.font.SysFont(None, 45)
decor = font_decor.render("*", False, BG_TEXT)  # for the ring around casino
############################################
# now to set up game
carry_on = True  # this is how we will run the while loop to see if we should keep updating game logic
clock = pygame.time.Clock()  # how we will control when the game updates
game_deck = Deck.Deck()
house = Player.Player(1000)
player = Player.Player(100)
river = Player.Player(0)     # this will be the river for texas holdem' (and hold our bets)
player_bet = Player.Player(0)

# rects for recurring objects
deck_rect = (50, 290)
player_cash_rect = (1030, 600)
player_cash_text_rect = (1000, 650)
house_cash_rect = (1030, 100)
house_cash_text_rect = (974, 50)
game_state_rect = (25, 50)
game_state_update_rect = (25, 100)
pot_rect = (25, 600)
pot_money_rect = (35, 650)
your_bet_rect = (1000, 515)
# the empty lists to store the img string
player_hand = []
house_hand = []
river_hand = []
# int variable to keep track of game state
game_state = 1
ante = 5
# buttons
ante_button = button(YCP_GREEN, 850, 500, 150, 60, "ante up")
bet1_button = button(YCP_GREEN, 640, 500, 100, 60, "$1")
bet5_button = button(YCP_GREEN, 745, 500, 100, 60, "$5")
bet10_button = button(YCP_GREEN, 850, 500, 100, 60, "$10")
all_in_button = button(YCP_GREEN, 745, 600, 200, 60, "all in baby")
check_button = button(YCP_GREEN, 640, 600, 100, 60, "check")
cancel_bet = button(YCP_GREEN, 1000, 300, 175, 60, "cancel bet")
send_it_button = button(YCP_GREEN, 1000, 400, 175, 60, "send it!")
fold_button = button(YCP_GREEN, 40, 450, 100, 60, "fold")
# *** *** *** *** MAIN *** *** *** *** #
while carry_on:
    # this is where game logic will go
    """
    bg color
    """
    screen.fill(DARK_GREEN)
    """
    draw betting buttons
    """
    if game_state == 2: # ante
        ante_button.draw(screen, BLACK)
        fold_button.draw(screen, BLACK)

    if game_state > 3: # time to bet
        bet1_button.draw(screen, BLACK)
        bet5_button.draw(screen, BLACK)
        bet10_button.draw(screen, BLACK)
        all_in_button.draw(screen, BLACK)
        cancel_bet.draw(screen, BLACK)
        send_it_button.draw(screen, BLACK)
        fold_button.draw(screen, BLACK)
        check_button.draw(screen, BLACK)

        your_bet = font_money.render("Bet:", False, BLACK)
        screen.blit(your_bet, your_bet_rect)
        bet_num = font_money.render("$" + str(player_bet.get_money()), False, BLACK)
        screen.blit(bet_num, ((your_bet_rect[0] + 70), (your_bet_rect[1])))

    # draw title, stars
    screen.blit(title, ((WIDTH / 2) - title.get_width() // 2,(HEIGHT / 2)  - title.get_height() // 2))
    draw_star(decor, screen, title)

    # draw player mula
    player_cash = font_money.render("$" + str(player.get_money()), False, BLACK)
    player_cash_text = font_money.render("Your Mula", False, BLACK)
    screen.blit(player_cash, player_cash_rect)
    screen.blit(player_cash_text, player_cash_text_rect)

    # draw house mula
    house_cash = font_money.render("$" + str(house.get_money()), False, BLACK)
    house_cash_text = font_money.render("House Mula", False, BLACK)
    screen.blit(house_cash, house_cash_rect)
    screen.blit(house_cash_text, house_cash_text_rect)

    # draw current game state (ante, etc.)
    game_state_text = font_money.render("Current State:", False, BLACK)
    screen.blit(game_state_text, game_state_rect)

    # draw the pot
    pot = font_money.render("Pot:", False, BLACK)
    pot_money = font_money.render("$" + str(river.get_money()), False, BLACK)
    screen.blit(pot, pot_rect)
    screen.blit(pot_money, pot_money_rect)

    """
    game state check for changing text
    """
    # ante state
    if game_state == 2:
        game_state_update_text = font_money.render("*ante*", False, BLACK)
        screen.blit(game_state_update_text, game_state_update_rect)

    # deal state 1
    if game_state == 3:
        game_state_update_text = font_money.render("*river deal*", False, BLACK)
        screen.blit(game_state_update_text, game_state_update_rect)
        # deal 3 cards to river
        print("test")
        for i in range(0, 3):
            print(len(river_hand))
            print(len(river.get_hand()))
            river_card = game_deck.deal_card()
            river.add_card_to_hand(river_card)
            river_img = get_img_string_from_card(river_card)
            river_hand.append(river_img)
        game_state = 4

    # first round of betting state
    if game_state == 4:
        game_state_update_text = font_money.render("*1st round of betting*", False, BLACK)
        screen.blit(game_state_update_text, game_state_update_rect)

    # second deal state
    if game_state == 5:
        river_card = game_deck.deal_card()
        river.add_card_to_hand(river_card)
        river_img = get_img_string_from_card(river_card)
        river_hand.append(river_img)
        game_state = 6

    # second betting state
    if game_state == 6:
        game_state_update_text = font_money.render("*2nd round of betting*", False, BLACK)
        screen.blit(game_state_update_text, game_state_update_rect)

    # third deal state
    if game_state == 7:
        river_card = game_deck.deal_card()
        river.add_card_to_hand(river_card)
        river_img = get_img_string_from_card(river_card)
        river_hand.append(river_img)
        print(game_deck.get_len())
        game_state = 8

    # third betting state
    if game_state == 8:
        game_state_update_text = font_money.render("*3rd round of betting*", False, BLACK)
        screen.blit(game_state_update_text, game_state_update_rect)

    # reveal state
    if game_state == 9:
        game_state_update_text = font_money.render("*reveal!*", False, BLACK)
        # draw our hands
        screen.blit(game_state_update_text, game_state_update_rect)
        screen.blit(pygame.image.load(house_hand[0]).convert(), (510, 70))
        screen.blit(pygame.image.load(house_hand[1]).convert(), (610, 70))
        screen.blit(pygame.image.load(player_hand[0]).convert(), (310, 520))
        screen.blit(pygame.image.load(player_hand[1]).convert(), (410, 520))
        for i in range(0, len(river_hand)):
            screen.blit(pygame.image.load(river_hand[i]).convert(), (350 + (i * 100), 300))
        print("reveal state")
        pygame.display.flip()
        pygame.time.wait(5000)
        print("after wait")

        # now we score the decks
        for i in range(0, 3):
            player.add_card_to_hand(river.get_hand()[i])
            house.add_card_to_hand(river.get_hand()[i])

        p_score = HandScore.get_score(player.get_hand())
        h_score = HandScore.get_score(house.get_hand())
        print(p_score)
        print(h_score)
        if p_score > h_score:
            game_state_update_text = font_money.render("you win >:(", False, BLACK)
            screen.blit(game_state_update_text, game_state_update_rect)
            winnings = river.get_money()
            river.bet(river.get_money())
            player.add_money(winnings)
            pygame.display.flip()
            pygame.time.wait(5000)
            player.clear_hand()
            player_hand = []
            house.clear_hand()
            house_hand = []
            river.clear_hand()
            river_hand = []
            game_state = 1
        else:
            game_state_update_text = font_money.render("House Always Wins!", False, BLACK)
            screen.blit(game_state_update_text, game_state_update_rect)
            winnings = river.get_money()
            river.bet(river.get_money())
            house.add_money(winnings)
            player.clear_hand()
            player_hand = []
            house.clear_hand()
            house_hand = []
            river.clear_hand()
            river_hand = []
            pygame.display.flip()
            pygame.time.wait(5000)
            game_state = 1


    """
    draw the game deck
    """
    deck_img = pygame.image.load('card_images/back-sm.png').convert()
    screen.blit(deck_img, deck_rect)
    """
    shuffle the deck
    """
    deck_shuffled = random.sample(game_deck.get_deck(), len(game_deck.get_deck()))
    game_deck.set_new_deck(deck_shuffled)

    # first game state
    if game_state == 1:
        # now we have to deal from the deck into each player's hands (house, player)
        print(game_deck.get_len())
        for i in range(0, 2):
            card_deck = game_deck.deal_card()
            house.add_card_to_hand(card_deck)
            house_img = get_img_string_from_card(card_deck)
            # animation for dealing a card will eventually be here
            house_hand.append(house_img)

        for i in range(0, 2):
            card_player = game_deck.deal_card()
            player.add_card_to_hand(card_player)
            player_img = get_img_string_from_card(card_player)
            player_hand.append(player_img)

        print(game_deck.get_len())
        print("***")
        for i in range(0, len(player.get_hand())):
            print(player.get_hand()[i].get_rank())
        print("***")
        for i in range(0, len(house.get_hand())):
            print(house.get_hand()[i].get_rank())

        game_state = 2  # game switches states

    # drawing our hands
    if game_state > 3:
        screen.blit(pygame.image.load(player_hand[0]).convert(), (310, 520))
        screen.blit(pygame.image.load(player_hand[1]).convert(), (410, 520))
    else:
        screen.blit(pygame.image.load(player_hand[0]).convert(), (510, 520))
        screen.blit(pygame.image.load(player_hand[1]).convert(), (610, 520))

    if game_state < 9:
        screen.blit(deck_img, (510, 70))
        screen.blit(deck_img, (610, 70))

    if game_state > 2:
        for i in range(0, len(river_hand)):
            screen.blit(pygame.image.load(river_hand[i]).convert(), (350 + (i * 100), 300))

    # main event loop
    for event in pygame.event.get():  # user did something
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            carry_on = False

        if event.type == pygame.MOUSEMOTION:
            if game_state == 2:
                if ante_button.is_over(pos):
                    ante_button.color = DARK_GREEN
                elif fold_button.is_over(pos):
                    fold_button.color = DARK_GREEN
                else:
                    ante_button.color = YCP_GREEN
                    fold_button.color = YCP_GREEN

            if game_state > 3:
                if bet1_button.is_over(pos):
                    bet1_button.color = DARK_GREEN

                elif bet5_button.is_over(pos):
                    bet5_button.color = DARK_GREEN

                elif bet10_button.is_over(pos):
                    bet10_button.color = DARK_GREEN

                elif all_in_button.is_over(pos):
                    all_in_button.color = DARK_GREEN

                elif cancel_bet.is_over(pos):
                    cancel_bet.color = DARK_GREEN

                elif send_it_button.is_over(pos):
                    send_it_button.color = DARK_GREEN

                elif fold_button.is_over(pos):
                    fold_button.color = DARK_GREEN

                elif check_button.is_over(pos):
                    check_button.color = DARK_GREEN

                else:
                    bet1_button.color = YCP_GREEN
                    bet5_button.color = YCP_GREEN
                    bet10_button.color = YCP_GREEN
                    all_in_button.color = YCP_GREEN
                    cancel_bet.color = YCP_GREEN
                    send_it_button.color = YCP_GREEN
                    fold_button.color = YCP_GREEN
                    check_button.color = YCP_GREEN

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == 2:
                if ante_button.is_over(pos):
                    river.add_money(ante*2)
                    player.bet(ante)
                    house.bet(ante)
                    game_state = 3
                if fold_button.is_over(pos):
                    print(game_deck.get_len())
                    game_deck.rebuild(player.get_hand())
                    print(game_deck.get_len())
                    game_deck.rebuild(house.get_hand())
                    print("CHECK HERE" + str(game_deck.get_len()))
                    player.clear_hand()
                    player_hand = []
                    house.clear_hand()
                    house_hand = []
                    river.clear_hand()
                    river_hand = []
                    player_hand = []
                    game_state = 1

            if game_state > 3:
                if bet1_button.is_over(pos):
                    player.bet(1)
                    player_bet.add_money(1)

                if bet5_button.is_over(pos):
                    player.bet(5)
                    player_bet.add_money(5)

                if bet10_button.is_over(pos):
                    player.bet(10)
                    player_bet.add_money(10)

                if all_in_button.is_over(pos):
                    total = player.get_money()
                    player.bet(total)
                    player_bet.add_money(total)

                if cancel_bet.is_over(pos):
                    refund = player_bet.get_money()
                    player_bet.bet(refund)
                    player.add_money(refund)

                if send_it_button.is_over(pos):
                    bet = player_bet.get_money()
                    player_bet.bet(bet)
                    house.bet(bet)
                    river.add_money(bet*2)
                    game_state += 1

                if fold_button.is_over(pos):
                    game_deck.rebuild(player.get_hand())
                    game_deck.rebuild(house.get_hand())
                    game_deck.rebuild(river.get_hand())
                    player.clear_hand()
                    house.clear_hand()
                    river.clear_hand()
                    player_hand = []
                    river_hand = []
                    house_hand = []
                    game_state = 1




    # now need to update the screen
    pygame.display.flip()
    clock.tick(60)

# once we exit the main loop we can exit the engine
pygame.quit()
