
from PIL import Image

def split_image_into_squares(image_path, output_folder):
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

# Пример использования
split_image_into_squares('skybox.png', 'skybox')