import random

from PIL import Image, ImageDraw
import numpy as np
from settings_loader import get_processor_settings
import os
settings = get_processor_settings()
def create_planet_skybox(planet):
    width, height = 1000, 600
    image = Image.new('RGB', (width, height), (0, 0, 0))
    pixels = image.load()
    draw = ImageDraw.Draw(image)

    star_points = random.randint(2000,8000)
    for _ in range(star_points):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        pixels[x, y] = (255, 255, 255)

    planets = settings[planet]
    for planet in planets:
        print(planet)
        obj = Image.open(os.path.join('planet',planet)).convert("RGBA").resize((planets[planet][0],planets[planet][1]))
        radx,rady = obj.size
        position = (random.randint(0,1000)),random.randint(0,300-(rady//2))
        while (position[0] in range(0,250) or position[0] in range(500-(radx//2),1001)) and (position[1] in range(0,200)):
            position = (random.randint(0, 1000)), random.randint(0, 300 - (rady // 2))
            print("REROLL")
        print(position)
        image.paste(obj,position,obj)

    draw.rectangle([0,300,1000,1000],fill=(0,0,0))
    draw.rectangle([0,0,250,200],fill=(100,100,100))
    draw.rectangle([500, 0, 1000, 200], fill=(100, 100, 100))
    draw.rectangle([500, 400, 1000, 600], fill=(100, 100, 100))
    draw.rectangle([0, 400, 250, 600], fill=(100, 100, 100))
    draw.rectangle([500, 400, 1000, 600], fill=(100, 100, 100))
    image.save('skybox.png')
    image.save('skybox.tga',format="TGA")




