from gilded_rose.item_factory import ItemFactory
from gilded_rose.items.item import Item


class GildedRose:

    def __init__(self, items: list[Item]):
        self.items: list[Item] = [ItemFactory.create_item(item=item) for item in items]

    def update_quality(self):
        for item in self.items:
            item.update_quality()
