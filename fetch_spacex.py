import requests
import pathlib
import json


def download_image(url, image_name):
    response = requests.get(url)
    with open(f'images/{image_name}', 'wb') as new_file:
        new_file.write(response.content)

def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/65'
    spacex_links = requests.get(url).json()['links']['flickr_images']
    for link_number, link in enumerate(spacex_links):
        download_image(link, f'spacex_{link_number}.jpg')

pathlib.Path('images').mkdir(parents=True, exist_ok=True) 
fetch_spacex_last_launch()