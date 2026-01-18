from scr.fairsharer import fair_sharer
def test_fair_sharer():
    

    result = fair_sharer([10, 20, 30, 40, 50, 0], 4, 0.1)
    expected = [10, 20, 34.0, 38.0, 10.0, 0]
    assert result == expected