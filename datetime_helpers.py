from datetime import datetime as dt, date
from calendar import isleap

import numpy as np



NON_LEAP_YEAR_DAYS = 365
LEAP_YEAR_DAYS = 366


#still a mistake becasue if end date is leap year then denominator becomes 366 even if the date does not go over 29 feb which isn't correct.  only impacts at 6dp so irrelevant for pricing but needs to be fixed.

def relative_date_in_years(start_date: date, end_date: date) -> np.double:

    days_from_start_year = (dt(start_date.year, 12, 31) - start_date).days + 1
    days_from_end_year = (end_date - dt(end_date.year, 1, 1)).days + 1

    print(days_from_start_year)
    print(days_from_end_year)

    years_inbetween = end_date.year - start_date.year - 1

    start_year_length = NON_LEAP_YEAR_DAYS if not isleap(start_date.year) else LEAP_YEAR_DAYS
    end_year_length = NON_LEAP_YEAR_DAYS if not isleap(end_date.year) else LEAP_YEAR_DAYS
    
    return (days_from_start_year / start_year_length) + years_inbetween + (days_from_end_year / end_year_length)


