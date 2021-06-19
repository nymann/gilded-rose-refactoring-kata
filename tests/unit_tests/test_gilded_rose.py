from gilded_rose.gilded_rose import GildedRose
from gilded_rose.items.aged_brie import AgedBrie
from gilded_rose.items.conjured import ConjuredItem
from gilded_rose.items.item import Item

COMMON_VARS = {"sell_in": 10, "quality": 5}
items = [
        Item(name="Sulfuras, Hand of Ragnaros", **COMMON_VARS),
        AgedBrie(name="Aged Brie", **COMMON_VARS),
        ConjuredItem(name="Conjured", **COMMON_VARS),
        ConjuredItem(name="Backstage passes to a TAFKAL80ETC concert", **COMMON_VARS)
]

def test_init():
    """Test if no errors are thrown.

    Since we are testing all the items by themselves we don't really need to do anything.
    """
    gilded_rose = GildedRose(items=items)
    gilded_rose.update_quality()
