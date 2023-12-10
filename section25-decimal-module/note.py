from decimal import Decimal

decimal_1 = Decimal(0.1)
decimal_2 = Decimal('0.1')
float_1 = float(0.1)

print(f'decimal_1: {decimal_1}')
print(f'decimal_2: {decimal_2}')
print(f'float_1: {float_1}')
print(decimal_1 == decimal_2)
print(decimal_2 == float_1)
print(decimal_1 == float_1)
