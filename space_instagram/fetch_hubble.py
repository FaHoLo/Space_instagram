import requests
import pathlib
import os
from download_img import download_image


def main():
    pathlib.Path('images').mkdir(parents=True, exist_ok=True)
    fetch_hubble_collection('wallpaper')


def fetch_hubble_photo(id):
    url = f'http://hubblesite.org/api/v3/image/{id}'
    response = requests.get(url)
    response.raise_for_status()
    last_image_link = response.json()['image_files'][-1]['file_url']
    image_extension = os.path.splitext(last_image_link)[-1]
    image_name = f'hubble_{id}{image_extension}'
    download_image(last_image_link, image_name)


def fetch_hubble_collection(collections_name):
    url = f'http://hubblesite.org/api/v3/images/{collections_name}'
    response = requests.get(url)
    response.raise_for_status()
    collection = response.json()
    for image_number, image in enumerate(collection):
        fetch_hubble_photo(image['id'])
        print(f'{image_number + 1} of {len(collection)}')


if __name__ == '__main__':
    main()
