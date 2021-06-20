from gilded_rose.gilded_rose import GildedRose
from gilded_rose.items.aged_brie import AgedBrie
from gilded_rose.items.item import Item

items = [Item(name="Aged Brie", sell_in=2, quality=4)]

def test_init():
    """Test if all items are converted.

    We test that that the converted type is correct in test_item_factory so we don't do it here.
    """

    gilded_rose = GildedRose(items=items)
    assert len(gilded_rose.items) == len(items)

def test_update_call():
    """Test that update quality is called on the GildedRose items."""

    gilded_rose = GildedRose(items=items)
    gilded_rose.update_quality()
    aged_brie = gilded_rose.items[0]

    assert isinstance(aged_brie, AgedBrie)
    assert aged_brie.quality == 5
