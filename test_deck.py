import random
import Deck
import Card as c
import copy #  big time needed

##############################################
# setup
###############################################


# main deck object
deck = Deck.Deck()
deck1 = copy.deepcopy(deck)

# now to make a bunch of cards to test deck order

two_of_hearts = c.Card(2, "hearts")
ace_of_spades = c.Card(1, "spades")
king_of_clover = c.Card(13, "clovers")
king_of_spade = c.Card(13, "spades")
eight_of_diamonds = c.Card(8, "diamonds")
ace_of_hearts = c.Card(1, "hearts")


##############################################
# tests
##############################################
def test_deck_setup():
    x = deck.get_len()
    assert x == 52
    y = deck1.get_len()
    assert y == 52

def test_deck_order():
    # will be reusing x throughout this test
    x = deck.get_card(0) # this card is the ace of hearts
    assert x.get_rank() == ace_of_hearts.get_rank()
    assert deck.get_card(5).get_rank() == two_of_hearts.get_rank() # the card it is pulling is the two of hearts
    assert deck.get_card(51).get_rank() == king_of_clover.get_rank()

def test_deal_card():
    top_card = deck.deal_card()
    next_top_card = deck.deal_card()
    assert top_card.get_rank() == king_of_clover.get_rank() and top_card.get_suit() == king_of_clover.get_suit()
    assert next_top_card.get_rank() == king_of_spade.get_rank() and next_top_card.get_suit() == king_of_spade.get_suit()

def test_add_old_cards():
    hand = []
    before = deck.get_len()
    assert before == 50  # because we dealt 2 cards in the above test
    for i in range(0, 5):
        hand.append(deck.deal_card())
        print(len(hand))

    after = deck.get_len()
    assert after == 45

def test_deck_shuffle():
    # need to get a temp list to test against
    temp_deck = Deck.Deck()
    # now shuffling
    deck_shuffled = random.sample(deck.get_deck(), len(deck.get_deck())) # how to shuffle ****
    # now setting the shuffled deck as our main deck
    deck.set_new_deck(deck_shuffled)
    # tests
    assert deck.get_card(0) != temp_deck.get_card(0)
    assert deck.get_card(32) != temp_deck.get_card(32)
    assert deck.get_card(51) != temp_deck.get_card(51)
    assert deck.get_card(38) != temp_deck.get_card(38)