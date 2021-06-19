from gilded_rose.items.conjured import ConjuredItem

QUALITY = 5

def test_conjured_past_expire():
    """When past the expiration sell date, quality should decrement by 4."""
    conjured_item = ConjuredItem(name="", sell_in=0, quality=QUALITY)
    conjured_item.update_quality()
    assert conjured_item.quality == QUALITY - 4

def test_conjured_pre_expire():
    """When not past the expiration sell date, quality should decrement by 2."""
    conjured_item = ConjuredItem(name="", sell_in=1, quality=QUALITY)
    conjured_item.update_quality()
    assert conjured_item.quality == QUALITY - 2
