import pytest

from gilded_rose.items.backstage_passes import BackstagePasses
from gilded_rose.items.conjured import ConjuredItem
from gilded_rose.items.item import Item
from gilded_rose.items.aged_brie import AgedBrie

COMMON_VARS = {"name": "SomeName", "sell_in": 30, "quality": 60}
EXPECTED_QUALITY = 50

test_cases = [
    AgedBrie(**COMMON_VARS),
    BackstagePasses(**COMMON_VARS),
    ConjuredItem(**COMMON_VARS),
]

@pytest.mark.parametrize("item", test_cases)
def test_quality_cap(item: Item):
    item.update_quality()
    assert item.quality == EXPECTED_QUALITY

@pytest.mark.parametrize("item", test_cases)
def test_sell_in_decrement(item: Item):
    expected_sell_in: int = item.sell_in - 1
    item.update_quality()
    assert item.sell_in == expected_sell_in
