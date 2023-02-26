import math

def simple_discount(cashflow, time_in_years, rate):
    return cashflow / (1 + time_in_years * rate)


def compound_discount(cashflow, time_in_years, rate):
    time_split = math.modf(time_in_years)
    print(time_split)
    full_years_dicount =  cashflow / ((1 + rate) ** time_split[1])
    if time_split[0] == 0:
        return full_years_dicount
    else:
        return simple_discount(full_years_dicount, time_split[0], rate)
