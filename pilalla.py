from PIL import Image, ImageDraw, ImageFont
import random

"""
Pilalla. Image macro.

TODO:
- Puts words to separate file
- Do web / Telegram-bot integration
- Push to Github 
"""

def background():
    image = Image.open("download.jpeg")
    return image

def set_text(img, text):
    font = ImageFont.truetype("FreeSans.ttf", 15)
    d = ImageDraw.Draw(img)
    d.text((75,110), text=f"{text} on pilalla,\npelkkää paskaa tilalla", fill=(255,255,255), align='center', font=font)
    print('text')
    return img

def save_img(img):
    print('save')
    img.save('pil_red.png')

def pilalla():
    image = background()
    image_with_text = set_text(image, random.choice(
        [
            "Tietokoneet",
            "Ihmiset",
            "Oluet",
            "Musiikki",
            "Pelit",
            "Opiskelut",
            "Duunit",
            "Elämäntavat",
            "Naapurit",
            "Ruokavalio",
            "Politiikka",
            "Paini",
            "Urheilu",
            "Talous"
        ]
    ))
    save_img(image_with_text)

if __name__ == '__main__':
    pilalla()