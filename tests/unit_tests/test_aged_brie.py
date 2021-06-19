from gilded_rose.gilded_rose import GildedRose
from gilded_rose.items.item import Item

def test_aged_brie():
    gilded_rose = GildedRose(items=[Item(name="Aged Brie", sell_in=20, quality=5)])
    for _ in range(100):
        aged_brie = gilded_rose.items[0]
        expected_quality = aged_brie.quality + 1
        if aged_brie.sell_in <= 0:
            expected_quality += 1
        if expected_quality > 50:
            expected_quality = 50
        expected_sell_in = aged_brie.sell_in - 1
        gilded_rose.update_quality()
        assert aged_brie.quality == expected_quality
        assert aged_brie.sell_in == expected_sell_in
