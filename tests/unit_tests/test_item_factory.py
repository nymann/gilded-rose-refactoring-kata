import pytest

from gilded_rose.items.aged_brie import AgedBrie
from gilded_rose.items.backstage_passes import BackstagePasses
from gilded_rose.items.conjured import ConjuredItem
from gilded_rose.items.item import Item
from gilded_rose.items.sulfuras import Sulfuras

COMMON_VARS = {"sell_in": 10, "quality": 10}

test_cases = [
        (Item(name="Sulfuras, Hand of Ragnaros", **COMMON_VARS), Sulfuras),
        (Item(name="Aged Brie", **COMMON_VARS), AgedBrie),
        (Item(name="Conjured", **COMMON_VARS), ConjuredItem),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", **COMMON_VARS), BackstagePasses),
]

@pytest.mark.parametrize("item,expected_item_type", test_cases)
def test_item_factory(item: Item, expected_item_type):
    item_type: Item = Item.create_from_item(item=item)
    assert isinstance(item_type, expected_item_type)
