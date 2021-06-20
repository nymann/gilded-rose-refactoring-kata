from __future__ import annotations
from abc import abstractmethod
from typing import Type


class Item:
    item_types = {}

    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __init_subclass__(cls, name: str):
        cls.item_types[name] = cls

    @classmethod
    def create_from_item(cls, item: Item) -> Item:
        """Chooses the relevant subclass where the name matches."""
        item_class: Type[Item] = cls.item_types[item.name]
        return item_class(name=item.name, sell_in=item.sell_in, quality=item.quality)

    def update_quality(self):
        self._change_sell_in()
        self._change_quality()
        self._ensure_quality_within_bounds()

    def _change_sell_in(self):
        # Step 1
        self.sell_in -= 1
    
    @abstractmethod
    def _change_quality(self):
        # Step 2
        raise NotImplementedError

    def _ensure_quality_within_bounds(self):
        # Step 3
        if self.quality > 50:
            self.quality = 50
        if self.quality < 0:
            self.quality = 0
