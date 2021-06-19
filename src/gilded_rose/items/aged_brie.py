from gilded_rose.items.item import Item


class AgedBrie(Item):
    def _change_quality(self):
        if self.sell_in < 0:
            self.quality += 2
        else:
            self.quality += 1
