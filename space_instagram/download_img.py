import os

import requests


def download_image(url, image_name):
    response = requests.get(url)
    response.raise_for_status()
    with open(os.path.join('images', f'{image_name}'), 'wb') as new_file:
        new_file.write(response.content)
