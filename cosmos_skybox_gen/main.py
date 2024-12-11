import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from image_gen_hor_alt import create_planet_skybox

planets = {
    "Луна": "moon",
    "Меркурий": "mercury",
    "Венера": "venus",
    "Земля": "earth",
    "Марс": "mars",
    "Юпитер": "jupiter",
    "Сатурн": "saturn",
    "Уран": "uranus",
    "Нептун": "neptune"
}

# Переменная для хранения последнего сгенерированного изображения
last_generated_image_path = 'skybox.png'

def generate_parameters():
    global last_generated_image_path
    selected_planet = planet_var.get()
    create_planet_skybox(planets[selected_planet])
    last_generated_image_path = 'skybox.png'
    img = Image.open(last_generated_image_path)
    img_tk = ImageTk.PhotoImage(img)
    output_label.config(image=img_tk)
    output_label.image = img_tk

def save_image():
    global last_generated_image_path
    img = Image.open(last_generated_image_path)
    img.save('skybox.tga')

root = tk.Tk()
root.title("Генератор скайбоксов")
root.iconbitmap("globe_earth_planet_2767.ico")

planet_var = tk.StringVar(value=list(planets.keys())[0])
planet_menu = ttk.Combobox(root, textvariable=planet_var, values=list(planets.keys()))
planet_menu.pack(pady=10)

generate_button = tk.Button(root, text="Сгенерировать", command=generate_parameters)
generate_button.pack(pady=10)

save_button = tk.Button(root, text="Сохранить", command=save_image)
save_button.pack(pady=10)

output_label = tk.Label(root, text="")
output_label.pack(pady=10)

root.mainloop()