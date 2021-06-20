from gilded_rose.items.backstage_passes import BackstagePasses

def test_backstage_passes_normal():
    backstage_passes = BackstagePasses(sell_in=15, quality=2)
    backstage_passes.update_quality()
    assert backstage_passes.quality == 3

def test_backstage_passes_10_days_pre_expire():
    backstage_passes = BackstagePasses(sell_in=10, quality=2)
    backstage_passes.update_quality()
    assert backstage_passes.quality == 4

def test_backstage_passes_5_days_pre_expire():
    backstage_passes = BackstagePasses(sell_in=5, quality=2)
    backstage_passes.update_quality()
    assert backstage_passes.quality == 5

def test_backstage_passes_post_expire():
    backstage_passes = BackstagePasses(sell_in=0, quality=2)
    backstage_passes.update_quality()
    assert backstage_passes.quality == 0
