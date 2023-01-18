def mortgage(rate, borrowedmon):
    monthpay = round((rate/12) * (1/(1-(1+rate/12)**(-360)))*borrowedmon, 5)
    return monthpay

rate = float(input("Annual Interest Rate: "))
borrowedmon = float(input("Money Borrowed: "))
print(mortgage(rate, borrowedmon), "dollors per month")