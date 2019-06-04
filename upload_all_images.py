import os
from instabot import Bot
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

INSTA_LOGIN = os.getenv('INSTA_LOGIN')
INSTA_PASSWORD = os.getenv('INSTA_PASSWORD')

def upload_image_to_insta(image_name):
    bot.upload_photo(f'images/{image_name}', caption=f'Here is {image_name} image')

bot = Bot()
bot.login(username=INSTA_LOGIN, password=INSTA_PASSWORD)
images_name = os.listdir('images')
for image_number, image_name in enumerate(images_name):
    if not image_name.endswith('.jpg') or not image_name.endswith('.jpeg'):
        image = Image.open(f'images/{image_name}')
        rgb_image = image.convert('RGB')
        rgb_image.save(f'images/{image_name}.jpg')
        upload_image_to_insta(f'{image_name}.jpg')
    else:
        upload_image_to_insta(image_name)  
    print(f'{image_number + 1} of {len(images_name)} images uploaded')
