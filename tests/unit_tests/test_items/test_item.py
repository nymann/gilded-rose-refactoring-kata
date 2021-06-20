import pytest

from gilded_rose.items.item import Item


def test_raises_not_implemented():
    item = Item(name="Non existing item", sell_in=2, quality=3)
    with pytest.raises(NotImplementedError):
        item.update_quality()
