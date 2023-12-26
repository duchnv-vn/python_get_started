import requests
import json
FINNHUB_API_KEY = None

with open('.env') as file:
    rows = [row.split(sep='=')
            for row in file.readlines()
            ]

    variables = {
        key: value
        for [key, value] in rows
    }

    FINNHUB_API_KEY = variables['FINNHUB_API_KEY']

BASE_FINNHUB_URL = 'https://finnhub.io/api/v1'
BASE_WEB_HOOK_URL = f'{BASE_FINNHUB_URL}/webhook'

FINNHUB_HEADERS = {
    'X-Finnhub-Token': FINNHUB_API_KEY
}


def make_finnhub_request():
    QUOTE_URL = f'{BASE_FINNHUB_URL}/quote'

    response = requests.get(
        url=QUOTE_URL,
        params={
            'symbol': 'AAPL'
        },
        headers=FINNHUB_HEADERS
    )

    print(response.status_code)
    print(json.dumps(response.json(), indent=1))


def make_finnhub_webhook_post():
    WEBHOOK_ADD_URL = f'{BASE_WEB_HOOK_URL}/add'

    post_data = {
        'event': 'earnings',
        'symbol': 'AAPL'
    }

    response = requests.post(
        url=WEBHOOK_ADD_URL,
        json=post_data,
        headers=FINNHUB_HEADERS
    )

    print(response.status_code)
    print(response.json())


make_finnhub_webhook_post()
make_finnhub_webhook_post()
make_finnhub_webhook_post()


def make_finnhub_webhook_get():
    WEBHOOK_LIST_URL = f'{BASE_WEB_HOOK_URL}/list'

    response = requests.get(
        url=WEBHOOK_LIST_URL,
        headers=FINNHUB_HEADERS
    )

    print(response.status_code)
    print(response.json())

    return response.json()


webhook_get_data_before = make_finnhub_webhook_get()
id_list = (data['id'] for data in webhook_get_data_before)


def make_finnhub_webhook_delete():

    for id in id_list:
        WEBHOOK_DELETE_URL = f'{BASE_WEB_HOOK_URL}/delete'

        response = requests.post(
            url=WEBHOOK_DELETE_URL,
            json={
                'id': id
            },
            headers=FINNHUB_HEADERS
        )

        print(response.status_code)
        print(response.json())


make_finnhub_webhook_delete()

webhook_get_data_after = make_finnhub_webhook_get()
