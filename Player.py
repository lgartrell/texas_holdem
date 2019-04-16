

class Player:
    __cards = []
    __money = None

    def __init__(self, start_money):
        self.__money = start_money

    def add_card_to_hand(self, deal):
        self.__cards.append(deal)
        return

    def sort_hand(self):
        self.__cards.sort()
        return

    """
    should return None if bet is greater than money
    """
    def bet(self, num):
        if self.__money < int(num):
            return 0
        else:
            self.__money = self.__money - int(num)
        return

    def add_money(self, num):
        self.__money += num

    def get_money(self):
        return self.__money

    def get_hand(self):
        return self.__cards

    def clear_hand(self):
        self.__cards = []

