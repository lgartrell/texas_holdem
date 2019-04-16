import Card as c


class Deck:
    __game_deck = []

    def __init__(self):
        for rank in range(1, 14):
            for suit in range(0, 4):
                if suit == 0:
                    self.__game_deck.append(c.Card(rank, "hearts"))
                elif suit == 1:
                    self.__game_deck.append(c.Card(rank, "diamonds"))
                elif suit == 2:
                    self.__game_deck.append(c.Card(rank, "spades"))
                else:  # suit must then be 3 (slightly faster i think)
                    self.__game_deck.append(c.Card(rank, "clovers"))

    """
    returns the length of the deck -- used to check if the constructor is working
    """

    def get_len(self):
        return len(self.__game_deck)

    """
    returns the card at the index passed through num -- the card can then be used with get_rank and get_suit
    methods
    """

    def get_card(self, num):
        return self.__game_deck[num]

    """
    sets the old deck to the new shuffled one
    """

    def set_new_deck(self, shuffled):
        self.__game_deck = shuffled
        return

    """
    returns the deck
    """

    def get_deck(self):
        return self.__game_deck

    """
    removes the top card from the deck and returns it
    """
    def deal_card(self):
        return self.__game_deck.pop()  # need to subtract 1 so we don't go out of bounds

    """
    adds the list of old_cards to the top of the deck, then the deck should be shuffled
    """
    def rebuild(self, old_cards):
        self.__game_deck.extend(old_cards)
        return

