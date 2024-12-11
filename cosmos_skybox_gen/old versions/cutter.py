from PIL import Image
images = []
image_path = 'skybox.png'
output_folder = 'skybox'

# Открываем изображение
image = Image.open(image_path)
width, height = image.size
# Определяем размеры квадратов
square_size = min(width // 3, height // 2)
for i in range(3):  # три колонны
    for j in range(2):  # две строки
        left = i * square_size
        upper = j * square_size
        right = left + square_size
        lower = upper + square_size
        # Обрезаем квадрат
        square = image.crop((left, upper, right, lower))
        square.save(f"{output_folder}/square_{j * 3 + i + 1}.png")
        images.append(f"{output_folder}/square_{j * 3 + i + 1}.png")


images = [Image.open(i) for i in images ]

width, height = images[0].size
tga_image = Image.new("RGBA", (width * 4, height * 3),(0,0,0))

#tga_image.save('skybox_done.png')


tga_image.paste(images[4], (width, 0))         # front
tga_image.paste(images[1], (0, height))        # left
tga_image.paste(images[0], (width * 2, height)) # right
tga_image.paste(images[5], (width, height * 2)) # back
tga_image.paste(images[2], (width*3, height))    # top
tga_image.paste(images[3], (width, height )) # bottom


tga_image.save('skybox.tga', format='TGA')