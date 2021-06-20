from gilded_rose.items.item import Item


class AgedBrie(Item, name="Aged Brie"):
    def __init__(self, sell_in: int, quality: int, name: str = "Aged Brie"):
        super().__init__(name, sell_in, quality)

    def _change_quality(self):
        if self.sell_in < 0:
            self.quality += 2
        else:
            self.quality += 1
