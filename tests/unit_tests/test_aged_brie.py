from gilded_rose.gilded_rose import GildedRose, Item

def test_aged_brie():
    aged_brie = Item(name="Aged Brie", sell_in=20, quality=5)
    gilded_rose = GildedRose(items=[aged_brie])
    for _ in range(100):
        expected_quality = aged_brie.quality + 1
        if aged_brie.sell_in <= 0:
            expected_quality += 1
        if expected_quality > 50:
            expected_quality = 50
        gilded_rose.update_quality()
        assert aged_brie.quality == expected_quality
