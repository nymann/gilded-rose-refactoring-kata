from gilded_rose.items.item import Item


class Sulfuras(Item, name="Sulfuras, Hand of Ragnaros"):
    def __init__(self, sell_in: int, quality: int, name: str = "Sulfuras, Hand of Ragnaros"):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        pass
