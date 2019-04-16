import Card as c

# setup
ace_of_hearts = c.Card(1, "heart")
eight_of_diamonds = c.Card(8, "diamond")

def test_get_rank():
    assert 1 == ace_of_hearts.get_rank()
    assert 8 == eight_of_diamonds.get_rank()

def test_get_suit():
    assert "heart" == ace_of_hearts.get_suit()
    assert "diamond" == eight_of_diamonds.get_suit()
