from gilded_rose.items.aged_brie import AgedBrie
from gilded_rose.items.conjured import ConjuredItem
from gilded_rose.items.sulfuras import Sulfuras
from gilded_rose.items.backstage_passes import BackstagePasses
from gilded_rose.items.item import Item

class ItemFactory:
    item_types = {
        "Aged Brie": AgedBrie,
        "Sulfuras, Hand of Ragnaros": Sulfuras,
        "Backstage passes to a TAFKAL80ETC concert": BackstagePasses,
        "Conjured": ConjuredItem,
    }

    @classmethod
    def create_item(cls, item: Item) -> Item:
        item_type = cls.item_types[item.name]
        return item_type(name=item.name, quality=item.quality, sell_in=item.sell_in)
