from gilded_rose.items.item import Item


class IncreasingQualityItem(Item):
    def update_quality(self):
        self.sell_in -= 1
        self.quality += 1
