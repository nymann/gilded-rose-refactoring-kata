from gilded_rose.items.item import Item


class AgedBrie(Item):
    def update_quality(self):
        self.quality += 1
        self.sell_in -= 1

        if self.sell_in < 0:
            self.quality += 1
        if self.quality > 50:
            self.quality = 50
