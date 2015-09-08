# A block of stock has a number of attributes, including a purchase date, a purchase price,
# a number of shares, and a ticker symbol. We can record these pieces of information in a
# tuple for each block of stock and do a number of simple operations on the blocks.
#
# Let's dream that we have the following portfolio:
#     Purchase Date     Purchase Price     Shares     Symbol     :Current Price
#     -------------     --------------     ------     ------     --------------
#     25 Jan 2001       43.50              25         CAT        92.45
#     25 Jan 2001       42.80              50         DD         51.19
#     25 Jan 2001       42.10              75         EK         34.87
#     25 Jan 2001       37.58              100        GM         37.58
#
# We can represent each block of stock as a 5-tuple with purchase date, purchase price,
# shares, ticker symbol, and current price.

portfolio = [
 ('25-Jan-2001', 43.50, 25, 'CAT', 92.45),
 ('25-Jan-2001', 42.80, 50, 'DD', 51.19),
 ('25-Jan-2001', 42.10, 75, 'EK', 34.87),
 ('25-Jan-2001', 37.58, 100, 'GM', 37.58)
]

# Develop a function that examines each block, multiplies shares by purchase price, and 
# determines the total purchase price of the portfolio.

def purchasePrice(portfolio):
  price = 0

  for block in portfolio:
    price += block[1] * block[2]

  return price

# Develop a second function that examines each block, multiplies shares by purchase price
# and shares by current price and determines the total amount gained or lost.

def profitOrLoss(portfolio):
  initial = purchasePrice(portfolio)
  current = 0

  for block in portfolio:
    current += block[4] * block[2]

  return current - initial