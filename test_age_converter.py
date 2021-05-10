import unittest
from age_converter import convert_age, days_in_year, hours_in_year, minutes_in_year, seconds_in_year


class TestConvertAge(unittest.TestCase):
    def test_types(self):
        # make sure type errors are raised when necessary
        self.assertRaises(TypeError, convert_age, "twenty years old")
        self.assertRaises(TypeError, convert_age, 15 + 2j)
        self.assertRaises(TypeError, convert_age, False)
        self.assertRaises(TypeError, convert_age, [20])

    def test_values(self):
        # make sure that ValueError raise when required
        self.assertRaises(ValueError, convert_age, -4, None)

    def test_converter(self):
        # check if the values are equal approximately
        self.assertAlmostEqual(convert_age(1, '1'), days_in_year)
        self.assertAlmostEqual(convert_age(1, '2'), hours_in_year)
        self.assertAlmostEqual(convert_age(1, '3'), minutes_in_year)
        self.assertAlmostEqual(convert_age(1, '4'), seconds_in_year)
