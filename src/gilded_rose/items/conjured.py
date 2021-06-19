from gilded_rose.items.item import Item


class ConjuredItem(Item):
    def update_quality(self):
        self.quality -= 2
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality -= 2
        self._cap_quality()
