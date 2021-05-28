import os
import requests
import logging
from urllib.parse import urlparse
import argparse
from dotenv import load_dotenv

HOST = 'https://api-ssl.bitly.com/v4'


def shorten_link(long_url, headers):
    shorten_body = {
        'long_url': long_url
    }
    response = requests.post(
        url=f'{HOST}/shorten',
        headers=headers,
        json=shorten_body
    )
    response.raise_for_status()

    logging.debug(f'short link status code: {response.status_code}')
    short_link = response.json()['link']
    return short_link


def count_clicks(bitlink, headers):
    params = {
        'unit': 'day',
        'units': '-1'
    }
    response = requests.get(
        url=f'{HOST}/bitlinks/{bitlink}/clicks/summary',
        headers=headers,
        params=params
    )
    response.raise_for_status()

    clicks_count = response.json()['total_clicks']
    return clicks_count


def is_bitlink(bitlink, headers):
    resp = requests.get(f'{HOST}/bitlinks/{bitlink}', headers=headers)
    logging.debug(f'bitlink checking status code: {resp.status_code}')
    return resp.ok


def main():
    
    load_dotenv()
    TOKEN = os.getenv('BITLY_TOKEN')
    HEADERS = {
        'Authorization': f'Bearer {TOKEN}',
    }
    
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(
        description="""Программа позволяет получить bitlink\
         из url или позволяет получить количество переходов\
         по введенному bitlink"""
    )
    parser.add_argument('url', help='Адрес сайта или bitlink')
    args = parser.parse_args()

    url = args.url
    parsed_link = urlparse(url)
    bitly_link = f'{parsed_link.netloc}{parsed_link.path}'
    try:
        if is_bitlink(bitly_link, HEADERS):
            print('clicks_count: ', count_clicks(bitly_link, HEADERS))
        else:
            short_link = shorten_link(url, HEADERS)
            print('bitlink:', short_link)

    except requests.exceptions.HTTPError as err:
        logging.error(f"Can't get data from server:\n{err}")
        exit()


if __name__ == '__main__':
    main()
