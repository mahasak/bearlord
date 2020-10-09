import os
import datetime as dt

from dotenv import load_dotenv
from airtable import Airtable

load_dotenv()

AIRTABLE_KEY = os.getenv('AIRTABLE_KEY')
AIRTABLE_BASE = os.getenv('AIRTABLE_BASE')


class ExpenseTracker:
    # default constructor
    def __init__(self):
        pass

    def connect(self, table):
        self.expense_table = Airtable(AIRTABLE_BASE, table, AIRTABLE_KEY)

    def parse_message(self, type, payload):
        data = payload.split(' ')
        date_obj = dt.datetime.now()
        initial_amount = float(data[1]) if len(data) >= 2 else 0

        record = {
            "Date": date_obj.strftime("%Y-%m-%d"),
            "Year": date_obj.year,
            "Month": date_obj.month,
            "Day": date_obj.day,
            "Category": data[4] if len(data) >= 5 else "",
            "Type": type,
            "Amount": (0-initial_amount) if type == "EXPENSE" else initial_amount,
            "Currency": data[2] if len(data) >= 3 else "SGD",
            "Description": data[3] if len(data) >= 4 else "",
            "Status": 1
        }

        return record

    def add(self, type, message):
        payload = self.parse_message(type, message)
        status = self.expense_table.insert(payload)

        if status:
            return "{} {} {} has been added to tracker ! Meow !".format(type.capitalize(), payload["Amount"], payload["Currency"])
        else:
            return "{} {} {} failed to add to tracker ! Meow !".format(type.capitalize(), payload["Amount"], payload["Currency"])
