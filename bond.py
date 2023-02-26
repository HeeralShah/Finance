import math as math
from datetime import date, datetime as dt, timedelta
from functools import singledispatchmethod as dispatch

import numpy as np

class Bond:

    _days_to_maturity: int
    _maturity_date: date
    coupon: np.double
    compounding_periods: list[np.double]
    compounding_dates: list[date]
    price: np.double
    yield_to_maturity: np.double
    coupon_yield: np.double
    date_string_format: str
    

    def __init__(self, maturity=0, coupon: np.double=0, compounding_times=None, value=0, date_string_format: str=None):

        self.coupon = coupon
        self.date_string_format = date_string_format

        self._set_maturity(maturity)
        self._compounding_times = compounding_times

    @property
    def maturity_date(self):
        return self._maturity_date
    
    @property
    def days_to_maturity(self):
        return self._days_to_maturity
    
    

    
    @dispatch
    def _set_maturity(self, maturity):
        raise NotImplementedError("cannot set maturity for this data type")
    
    @_set_maturity.register
    def _(self, maturity: date):
        self._maturity_date = maturity
        self._days_to_maturity = (maturity - dt.now().date()).days

    @_set_maturity.register
    def _(self, maturity: int):
        self._days_to_maturity = maturity
        self._maturity_date = dt.now() + timedelta(days=maturity)

    @_set_maturity.register
    def _(self, maturity: str):
        if self.date_string_format == None:
            raise NotImplementedError("format of date strings has not been provided")
        self._maturity_date = dt.strptime(maturity, self.date_string_format).date()
        self._days_to_maturity = (self._maturity_date - dt.now().date()).days










    
    def ytm_to_price(yield_to_maturity, compounding_periods, coupon, maturity):
        pass

    def price_to_ytm(price, compounding_periods, coupon, maturity):
        pass


    
if __name__ == '__main__':
    bond = Bond(maturity='4 Aug 2023', coupon=2, compounding_times=[42,125], date_string_format="%d %b %Y")
    print(bond.maturity_date)
    bond = Bond(maturity='4 Aug 2023', coupon=2, compounding_times=[42,125])
    print(bond.maturity_date)





