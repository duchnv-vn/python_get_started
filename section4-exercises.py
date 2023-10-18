## Exercise 1
a = None

if a == None:
  a = "N/A"

# print("Exercise 1", {'a': a})

## Exercise 2
a = 123

a = "N/A" if a == None else a

# print("Exercise 2", {'a': a})

## Exercise 3
score = 790
rating = 'Poor'

if score >= 800:
  rating = 'Excellent'
elif score >= 740:
  rating = 'Very Good'
elif score >= 670:
  rating = 'Good'
elif score >= 580:
  rating = 'Fair'



# print('Exercise 3', {'score': score, 'rating': rating})

## Exercise 4
magnitude = 'seconds'
elapsed = 59

minute = 60
hour = minute * 60
day = hour * 24
week = day * 7

if elapsed > week:
  magnitude = 'weeks'
elif elapsed > day:
  magnitude = 'days'
elif elapsed > hour:
  magnitude = 'hours'
elif elapsed > minute:
  magnitude = 'minutes'

# print('Exercise 3', {'magnitude': magnitude, 'elapsed': elapsed})

