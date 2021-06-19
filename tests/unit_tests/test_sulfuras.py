from gilded_rose.gilded_rose import GildedRose, Item

def test_sulfuras_quality():
    starting_quality = 80
    sulfuras = Item(name="Sulfuras, Hand of Ragnaros", sell_in=30, quality=starting_quality)
    gilded_rose = GildedRose(items=[sulfuras])
    assert sulfuras.quality == starting_quality
    gilded_rose.update_quality()
    assert sulfuras.quality == starting_quality
