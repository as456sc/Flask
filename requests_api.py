import requests

HOST = 'http://127.0.0.1:8000'


def post():
    post_data = {
        'title': 'Flower',
        'description': 'Flower is a beautiful',
        'owner': 'Djim'
    }
    response = requests.post(f'{HOST}/advertisements', json=post_data)
    print(response.json())


def get():
    response = requests.get(f'{HOST}/advertisement/1')
    print(response.json())


def delete():
    response = requests.delete(f'{HOST}/advertisements/1')
    print(response.json())