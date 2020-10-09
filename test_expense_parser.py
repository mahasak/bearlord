import pytest

from expense import ExpenseTracker


class TestExpenseTracker(object):
    def test_parse_amount_only(self):
        test_payload = "?>expense 20"
        tracker = ExpenseTracker()
        payload = tracker.parse_message("EXPENSE", test_payload)
        assert payload["Amount"] == -20
        assert payload["Currency"] == "SGD"
        assert payload["Description"] == ""
        assert payload["Category"] == ""

    def test_parse_amount_and_currency(self):
        test_payload = "?>expense 20 THB"
        tracker = ExpenseTracker()
        payload = tracker.parse_message("EXPENSE", test_payload)
        assert payload["Amount"] == -20
        assert payload["Currency"] == "THB"
        assert payload["Description"] == ""
        assert payload["Category"] == ""

    def test_parse_amount_with_currency_and_description(self):
        test_payload = "?>expense 20 THB Manga"
        tracker = ExpenseTracker()
        payload = tracker.parse_message("EXPENSE", test_payload)
        assert payload["Amount"] == -20
        assert payload["Currency"] == "THB"
        assert payload["Description"] == "Manga"
        assert payload["Category"] == ""

    def test_parse_amount_with_currency_and_description_and_category(self):
        test_payload = "?>expense 20 THB Manga ENT"
        tracker = ExpenseTracker()
        payload = tracker.parse_message("EXPENSE", test_payload)
        assert payload["Amount"] == -20
        assert payload["Currency"] == "THB"
        assert payload["Description"] == "Manga"
        assert payload["Category"] == "ENT"
