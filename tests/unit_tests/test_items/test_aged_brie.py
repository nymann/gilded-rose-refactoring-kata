from gilded_rose.items.aged_brie import AgedBrie


def test_aged_brie_normal():
    aged_brie = AgedBrie(name="", sell_in=10, quality=9)
    aged_brie.update_quality()
    assert aged_brie.quality == 10

def test_aged_brie_double():
    aged_brie = AgedBrie(name="", sell_in=0, quality=9)
    aged_brie.update_quality()
    assert aged_brie.quality == 11
