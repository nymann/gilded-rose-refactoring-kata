from gilded_rose.items.item import Item


class ConjuredItem(Item):
    def _change_quality(self):
        if self.sell_in < 0:
            self.quality -= 4
        else:
            self.quality -= 2
