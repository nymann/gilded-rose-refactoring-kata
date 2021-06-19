import pytest
from gilded_rose.items.item import Item


def test_raises_not_implemented():
    item = Item(name="", sell_in=0, quality=3)
    with pytest.raises(NotImplementedError):
        item.update_quality()
