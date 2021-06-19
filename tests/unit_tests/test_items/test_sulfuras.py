from gilded_rose.items.sulfuras import Sulfuras

def test_sulfuras():
    sulfuras = Sulfuras(name="", sell_in=9, quality=80)
    sulfuras.update_quality()
    assert sulfuras.quality == 80
    assert sulfuras.sell_in == 9
