from gilded_rose.gilded_rose import GildedRose, Item

def test_backstage_passes_concert():
    gilded_rose = GildedRose(items=[Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=30, quality=5)])
    for _ in range(100):
        backstage_passes = gilded_rose.items[0]
        expected_quality = backstage_passes.quality
        if backstage_passes.sell_in <= 0:
            expected_quality = 0
        elif backstage_passes.sell_in <= 5:
            expected_quality += 3
        elif backstage_passes.sell_in <= 10:
            expected_quality += 2
        else:
            expected_quality += 1
        if expected_quality > 50:
            expected_quality = 50
        expected_sell_in = backstage_passes.sell_in - 1
        print(backstage_passes.sell_in)
        gilded_rose.update_quality()
        assert backstage_passes.quality == expected_quality
        assert backstage_passes.sell_in == expected_sell_in
