from gilded_rose.items.item import Item


class ConjuredItem(Item, name="Conjured"):
    def __init__(self, sell_in: int, quality: int, name: str = "Conjured"):
        super().__init__(name, sell_in, quality)

    def _change_quality(self):
        if self.sell_in < 0:
            self.quality -= 4
        else:
            self.quality -= 2
