class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self._change_sell_in()
        self._change_quality()
        self._ensure_quality_within_bounds()

    def _change_sell_in(self):
        # Step 1
        self.sell_in -= 1
    
    def _change_quality(self):
        # Step 2
        self.quality -= 1

    def _ensure_quality_within_bounds(self):
        # Step 3
        if self.quality > 50:
            self.quality = 50
        if self.quality < 0:
            self.quality = 0
