import requests
import pathlib
import json


def download_image(url, image_name):
    response = requests.get(url)
    with open(f'images/{image_name}', 'wb') as new_file:
        new_file.write(response.content)

def get_link_file_extension(link):
    extansion = link.split('.')[-1]
    return extansion

def fetch_hubble_photo(id):
    url = f'http://hubblesite.org/api/v3/image/{id}'
    last_image_link = requests.get(url).json()['image_files'][-1]['file_url']
    image_extension = get_link_file_extension(last_image_link)
    image_name = f'hubble_{id}.{image_extension}'
    download_image(last_image_link, image_name)

def fetch_hubble_collection(collections_name):
    url = f'http://hubblesite.org/api/v3/images/{collections_name}'
    collection = requests.get(url).json()
    for image_number, image in enumerate(collection):
        fetch_hubble_photo(image['id'])
        print(f'{image_number + 1} of {len(collection)}')

pathlib.Path('images').mkdir(parents=True, exist_ok=True)
fetch_hubble_collection('wallpaper')