from gilded_rose.items.increating_quality_item import IncreasingQualityItem


class BackstagePasses(IncreasingQualityItem):
    def update_quality(self):
        super().update_quality()

        if self.sell_in < 10:
            self.quality += 1
        if self.sell_in < 5:
            self.quality += 1
        if self.sell_in < 0:
            self.quality = 0
        self._cap_quality()
