from gilded_rose.items.item import Item


class GildedRose:

    def __init__(self, items: list[Item]):
        self.items: list[Item] = [Item.create_from_item(item=item) for item in items]

    def update_quality(self):
        for item in self.items:
            item.update_quality()
