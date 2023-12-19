from decimal import Decimal, getcontext, localcontext, ROUND_HALF_UP

decimal_1 = Decimal(0.1)
decimal_2 = Decimal("0.1")
float_1 = float(0.1)

# print(f'decimal_1: {decimal_1}')
# print(f'decimal_2: {decimal_2}')
# print(f'float_1: {float_1}')
# print(decimal_1 == decimal_2)
# print(decimal_2 == float_1)
# print(decimal_1 == float_1)

with localcontext() as ctx_l:
    ctx_l.prec = 5
    ctx_l.rounding = ROUND_HALF_UP
    print(f"ctx_l: {ctx_l}")
    print(f"example: {round(Decimal('100.445'), 2)}")

ctx = getcontext()

# ctx.prec = 10

print(f"ctx: {ctx}")
print(f"example: {round(Decimal('100.445'), 2)}")
