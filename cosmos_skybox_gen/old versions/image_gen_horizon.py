import random

from PIL import Image, ImageDraw
import numpy as np
from settings_loader import get_processor_settings
import os
settings = get_processor_settings()
def create_planet_skybox(planet):
    width, height = 1000, 800
    image = Image.new('RGB', (width, height), (0, 0, 0))
    pixels = image.load()
    draw = ImageDraw.Draw(image)

    num_points = 10000
    for _ in range(num_points):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        pixels[x, y] = (255, 255, 255)

    planets = settings[planet]
    for planet in planets:
        print(planet)
        obj = Image.open(os.path.join('planet',planet)).convert("RGBA").resize((planets[planet],planets[planet]))
        rad,rad = obj.size
        position = (random.randint(1,500)),random.randint(1,400-(rad//2)) # не хочу чтобы уходила наверх и в бока
        print(position)
        image.paste(obj,position,obj)

    draw.rectangle([0,400,1000,1000],fill=(0,0,0))
    image.save('skybox.png')

create_planet_skybox('moon')


