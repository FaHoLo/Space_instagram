import requests
import pathlib
import os
import json


def main():
    pathlib.Path('images').mkdir(parents=True, exist_ok=True)
    fetch_hubble_collection('wallpaper')

def download_image(url, image_name):
    response = requests.get(url)
    if response.ok:
        with open(f'images/{image_name}', 'wb') as new_file:
            new_file.write(response.content)
    else:
        with open(f'images/{image_name}.txt', 'w') as new_file:
            new_file.write(f'{response}, {response.content}')

def get_link_file_extension(link):
    extansion = link.split('.')[-1]
    return extansion

def fetch_hubble_photo(id):
    url = f'http://hubblesite.org/api/v3/image/{id}'
    response = requests.get(url)
    if last_image_link.ok:
        last_image_link = response.json()['image_files'][-1]['file_url']
        image_extension = os.path.splitext(last_image_link)[-1]
        image_name = f'hubble_{id}{image_extension}'
        download_image(last_image_link, image_name)
    else:
        with open(f'hubble_{id}.txt', 'w') as new_file:
            new_file.write(f'{response}, {response.content}')

def fetch_hubble_collection(collections_name):
    url = f'http://hubblesite.org/api/v3/images/{collections_name}'
    response = requests.get(url)
    if response.ok:
        collection = response.json()
        for image_number, image in enumerate(collection):
            fetch_hubble_photo(image['id'])
            print(f'{image_number + 1} of {len(collection)}')
    else:
        with open(f'hubble_collection.txt', 'w') as new_file:
            new_file.write(f'{response}, {response.content}')

if __name__ == '__main__':
    main()
