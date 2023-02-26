import math
from datetime import date, datetime as dt

import numpy as np
from multipledispatch import dispatch

from datetime_helpers import *
from finance_helpers import *



class CashFlow:

    cashflow: np.double
    rate_of_return: np.double  # must be rate of return in years
    date_of_cashflow: date
    _present_value: np.double

    def __init__ (self, cashflow, rate, date):

        self.cashflow = cashflow
        self.rate_of_return = rate
        self.date_of_cashflow = date
        self._present_value = self._present_value()

    def __str__(self):
        return "cashflow: {0}, rate of return: {1}, date of cashflow: {2}, present value: {3}".format(self.cashflow, self.rate_of_return, self.date_of_cashflow, self.present_value)

    def time_to_cashflow(self):
        now = dt.now()
        return relative_date_in_years(now, self.date_of_cashflow)

    @property
    def present_value(self):
        return self._present_value

    @classmethod
    def calculate_present_value(cls, cashflow, rate, date):
        return cls(cashflow, rate, date)._present_value

    def _present_value(self):
        time_delta = relative_date_in_years(dt.now(), self.date_of_cashflow)
        return compound_discount(self.cashflow, time_delta, self.rate_of_return)
    

    


if __name__ == '__main__':
    cashflow = CashFlow(100, 0.01, dt(2028, 2, 15))
    print(cashflow.present_value)
    print(CashFlow.calculate_present_value(100, 0.01, dt(2028, 2, 15)))