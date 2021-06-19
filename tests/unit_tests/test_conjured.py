from gilded_rose.gilded_rose import GildedRose
from gilded_rose.items.conjured import ConjuredItem
from gilded_rose.items.item import Item


def test_conjured():
    gilded_rose = GildedRose(items=[Item(name="Conjured", sell_in=20, quality=5)])
    for _ in range(100):
        conjured = gilded_rose.items[0]
        expected_quality = conjured.quality - 2
        if conjured.sell_in <= 0:
            expected_quality -= 2
        if expected_quality > 50:
            expected_quality = 50
        expected_sell_in = conjured.sell_in - 1
        gilded_rose.update_quality()
        assert conjured.quality == expected_quality
        assert conjured.sell_in == expected_sell_in

def test_conjured_past_expire():
    conjured_item = ConjuredItem(name="", sell_in=0, quality=5)
    conjured_item.update_quality()
    assert conjured_item.quality == 1
