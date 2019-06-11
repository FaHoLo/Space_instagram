import os
from instabot import Bot
bot = Bot()
from dotenv import load_dotenv
load_dotenv()
from PIL import Image


def main():
    log_into_insta()
    upload_images_from_folder('images')

def log_into_insta():
    INSTA_LOGIN = os.getenv('INSTA_LOGIN')
    INSTA_PASSWORD = os.getenv('INSTA_PASSWORD')
    bot.login(username=INSTA_LOGIN, password=INSTA_PASSWORD)

def upload_images_from_folder(folder_name):
    images_name = os.listdir(folder_name)
    for image_number, image_name in enumerate(images_name):
        if not image_name.endswith('.jpg') or not image_name.endswith('.jpeg'):
            image = Image.open(os.path.join('images', f'{image_name}'))
            rgb_image = image.convert('RGB')
            rgb_image.save(os.path.join('images', f'{image_name}.jpg'))
            upload_image_to_insta(f'{image_name}.jpg')
        else:
            upload_image_to_insta(image_name)  
        print(f'{image_number + 1} of {len(images_name)} images uploaded')

def upload_image_to_insta(image_name):
    bot.upload_photo(os.path.join('images', f'{image_name}'), caption=f'Here is {image_name} image')

if __name__ == '__main__':
    main()
