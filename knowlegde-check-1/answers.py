## QUESTION 1 => Answer: a
character_0 = "\u00E3"
character_1 = "\u00C3"
character_2 = "\u0040"
character_3 = "\u13F0"
character_4 = "\u2102"

# print(f'character_1: {character_0}')
# print(f'character_1: {character_1}')
# print(f'character_2: {character_2}')
# print(f'character_3: {character_3}')
# print(f'character_4: {character_4}')

## ------------------------------------------------------------
## QUESTION 2 => Answer: d
s1 = 'abCdeF'
s2 = 'ABCdeF'
compare = s1.casefold() == s2.casefold()

# print(f'compare: {compare}')

## ------------------------------------------------------------
## QUESTION 3 => Answer: b, c
s = '3.14/4.15/6.7/8.9'
solution_1 = s.split('/')[1]

solution_2 = float(s.split('/')[-3])

# print(f'solution_1: {solution_1}')
# print(f'solution_2: {solution_2}')

## ------------------------------------------------------------
## QUESTION 4 => Answer: c
data = 'this is the example string'
s = 'th'
check_contain = s in data

# print(f'check_contain: {check_contain}')

## ------------------------------------------------------------
## QUESTION 5 => Answer: a
def find_first_negative(numbers):
    negative_number = None
    number_index = None

    for index, value in zip(range(len(numbers)), numbers):
        if(value < 0):
            negative_number = value
            number_index = index
            break

    return negative_number, number_index

negative_number, number_index = find_first_negative([-1,2,3,4,-1])

# print(f'negative_number: {negative_number}')
# print(f'number_index: {number_index}')

## ------------------------------------------------------------
## QUESTION 6 => Answer: d
def validate(num):
    if not(isinstance(num, int) and num > 0 and num < 100):
        raise ValueError('Invalid input')

# result = validate(1)

## ------------------------------------------------------------
## QUESTION 7 => Answer: c
def func_7(arg_1, arg_2, *, kwarg_3=True):
    pass
## ------------------------------------------------------------
## QUESTION 8 => Answer: 6.27
def func_8(*, a, b, c):
    x = (-b + ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a)
    return round(x, 2)

result_8_1 = func_8(a=3, b=4, c=-5)
result_8_2 = func_8(a=1, b=-5, c=-8)

# print(f'result_8_1: {result_8_1}')
# print(f'result_8_2: {result_8_2}')
## ------------------------------------------------------------
## QUESTION 9 => Answer: Isaac Newton
def encrypt(s):
    return ''.join(chr(ord(c) + 10) for c in s)

def decrypt(encryted_s):
    output_str = ''
    list_of_s =[chr(ord(c) - 10) for c in encryted_s]
    return output_str.join(list_of_s)

decrypted_result = decrypt('S}kkm*Xo\x81~yx')

# print(f'decrypted_result: {decrypted_result}')
## ------------------------------------------------------------
## QUESTION 10 => Answer: d
currencies = 'USD, CAD, USD, JPY,  AUD'
values = [100, 200, 300, 400, 500]

def func_1(currencies, values):
    currencies = currencies.split(',')
    result = ''
    for i in range(min(len(currencies), len(values))):
        currency = currencies[i].strip()
        value = str(values[i])
        result = result + value + ' ' + currency + ', '
    return result.strip(', ')

def func_2(currencies, values):
    currencies = [s.strip() for s in currencies.split(',')]
    result = []
    for currency, value in zip(currencies, values):
        result.append(str(value) + ' ' + currency)
    return ', '.join(result)

def func_3(currencies, values):
    return ', '.join(
        [
            str(v1) + ' ' + v2
            for v1, v2 in zip(
                values,
                [s.strip() for s in currencies.split(',')]
            )
        ]
    )

def func_4(currencies, values):
    currencies = [s.strip() for s in currencies.split(',')]
    result = [
        ' '.join([str(v1), v2])
        for v1, v2 in zip(values, currencies)
    ]
    return ', '.join(result)

result_10_1 = func_1(currencies, values)
result_10_2 = func_2(currencies, values)
result_10_3 = func_3(currencies, values)
result_10_4 = func_4(currencies, values)

# print(f'result_10_1: {result_10_1}')
# print(f'result_10_2: {result_10_2}')
# print(f'result_10_3: {result_10_3}')
# print(f'result_10_4: {result_10_4}')