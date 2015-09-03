print 'Enter bet: '
bet = int(raw_input())

print 'Roll the first die: '
d1 = int(raw_input())

assert 1 <= d1 <= 6

print 'Roll the second die: '
d2 = int(raw_input())

assert 1 <= d2 <= 6

sum = d1 + d2

two_to_1 = [2, 12]
even_money = [3, 4, 9, 10, 11]
field_wins = two_to_1 + even_money
payout = 0

if sum in even_money:
  payout = bet
elif sum in two_to_1:
  payout = bet * 2

if sum in field_wins:
  print 'You have won! Your payout is $%d.' % payout
else:
  print 'Sorry, you have lost! Please play again soon.'