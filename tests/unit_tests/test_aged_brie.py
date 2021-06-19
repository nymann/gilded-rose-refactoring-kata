from gilded_rose.gilded_rose import GildedRose, Item

def test_aged_brie():
    aged_brie = Item(name="Aged Brie", sell_in=10, quality=5)
    gilded_rose = GildedRose(items=[aged_brie])
    for _ in range(30):
        if aged_brie.sell_in == 0:
            expected = aged_brie.quality + 2
        else:
            expected = aged_brie.quality + 1
        if expected > 50:
            expected = 50
        gilded_rose.update_quality()
        aged_brie.quality == expected
