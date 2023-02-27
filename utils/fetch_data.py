import requests


def hit_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        response.raise_for_status()
    else:
        return response
    