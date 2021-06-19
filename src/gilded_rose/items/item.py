from abc import abstractmethod


class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    @abstractmethod
    def update_quality(self):
        raise NotImplementedError

    def _ensure_quality_within_bounds(self):
        if self.quality > 50:
            self.quality = 50
        if self.quality < 0:
            self.quality = 0
