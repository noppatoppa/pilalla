from PIL import Image, ImageDraw, ImageFont
import random

"""
Pilalla. Image macro. Stupid.

TODO:
- Puts words to separate file
- Do web / Telegram-bot integration
- Push to Github
"""

PILALLA = (
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
)


def background():
    """
    Load background image.
    :return: Image object
    """
    image = Image.open("background.jpeg")
    return image


def set_text(img, text):
    """
    Draws text on to background image.
    :param img: background image object
    :param text: String
    :return: Image object with text
    """
    font = ImageFont.truetype("FreeSans.ttf", 15)
    d = ImageDraw.Draw(img)
    d.text((75, 110), text=f"{text} on pilalla,\npelkkää paskaa tilalla", fill=(255, 255, 255), align='center',
           font=font)
    return img


def save_img(img):
    """
    Save image file
    :param img: Image object
    """
    img.save('pilalla.png')


def pilalla():
    image = background()
    image_with_text = set_text(image, random.choice(PILALLA))
    save_img(image_with_text)


if __name__ == '__main__':
    pilalla()
