from converter import celsius_to_fahrenheit, miles_to_km, kg_to_lbs


def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32


def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212


def test_miles_to_km():
    assert miles_to_km(1) == 1.60934


def test_kg_to_lbs():
    assert kg_to_lbs(1) == 2.20462
