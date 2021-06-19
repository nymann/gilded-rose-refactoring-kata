from gilded_rose.items.increating_quality_item import IncreasingQualityItem


class AgedBrie(IncreasingQualityItem):
    def update_quality(self):
        super().update_quality()

        if self.sell_in < 0:
            self.quality += 1
        if self.quality > 50:
            self.quality = 50
