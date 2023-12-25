import json
from datetime import date
from decimal import Decimal

json_str = '''
{
    "a": 1,
    "b": "2",
    "c": true
}
'''

decoded = json.loads(json_str)
encoded = json.dumps(decoded)

# print(decoded)
# print(encoded)

stock_data = {
    'symbol': 'IBM',
    'date': date(2024, 1, 31),
    'day': {
        'open': Decimal('100.11'),
        'high': Decimal('150.11'),
        'low': Decimal('100.11'),
        'close': Decimal('120.11'),
        'volume': 5_124_200,
    }
}


def encode_stock(obj):
    if (isinstance(obj, date)):
        return obj.isoformat()
    elif (isinstance(obj, Decimal)):
        return round(float(obj), 2)
    else:
        raise ValueError(f'Invalid value {obj}')


ecoded_stock = json.dumps(stock_data, default=encode_stock, indent=2)

print(f'ecoded_stock: {ecoded_stock}')
