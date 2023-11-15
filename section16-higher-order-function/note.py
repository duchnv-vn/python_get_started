## MAP FUNCTION
l = [1,2,3,4,5]

def multiTwo(number):
  print(f'number: {number}')
  return number * 2

iterator = map(multiTwo, l)

print(f'iterator: {list(iterator)}')

## ------------------------------------------------------------------
## CLOSURE
def power(n):
  def inner(x):
    return x ** n
  return inner

