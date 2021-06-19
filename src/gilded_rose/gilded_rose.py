from gilded_rose.item_factory import ItemFactory
from gilded_rose.items.item import Item


class GildedRose:

    def __init__(self, items):
        self.items: list[Item] = []
        for item in items:
            self.items.append(ItemFactory.create_item(item=item))

    def update_quality(self):
        for item in self.items:
            item.update_quality()
