from gilded_rose.gilded_rose import GildedRose, Item

def test_backstage_passes_concert():
    tafkal = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=30, quality=5)
    gilded_rose = GildedRose(items=[tafkal])
    for _ in range(100):
        expected_quality = tafkal.quality
        if tafkal.sell_in <= 0:
            expected_quality = 0
        elif tafkal.sell_in <= 5:
            expected_quality += 3
        elif tafkal.sell_in <= 10:
            expected_quality += 2
        else:
            expected_quality += 1
        if expected_quality > 50:
            expected_quality = 50
        expected_sell_in = tafkal.sell_in - 1
        print(tafkal.sell_in)
        gilded_rose.update_quality()
        assert tafkal.quality == expected_quality
        assert tafkal.sell_in == expected_sell_in
