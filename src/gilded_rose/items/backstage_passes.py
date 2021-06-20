from gilded_rose.items.item import Item


class BackstagePasses(Item, name="Backstage passes to a TAFKAL80ETC concert"):
    def __init__(self, sell_in: int, quality: int, name: str = "Backstage passes to a TAFKAL80ETC concert"):
        super().__init__(name, sell_in, quality)

    def _change_quality(self):
        if self._is_expired():
            self.quality = 0
        else:
            self.quality += self._quality_add_amount()

    def _is_expired(self) -> bool:
        return self.sell_in < 0

    def _quality_add_amount(self) -> int:
        if self.sell_in < 5:
            return 3
        if self.sell_in < 10:
            return 2
        return 1
