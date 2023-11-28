from unittest import TestCase

# from main import format_money

# Format Money
# * Takes a value and outputs to 2dp with default currency of £
# * Takes an optional currency and outputs currency symbol (USD and GBP only)
# * Currency is accepted as a three letter code (otherwise value error is thrown)
# * If currency doesn't exist, exception is thrown
# * If value is less than zero, exception is thrown
# * If the currency is EUR, negative values are allowed


class TestFormatMoney(TestCase):
    pass

    # def test_it_takes_a_value_outputs_money_to_2dp(self):
    #     self.assertEqual(format_money(1), "£1.00")
    #     self.assertEqual(format_money(1.1), "£1.10")
    #     self.assertEqual(format_money(1.11), "£1.11")
    #     self.assertEqual(format_money(1.111), "£1.11")
    #     self.assertEqual(format_money(1.116), "£1.12")

    # def test_it_takes_gpb_or_usd_as_currency(self):
    #     self.assertEqual(format_money(1, "GBP"), "£1.00")
    #     self.assertEqual(format_money(1, "USD"), "$1.00")

    # def test_it_throws_an_excpetion_if_currency_is_not_a_three_letter_code(self):
    #     with self.assertRaises(ValueError):
    #         format_money(1, "US")

    #     with self.assertRaises(ValueError):
    #         format_money(1, "USDD")

    #     with self.assertRaises(ValueError):
    #         format_money(1, "")

    # def test_it_throws_an_exception_if_currency_does_not_exist(self):
    #     with self.assertRaises(ValueError):
    #         format_money(1, "XXX")

    # def test_it_throws_an_exception_if_value_is_less_than_zero(self):
    #     with self.assertRaises(ValueError):
    #         format_money(-1)

    #     with self.assertRaises(ValueError):
    #         format_money(-1, "USD")

    # def test_it_allows_negative_values_if_currency_is_eur(self):
    #     self.assertEqual(format_money(-1, "EUR"), "€-1.00")
    #     self.assertEqual(format_money(-1.1, "EUR"), "€-1.10")