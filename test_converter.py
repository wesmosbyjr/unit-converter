from converter import celsius_to_fahrenheit, miles_to_km

def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32

def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212

def test_miles_to_km():
    assert miles_to_km(1) == 1.60934