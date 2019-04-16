import Card
import HandScore

# setup
########################################################################################################################
# royale flush
hand_royale_hearts = [Card.Card(1, "heart"), Card.Card(10, "heart"), Card.Card(11, "heart"), Card.Card(12, "heart")
                    , Card.Card(13, "heart")]
# straight flush
hand_straight_flush = [Card.Card(2, "clover"), Card.Card(3, "clover"), Card.Card(4, "clover"), Card.Card(5, "clover")
                    , Card.Card(6, "clover")]
# straight
hand_straight = [Card.Card(5, "heart"), Card.Card(6, "heart"), Card.Card(7, "spade"), Card.Card(8, "clover")
                    , Card.Card(9, "diamond")]
# flush
hand_flush = [Card.Card(1, "diamond"), Card.Card(10, "diamond"), Card.Card(7, "diamond"), Card.Card(4, "diamond")
              , Card.Card(9, "diamond")]
# 4 pair
hand_four_pair = [Card.Card(1, "diamond"), Card.Card(1, "heart"), Card.Card(1, "spade"), Card.Card(1, "clover")
              , Card.Card(9, "diamond")]
# full house
hand_full_house = [Card.Card(2, "diamond"), Card.Card(2, "heart"), Card.Card(2, "spade"), Card.Card(3, "diamond")
              , Card.Card(3, "clover")]
# 3 pair
hand_three_pair = [Card.Card(7, "diamond"), Card.Card(7, "heart"), Card.Card(7, "clover"), Card.Card(4, "diamond")
              , Card.Card(9, "diamond")]
# 2 pair (double)
hand_doubs = [Card.Card(2, "diamond"), Card.Card(2, "clover"), Card.Card(5, "hearts"), Card.Card(5, "spades")
              , Card.Card(9, "diamond")]
# 2 pair (single)
hand_single_doub = [Card.Card(1, "heart"), Card.Card(1, "diamond"), Card.Card(7, "diamond"), Card.Card(4, "diamond")
              , Card.Card(9, "diamond")]
# high card 7
hand_seven_high = [Card.Card(7, "diamond"), Card.Card(3, "clover"), Card.Card(5, "heart"), Card.Card(2, "spade")
              , Card.Card(6, "diamond")]

def test_royale():
    assert HandScore.get_score(*hand_royale_hearts) == 10000000000

def test_straight_flush():
    assert len(hand_straight_flush) == 5
    assert HandScore.get_score(*hand_straight_flush) == 100000000

def test_straight():
    assert len(hand_straight) == 5
    assert HandScore.get_score(*hand_straight) == 9000

def test_flush():
    assert len(hand_flush) == 5
    assert HandScore.get_score(*hand_flush) == 10000

def test_double():
    assert HandScore.get_score(*hand_doubs) == 70

def test_four_pair():   # 4 pairs of aces
    assert HandScore.get_score(*hand_four_pair) == 14000000

def test_full_house():  # 3s over 2s (that way a higher full house beats a lower full house
    assert HandScore.get_score(*hand_full_house) == 100574

def test_hand_three_pair():
    assert HandScore.get_score(*hand_three_pair) == 1904

def test_hand_single_dub():
    assert HandScore.get_score(*hand_single_doub) == 140

def test_hand_seven_high():
    assert HandScore.get_score(*hand_seven_high) == 7

def test_compare():
    assert HandScore.get_score(*hand_seven_high) < HandScore.get_score(*hand_full_house)
    assert HandScore.get_score(*hand_straight_flush) < HandScore.get_score(*hand_royale_hearts)
    assert HandScore.get_score(*hand_three_pair) < HandScore.get_score(*hand_four_pair)
    assert HandScore.get_score(*hand_four_pair) > HandScore.get_score(*hand_full_house)
    assert HandScore.get_score(*hand_full_house) > HandScore.get_score(*hand_three_pair)
    assert HandScore.get_score(*hand_doubs) < HandScore.get_score(*hand_three_pair)