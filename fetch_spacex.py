import requests
import pathlib
import json


def main():
    pathlib.Path('images').mkdir(parents=True, exist_ok=True) 
    fetch_spacex_last_launch()

def download_image(url, image_name):
    response = requests.get(url)
    if response.ok:
        with open(f'images/{image_name}', 'wb') as new_file:
            new_file.write(response.content)
    else:
        with open(f'images/{image_name}.txt', 'w') as new_file:
            new_file.write(f'{response}, {response.content}')

def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/65'
    response = requests.get(url)
    if response.ok:
        spacex_links = response.json()['links']['flickr_images']
        for link_number, link in enumerate(spacex_links):
            download_image(link, f'spacex_{link_number}.jpg')
    else:
        with open(f'images/spacex_lust_launch.txt', 'w') as new_file:
            new_file.write(f'{response}, {response.content}')

if __name__ == '__main__':
    main()
