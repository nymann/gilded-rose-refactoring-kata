from __future__ import annotations
from abc import abstractmethod

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

def update_aged_brie_quality(item: Item):
    item.quality += 1

    if item.sell_in <= 0:
        item.quality += 1
    if item.quality > 50:
        item.quality = 50
    item.sell_in -= 1

def update_backstage_passes_concert_quality(item: Item):
    item.quality += 1

    if item.sell_in <= 10:
        item.quality += 1
    if item.sell_in <= 5:
        item.quality += 1

    if item.quality > 50:
        item.quality = 50

    if item.sell_in <= 0:
        item.quality = 0

    item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    @abstractmethod
    def update_quality(self):
        raise NotImplementedError


class Sulfuras(Item):
    def update_quality(self):
        pass

class AgedBrie(Item):
    def update_quality(self):
        self.quality += 1

        if self.sell_in <= 0:
            self.quality += 1
        if self.quality > 50:
            self.quality = 50
        self.sell_in -= 1

class BackstagePasses(Item):
    def update_quality(self):
        self.quality += 1

        if self.sell_in <= 10:
            self.quality += 1
        if self.sell_in <= 5:
            self.quality += 1

        if self.quality > 50:
            self.quality = 50

        if self.sell_in <= 0:
            self.quality = 0

        self.sell_in -= 1

