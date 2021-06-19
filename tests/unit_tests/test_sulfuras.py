from gilded_rose.gilded_rose import GildedRose
from gilded_rose.items.item import Item


def test_sulfuras():
    
    gilded_rose = GildedRose(items=[Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)])
    gilded_rose.update_quality()
    sulfuras = gilded_rose.items[0]
    assert sulfuras.quality == 80
    assert sulfuras.sell_in == 10

def test_sulfuras_negative():
    gilded_rose = GildedRose(items=[Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)])
    gilded_rose.update_quality()
    sulfuras = gilded_rose.items[0]
    assert sulfuras.quality == 80
    assert sulfuras.sell_in == -1
