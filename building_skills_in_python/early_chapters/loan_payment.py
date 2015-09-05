principal = 110000
monthly_interest_rate = 0.0725 / 12
n = 30 * 12

payment = (-monthly_interest_rate * principal * (monthly_interest_rate + 1) ** n) / \
(((monthly_interest_rate + 1) ** n - 1) * (monthly_interest_rate + 1))

print "The monthly payment is $%d" % abs(round(payment, 2))