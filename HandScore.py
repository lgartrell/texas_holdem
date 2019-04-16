"""
Scoring method. Pairs get calculated first, and then everything is scored in order of what beats what
if nothing hits, high card is calculated
"""

def get_score(first, *hand):
    score = 0
    calc_high_card = True  # we will update this to false if any other hand is scored
    cards = []
    cards.append(first)
    cards.extend(hand)
    # first we sort

    """
    this is our key function for our sorted function
    """

    def to_sort(single_card):
        return single_card.get_rank()

    cards = sorted(*cards, key=to_sort)
    print("cards after being sorted: ")
    for x in range(0, len(cards)):
        print(cards[x].get_rank())
    print('end of sort print')
    print('*****************')
    # the pair calculation (+10*rank for double pair, +100*rank for triple, 1000*rank for 4 pair)
    full_house = 0  # will equal 2 if a full house is present
    count = 0  # init value for count variable
    skip = 0
    for x in range(0, len(cards)):
        card = cards[x]
        if skip % 2 == 0:
            for y in range(0, len(cards)):
                print("cards being compared: ")
                print(card.get_rank(), ',', cards[y].get_rank())
                if card.get_rank() == cards[y].get_rank():
                    count += 1

            print(count)
            # normal pair (works the same way with 2 pair, score gets incremented with each pair
            if count == 2:
                skip += 1
                calc_high_card = False
                for i in range(1, 14):
                    if cards[x].get_rank() == i:
                        if i == 1:  # for a pair of  aces, we want it to beat a pair of kings
                            print("pair")
                            score += 140
                            full_house += 1
                        else:
                            print("pair")
                            score += i * 10
                            full_house += 1
            # 3 pair
            if count == 3:
                calc_high_card = False
                skip += 1
                for i in range(1, 14):
                    if cards[x].get_rank() == i:
                        if i == 1:  # ace calculation
                            print("3 pair")
                            score += 1800
                            full_house += 3
                        else:
                            print("3 pair")
                            score += i * 136  # this is a weird number to beat the best possible 2 pair
                            full_house += 3
            # 4 of a kind
            if count == 4:
                calc_high_card = False
                for i in range(1, 14):
                    if cards[x].get_rank() == i:
                        if i == 1:  # ace calculation
                            score += 14000000
                            print("4 of a kind")
                            return score
                        else:
                            score += i * 10000000
                            print("4 of a kind")
                            return score
            count = 0  # we want to reset count each time through
            print('made it down here')
        else:
            skip += 1

    if full_house == 7:  # this means a full house is present, now we need to score it
        score += 100000
        print("full house")
        return score
    if score != 0:
        return score
    # now to calculate royal flush
    b_check_rank = False
    true_if_len_of_hand = 0
    o_suit_of_first_card = cards[0].get_suit()
    for penis in range(0, len(cards)):
        if o_suit_of_first_card == cards[penis].get_suit():
            true_if_len_of_hand += 1

    if true_if_len_of_hand == len(cards):
        b_check_rank = True

    # now we know they are all the same suit, so we check the order of the ranks
    if b_check_rank and (cards[0].get_rank() == 1 and cards[1].get_rank() == 10
                         and cards[2].get_rank() == 11 and cards[3].get_rank() == 12
                         and cards[4].get_rank() == 13):
        score += 10000000000
        print("royale flush")
        return score

    # now we need to check for straight flush
    # reusing code for flush
    b_check_rank = False
    true_if_len_of_hand = 0
    o_suit_of_first_card = cards[0].get_suit()
    for penis in range(0, len(cards)):
        if o_suit_of_first_card == cards[penis].get_suit():
            true_if_len_of_hand += 1

    if true_if_len_of_hand == len(cards):
        b_check_rank = True
    # end of flush code
    # now need to see if cards are in order (already sorted above)
    len_if_sorted = 0
    if b_check_rank:
        for i in range(0, len(cards)):
            if (cards[i] == cards[len(cards) - 1]) and (cards[i].get_rank() - 1 == cards[i - 1].get_rank()):
                len_if_sorted += 1
            elif cards[i].get_rank() + 1 == cards[i + 1].get_rank():
                len_if_sorted += 1
    if len_if_sorted == len(cards):
        score += 100000000  # one less zero than the royal flush
        print("straight flush")
        return score

    # now need to check for a flush
    # same code as above, but this time if it is a flush we will return the score
    true_if_len_of_hand = 0
    o_suit_of_first_card = cards[0].get_suit()
    for penis in range(0, len(cards)):
        if o_suit_of_first_card == cards[penis].get_suit():
            true_if_len_of_hand += 1

    if true_if_len_of_hand == len(cards):
        print('flush')
        score += 10000
        return score

    # now need to check for a straight
    # reusing straight code, just returning the score this time
    len_if_sorted_round_two = 0
    for i in range(0, len(cards)):
        if (cards[i] == cards[len(cards) - 1]) and (cards[i].get_rank() - 1 == cards[i - 1].get_rank()):
            len_if_sorted_round_two += 1
        elif cards[i].get_rank() + 1 == cards[i + 1].get_rank():
            len_if_sorted_round_two += 1
    if len_if_sorted_round_two == len(cards):
        print('straight as a rainbow')
        score += 9000  # one thousand less than a flush
        return score

    # we will only reach here if none of the other code above executed.
    # the score could only of been incremented by the pair, and that it the only part of the scoring that doesnt
    # return if it is incremented. So we need to check if we are looking for the high card
    if calc_high_card:
        print('high card')
        # cards are already sorted, so we can just return the last card
        score += cards[len(cards) - 1].get_rank()
        return score
    else:  # else we return the score we calc above in the pair section
        return score
