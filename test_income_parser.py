import pytest

from expense import ExpenseTracker

tracker = ExpenseTracker()
class TestIncomeParser(object):
    def test_parse_amount_only(self):
        test_payload = "?>income 20"
        payload = tracker.parse_message("INCOME", test_payload)
        assert payload["Amount"] == 20
        assert payload["Currency"] == "SGD"
        assert payload["Description"] == ""
        assert payload["Category"] == ""

    def test_parse_amount_and_currency(self):
        test_payload = "?>income 20 THB"
        payload = tracker.parse_message("INCOME", test_payload)
        assert payload["Amount"] == 20
        assert payload["Currency"] == "THB"
        assert payload["Description"] == ""
        assert payload["Category"] == ""

    def test_parse_amount_with_currency_and_description(self):
        test_payload = "?>income 20 THB Testing"
        payload = tracker.parse_message("INCOME", test_payload)
        assert payload["Amount"] == 20
        assert payload["Currency"] == "THB"
        assert payload["Description"] == "Testing"
        assert payload["Category"] == ""

    def test_parse_amount_with_currency_and_description_and_category(self):
        test_payload = "?>income 20 THB Testing SIDE"
        payload = tracker.parse_message("INCOME", test_payload)
        assert payload["Amount"] == 20
        assert payload["Currency"] == "THB"
        assert payload["Description"] == "Testing"
        assert payload["Category"] == "SIDE"
