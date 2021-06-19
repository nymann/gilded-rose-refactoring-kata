from gilded_rose.items.aged_brie import AgedBrie
from gilded_rose.items.backstage_passes import BackstagePasses
from gilded_rose.items.item import Item
from gilded_rose.items.sulfuras import Sulfuras

class GildedRose(object):

    def __init__(self, items):
        self.items: list[Item] = []
        for item in items:
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.items.append(BackstagePasses(name=item.name, sell_in=item.sell_in, quality=item.quality))
            elif item.name == "Aged Brie":
                self.items.append(AgedBrie(name=item.name, sell_in=item.sell_in, quality=item.quality))
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.items.append(Sulfuras(name=item.name, sell_in=item.sell_in, quality=item.quality))

    def update_quality(self):
        for item in self.items:
            item.update_quality()
