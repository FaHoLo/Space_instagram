import pathlib

import requests

from download_img import download_image


def main():
    pathlib.Path('images').mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/65'
    response = requests.get(url)
    response.raise_for_status()
    spacex_links = response.json()['links']['flickr_images']
    for link_number, link in enumerate(spacex_links):
        download_image(link, f'spacex_{link_number}.jpg')


if __name__ == '__main__':
    main()
