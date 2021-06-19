import pytest

from gilded_rose.items.backstage_passes import BackstagePasses
from gilded_rose.items.conjured import ConjuredItem
from gilded_rose.items.item import Item
from gilded_rose.items.aged_brie import AgedBrie

common_vars = {"name": "SomeName", "sell_in": 30, "quality": 60}
expected_quality = 50

test_cases = [
    (AgedBrie(**common_vars), expected_quality),
    (BackstagePasses(**common_vars), expected_quality),
    (ConjuredItem(**common_vars), expected_quality),
]

@pytest.mark.parametrize("item,expected_quality", test_cases)
def test_quality_cap(item: Item, expected_quality: int):
    item.update_quality()
    assert item.quality == expected_quality
