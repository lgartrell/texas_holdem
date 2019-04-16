
class Card:
    __rank = 0
    __suit = None

    """
    the constructor for card, sets the rank and color value passed through
    """

    def __init__(self,  r, s):
        self.__rank = r
        self.__suit = s

    """
    returns the rank of the card
    """

    def get_rank(self) -> int:
        return self.__rank

    """
    returns the suit of the card
    """
    def get_suit(self) -> str:
        return self.__suit
