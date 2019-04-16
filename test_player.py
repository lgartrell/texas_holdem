import Player
import Deck

#  setup
game_deck = Deck.Deck()  # we are not gonna shuffle the deck so we know what the cards that will be dealed are
player = Player.Player(100)  # we are passing in 100 as the starting money


def test_player_accept_deal():
    for i in range(0, 2):
        player.set_hand(game_deck.deal_card())

    assert len(player.get_hand()) == 2
    # now we will deal 3 more, the hand should grow to 5
    for x in range(0 , 3):
        player.set_hand(game_deck.deal_card())

    assert len(player.get_hand()) == 5

def test_get_money():
    assert 100 == player.get_money()

def test_bet():
    player.bet(25.0)
    assert 75.0 == player.get_money()
