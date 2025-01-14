import re
import io
import sqlite3
from database import create_database, get_instructors
import tkinter as tk
from future.moves.tkinter import ttk
from tkinter import messagebox
import tkintermapview
from tkcalendar import DateEntry
import webbrowser
from datetime import datetime
from PIL import Image, ImageTk

# Создание базы данных
create_database()

# Создание главного окна
W_main = tk.Tk()
W_main.title("Аэропорт Уктус")
W_main.geometry("1200x750")
W_main.resizable(False, False)

# Загрузка фонового изображения
image_path = "gl_fon.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

L1 = tk.Label(W_main, image=photo)
L1.place(x=0, y=0)

# Загрузка изображения меню
image_path2 = "menu.png"
image2 = Image.open(image_path2)
photo2 = ImageTk.PhotoImage(image2)

L2 = tk.Label(W_main, image=photo2)
L2.place(x=0, y=0)

# Загрузка изображений для кнопок
o_nas_img = ImageTk.PhotoImage(Image.open("o_nas.png"))
o_nas_temnee_img = ImageTk.PhotoImage(Image.open("o_nas_temnee.png"))
park_vs_img = ImageTk.PhotoImage(Image.open("park_vs.png"))
park_vs_temnee_img = ImageTk.PhotoImage(Image.open("park_vs_temnee.png"))
zapis_img = ImageTk.PhotoImage(Image.open("zapis.png"))
zapis_temnee_img = ImageTk.PhotoImage(Image.open("zapis_temnee.png"))
instruktory_img = ImageTk.PhotoImage(Image.open("instruktory.png"))
instruktory_temnee_img = ImageTk.PhotoImage(Image.open("instruktory_temnee.png"))

sam_img = ImageTk.PhotoImage(Image.open("sam.png"))
sam_temnee_img = ImageTk.PhotoImage(Image.open("sam_temnee.png"))
vert_img = ImageTk.PhotoImage(Image.open("vert.png"))
vert_temnee_img = ImageTk.PhotoImage(Image.open("vert_temnee.png"))
delta_img = ImageTk.PhotoImage(Image.open("delta.png"))
delta_temnee_img = ImageTk.PhotoImage(Image.open("delta_temnee.png"))
shar_img = ImageTk.PhotoImage(Image.open("shar.png"))
shar_temnee_img = ImageTk.PhotoImage(Image.open("shar_temnee.png"))
par_img = ImageTk.PhotoImage(Image.open("par.png"))
par_temnee_img = ImageTk.PhotoImage(Image.open("par_temnee.png"))

zapis_na_polet_img = ImageTk.PhotoImage(Image.open("zapis_na_polet.png"))
zapis_na_polet_temnee_img = ImageTk.PhotoImage(Image.open("zapis_na_polet_temnee.png"))

back_to_vs_img = ImageTk.PhotoImage(Image.open("k_vybory_vs.png"))
back_to_vs_temnee_img = ImageTk.PhotoImage(Image.open("k_vybory_vs_temnee.png"))

sled_instruktor_img = ImageTk.PhotoImage(Image.open("sled_instruktor.png"))
sled_instruktor_img_dark = ImageTk.PhotoImage(Image.open("sled_instruktor_temnee.png"))

zapisatsa_img = ImageTk.PhotoImage(Image.open("zapisatsa.png"))
zapisatsa_temnee_img = ImageTk.PhotoImage(Image.open("zapisatsa_temnee.png"))

home_img = ImageTk.PhotoImage(Image.open("home.png").resize((65, 60)))
home_temnee_img = ImageTk.PhotoImage(Image.open("home_temnee.png").resize((65, 60)))

sled_vs_img = ImageTk.PhotoImage(Image.open("sled_vs.png").resize((312, 64)))
sled_vs_temnee_img = ImageTk.PhotoImage(Image.open("sled_vs_temnee.png").resize((312, 64)))

vk_img = ImageTk.PhotoImage(Image.open("vk.png").resize((50, 50)))
vk_temnee_img = ImageTk.PhotoImage(Image.open("vk_temnee.png").resize((50, 50)))
youtube_img = ImageTk.PhotoImage(Image.open("youtube.png").resize((70, 50)))
youtube_temnee_img = ImageTk.PhotoImage(Image.open("youtube_temnee.png").resize((70, 50)))

# Функции для обработки событий наведения и покидания кнопок
def on_enter_o_nas(event):
    But1.config(image=o_nas_temnee_img)
    But1.config(activebackground='gray')

def on_leave_o_nas(event):
    But1.config(image=o_nas_img)

def on_enter_park_vs(event):
    But2.config(image=park_vs_temnee_img)
    But2.config(activebackground='gray')

def on_leave_park_vs(event):
    But2.config(image=park_vs_img)

def on_enter_zapis(event):
    But3.config(image=zapis_temnee_img)
    But3.config(activebackground='gray')

def on_leave_zapis(event):
    But3.config(image=zapis_img)

def on_enter_instruktory(event):
    But4.config(image=instruktory_temnee_img)
    But4.config(activebackground='gray')

def on_leave_instruktory(event):
    But4.config(image=instruktory_img)

def on_enter_sam(event):
    But_sam.config(image=sam_temnee_img)
    But_sam.config(activebackground='gray')

def on_leave_sam(event):
    But_sam.config(image=sam_img)

def on_enter_vert(event):
    But_vert.config(image=vert_temnee_img)
    But_vert.config(activebackground='gray')

def on_leave_vert(event):
    But_vert.config(image=vert_img)

def on_enter_delta(event):
    But_delta.config(image=delta_temnee_img)
    But_delta.config(activebackground='gray')

def on_leave_delta(event):
    But_delta.config(image=delta_img)

def on_enter_shar(event):
    But_shar.config(image=shar_temnee_img)
    But_shar.config(activebackground='gray')

def on_leave_shar(event):
    But_shar.config(image=shar_img)

def on_enter_par(event):
    But_par.config(image=par_temnee_img)
    But_par.config(activebackground='gray')

def on_leave_par(event):
    But_par.config(image=par_img)

def on_enter_zapis_na_polet(event):
    zapis_na_polet_button.config(image=zapis_na_polet_temnee_img)
    zapis_na_polet_button.config(activebackground='gray')

def on_leave_zapis_na_polet(event):
    zapis_na_polet_button.config(image=zapis_na_polet_img)

def on_enter_back_to_vs(event):
    back_to_vs_button.config(image=back_to_vs_temnee_img)
    back_to_vs_button.config(activebackground='gray')

def on_leave_back_to_vs(event):
    back_to_vs_button.config(image=back_to_vs_img)

def on_enter_zapisatsa(event):
    zapisatsa_button.config(image=zapisatsa_temnee_img)
    zapisatsa_button.config(activebackground='gray')

def on_leave_zapisatsa(event):
    zapisatsa_button.config(image=zapisatsa_img)

def on_enter_vk(event):
    vk_button.config(image=vk_temnee_img)
    vk_button.config(activebackground='gray')

def on_leave_vk(event):
    vk_button.config(image=vk_img)

def on_enter_youtube(event):
    youtube_button.config(image=youtube_temnee_img)
    youtube_button.config(activebackground='gray')

def on_leave_youtube(event):
    youtube_button.config(image=youtube_img)

# Функции для открытия ссылок в браузере
def open_vk():
    webbrowser.open("https://vk.com/uktus.aero")

def open_youtube():
    webbrowser.open("https://www.youtube.com/channel/UCVMQr_GwBjfqp_HrAGJ2Mmg")

# Глобальные переменные для хранения текущего инструктора и индекса
current_instructor_index = 0
instructors = get_instructors()

def open_instruktory():
    global current_instructor_index, instruktory_window
    current_instructor_index = 0

    instruktory_window = tk.Toplevel(W_main)
    instruktory_window.title("Инструкторы")
    instruktory_window.geometry("1200x700")
    instruktory_window.resizable(False, False)

    background_image_path = "fon_okon.png"
    background_image = Image.open(background_image_path)
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(instruktory_window, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0)

    label_text = tk.Label(
        instruktory_window,
        text="Наши сотрудники - профессионалы своего дела с многолетним опытом работы\n и тысячами довольных клиентов! \nКаждый инструктор отвечает за свой тип воздушного судна,\n пожалуйста, выберите тип ВС для просмотра информации об инструкторе: ",
        font=("Segoe UI", 18, "bold"),
        bg="#9AC1CF",
        fg="#FFFFFF"
    )
    label_text.place(x=80, y=145)

    global But_sam, But_vert, But_delta, But_shar, But_par

    But_sam = tk.Button(instruktory_window, image=sam_img, borderwidth=2, relief="ridge", command=open_instructor_info_sam)
    But_sam.place(x=85, y=340, width=297, height=117)
    But_sam.bind("<Enter>", on_enter_sam)
    But_sam.bind("<Leave>", on_leave_sam)

    But_vert = tk.Button(instruktory_window, image=vert_img, borderwidth=2, relief="ridge", command=open_instructor_info_vert)
    But_vert.place(x=440, y=340, width=297, height=117)
    But_vert.bind("<Enter>", on_enter_vert)
    But_vert.bind("<Leave>", on_leave_vert)

    But_delta = tk.Button(instruktory_window, image=delta_img, borderwidth=2, relief="ridge", command=open_instructor_info_delta)
    But_delta.place(x=800, y=340, width=297, height=117)
    But_delta.bind("<Enter>", on_enter_delta)
    But_delta.bind("<Leave>", on_leave_delta)

    But_shar = tk.Button(instruktory_window, image=shar_img, borderwidth=2, relief="ridge", command=open_instructor_info_shar)
    But_shar.place(x=250, y=500, width=297, height=117)
    But_shar.bind("<Enter>", on_enter_shar)
    But_shar.bind("<Leave>", on_leave_shar)

    But_par = tk.Button(instruktory_window, image=par_img, borderwidth=2, relief="ridge", command=open_instructor_info_par)
    But_par.place(x=600, y=500, width=297, height=117)
    But_par.bind("<Enter>", on_enter_par)
    But_par.bind("<Leave>", on_leave_par)

    home_button = tk.Button(instruktory_window, image=home_img, borderwidth=0, highlightthickness=0, relief="flat", activebackground="#9AC1CF",
                            command=return_instructory_to_main)
    home_button.image = home_img
    home_button.place(x=1093, y=30)

    home_button.bind("<Enter>", lambda e: home_button.config(image=home_temnee_img))
    home_button.bind("<Leave>", lambda e: home_button.config(image=home_img))

def open_instructor_info(vehicle_type, description_position):
    global current_instructor_index
    current_instructor_index = 0

    instructor_info_window = tk.Toplevel(W_main)
    instructor_info_window.title("Информация об инструкторе")
    instructor_info_window.geometry("1200x680")
    instructor_info_window.resizable(False, False)

    frame = tk.Frame(instructor_info_window)
    frame.place(x=0, y=0, width=1200, height=680)

    background_image_path = "fon_okon.png"
    background_image = Image.open(background_image_path)
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(frame, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0)

    filtered_instructors = [instructor for instructor in instructors if
                            instructor[5].lower() == vehicle_type.lower()]

    if not filtered_instructors:
        return

    def update_instructor_info():
        global current_instructor_index
        selected_instructor = filtered_instructors[current_instructor_index]
        name_label.config(text=f"{selected_instructor[1]} {selected_instructor[2]} - {selected_instructor[8]}")
        if selected_instructor[7]:
            try:
                photo_data = selected_instructor[7]
                photo = Image.open(io.BytesIO(photo_data))
                photo = photo.resize((350, 360), Image.LANCZOS)
                photo_image = ImageTk.PhotoImage(photo)
                photo_label.config(image=photo_image)
                photo_label.image = photo_image
            except Exception as e:
                print(f"Ошибка при загрузке фото: {e}")
        if selected_instructor[6]:
            description_label.config(text=selected_instructor[6])

    def next_instructor():
        global current_instructor_index
        current_instructor_index = (current_instructor_index + 1) % len(filtered_instructors)
        frame.after(100, update_instructor_info)  # задержка перед обновлением информации

    name_font = ("Segoe UI", 18, "bold")
    name_label = tk.Label(
        frame,
        text=f"{filtered_instructors[0][1]} {filtered_instructors[0][2]} - {filtered_instructors[0][8]}",
        font=name_font,
        bg="#9AC1CF",
        fg="#FFFFFF"
    )
    name_label.place(x=300, y=40)

    photo_label = tk.Label(frame, bg="#9AC1CF")
    photo_label.place(x=33, y=140)

    description_font = ("Verdana", 14)
    description_label = tk.Label(
        frame,
        text=filtered_instructors[0][6],
        font=description_font,
        wraplength=750,
        justify=tk.LEFT,
        bg="#9AC1CF",
        fg="#FFFFFF"
    )
    description_label.place(x=description_position[0], y=description_position[1])

    global zapis_na_polet_button
    zapis_na_polet_button = tk.Button(
        frame,
        image=zapis_na_polet_img,
        borderwidth=2,
        relief="ridge",
        command=lambda: smooth_transition_to_zapis(instructor_info_window)
    )
    zapis_na_polet_button.place(x=920, y=555, width=232, height=64)
    zapis_na_polet_button.bind("<Enter>", on_enter_zapis_na_polet)
    zapis_na_polet_button.bind("<Leave>", on_leave_zapis_na_polet)

    global back_to_vs_button
    back_to_vs_button = tk.Button(
        frame,
        image=back_to_vs_img,
        borderwidth=2,
        relief="ridge",
        command=lambda: instructor_info_window.destroy()
    )
    back_to_vs_button.place(x=33, y=555, width=206, height=64)
    back_to_vs_button.bind("<Enter>", on_enter_back_to_vs)
    back_to_vs_button.bind("<Leave>", on_leave_back_to_vs)

    global sled_instruktor_button
    sled_instruktor_button = tk.Button(
        frame,
        image=sled_instruktor_img,
        borderwidth=2,
        relief="ridge",
        command=next_instructor
    )
    sled_instruktor_button.place(x=325, y=555, width=507, height=64)
    sled_instruktor_button.bind("<Enter>", lambda e: sled_instruktor_button.config(image=sled_instruktor_img_dark))
    sled_instruktor_button.bind("<Leave>", lambda e: sled_instruktor_button.config(image=sled_instruktor_img))

    update_instructor_info()

def open_instructor_info_sam():
    open_instructor_info("Самолет", (420, 140))

def open_instructor_info_vert():
    open_instructor_info("Вертолет", (420, 120))

def open_instructor_info_delta():
    open_instructor_info("Дельтаплан", (420, 95))

def open_instructor_info_shar():
    open_instructor_info("Воздушный шар", (420, 100))

def open_instructor_info_par():
    open_instructor_info("Парашют", (420, 110))

def smooth_transition_to_zapis(current_window, additional_window=None):
    # Закрываем текущее окно
    current_window.destroy()

    # Если передано дополнительное окно, закрываем его
    if additional_window:
        additional_window.destroy()

    # Открываем окно "Запись" с задержкой для плавного перехода
    W_main.after(100, open_zapis)

# Словарь с координатами для каждого типа самолета
vehicle_coordinates = {
    "Pilatus PC-12": {
        "name": (500, 40),
        "photo": (33, 180),
        "history": (420, 140),
        "specification": (420, 350),
        "conveniences": (420, 430)
    },
    "Cessna 172": {
        "name": (500, 40),
        "photo": (33, 180),
        "history": (420, 140),
        "specification": (420, 330),
        "conveniences": (420, 410)
    },
    "Ми-8": {
        "name": (500, 40),
        "photo": (33, 180),
        "history": (420, 130),
        "specification": (420, 335),
        "conveniences": (420, 410)
    },
    "Ка-226": {
        "name": (500, 40),
        "photo": (33, 180),
        "history": (420, 130),
        "specification": (420, 323),
        "conveniences": (420, 410)
    },
    "C-15": {
        "name": (500, 40),
        "photo": (33, 180),
        "history": (420, 110),
        "specification": (420, 342),
        "conveniences": (420, 455)
    },
    "Atlas": {
        "name": (500, 40),
        "photo": (33, 180),
        "history": (420, 120),
        "specification": (420, 350),
        "conveniences": (420, 420)
    },
    "Монгольфьер": {
        "name": (500, 40),
        "photo": (33, 180),
        "history": (420, 120),
        "specification": (420, 335),
        "conveniences": (420, 410)
    },
    "Ultramagic M-Series": {
        "name": (500, 40),
        "photo": (33, 180),
        "history": (420, 110),
        "specification": (420, 363),
        "conveniences": (420, 440)
    },
    "Д-1": {
        "name": (500, 40),
        "photo": (33, 180),
        "history": (420, 120),
        "specification": (420, 340),
        "conveniences": (420, 425)
    },
    "PD Sabre": {
        "name": (500, 40),
        "photo": (33, 180),
        "history": (420, 120),
        "specification": (420, 355),
        "conveniences": (420, 425)
    }
}

def open_vehicle_info(vehicle_model):
    global current_vehicle_index
    current_vehicle_index = 0

    vehicle_info_window = tk.Toplevel(W_main)
    vehicle_info_window.title("Информация о воздушном судне")
    vehicle_info_window.geometry("1200x680")
    vehicle_info_window.resizable(False, False)

    frame = tk.Frame(vehicle_info_window)
    frame.place(x=0, y=0, width=1200, height=700)

    background_image_path = "fon_okon.png"
    background_image = Image.open(background_image_path)
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(frame, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0)

    filtered_vehicles = get_vehicle_specifications(vehicle_model)

    if not filtered_vehicles:
        return

    def update_vehicle_info():
        global current_vehicle_index
        selected_vehicle = filtered_vehicles[current_vehicle_index]
        name_label.config(text=f"{selected_vehicle[0]} {selected_vehicle[1]}")
        if selected_vehicle[5]:
            try:
                photo_data = selected_vehicle[5]
                photo = Image.open(io.BytesIO(photo_data))
                photo = photo.resize((370, 246), Image.LANCZOS)
                photo_image = ImageTk.PhotoImage(photo)
                photo_label.config(image=photo_image)
                photo_label.image = photo_image
            except Exception as e:
                print(f"Ошибка при загрузке фото: {e}")
        history_label.config(text=selected_vehicle[2])
        specification_label.config(text=selected_vehicle[3])
        conveniences_label.config(text=selected_vehicle[4])

        # Обновление координат в зависимости от модели самолета
        coords = vehicle_coordinates[selected_vehicle[1]]
        name_label.place(x=coords["name"][0], y=coords["name"][1])
        photo_label.place(x=coords["photo"][0], y=coords["photo"][1])
        history_label.place(x=coords["history"][0], y=coords["history"][1])
        specification_label.place(x=coords["specification"][0], y=coords["specification"][1])
        conveniences_label.place(x=coords["conveniences"][0], y=coords["conveniences"][1])

    def next_vehicle():
        global current_vehicle_index
        current_vehicle_index = (current_vehicle_index + 1) % len(filtered_vehicles)
        frame.after(100, update_vehicle_info)  # задержка перед обновлением информации

    name_font = ("Segoe UI", 18, "bold")
    name_label = tk.Label(
        frame,
        text=f"{filtered_vehicles[0][0]} {filtered_vehicles[0][1]}",
        font=name_font,
        bg="#9AC1CF",
        fg="#FFFFFF"
    )
    name_label.place(x=500, y=40)  # Начальные координаты

    photo_label = tk.Label(frame, bg="#9AC1CF")
    photo_label.place(x=33, y=140)  # Начальные координаты

    description_font = ("Verdana", 14)
    history_label = tk.Label(
        frame,
        text=filtered_vehicles[0][2],
        font=description_font,
        wraplength=750,
        justify=tk.LEFT,
        bg="#9AC1CF",
        fg="#FFFFFF"
    )
    history_label.place(x=400, y=140)  # Начальные координаты

    specification_label = tk.Label(
        frame,
        text=filtered_vehicles[0][3],
        font=description_font,
        wraplength=750,
        justify=tk.LEFT,
        bg="#9AC1CF",
        fg="#FFFFFF"
    )
    specification_label.place(x=400, y=280)  # Начальные координаты

    conveniences_label = tk.Label(
        frame,
        text=filtered_vehicles[0][4],
        font=description_font,
        wraplength=750,
        justify=tk.LEFT,
        bg="#9AC1CF",
        fg="#FFFFFF"
    )
    conveniences_label.place(x=400, y=420)  # Начальные координаты

    global back_to_vs_button
    back_to_vs_button = tk.Button(
        frame,
        image=back_to_vs_img,
        borderwidth=2,
        relief="ridge",
        command=lambda: vehicle_info_window.destroy()
    )
    back_to_vs_button.place(x=33, y=555, width=206, height=64)
    back_to_vs_button.bind("<Enter>", on_enter_back_to_vs)
    back_to_vs_button.bind("<Leave>", on_leave_back_to_vs)

    global sled_vs_button
    sled_vs_button = tk.Button(
        frame,
        image=sled_vs_img,
        borderwidth=2,
        relief="ridge",
        command=next_vehicle
    )
    sled_vs_button.place(x=420, y=555, width=312, height=64)
    sled_vs_button.bind("<Enter>", lambda e: sled_vs_button.config(image=sled_vs_temnee_img))
    sled_vs_button.bind("<Leave>", lambda e: sled_vs_button.config(image=sled_vs_img))

    global zapis_na_polet_button
    zapis_na_polet_button = tk.Button(
        frame,
        image=zapis_na_polet_img,
        borderwidth=2,
        relief="ridge",
        command=lambda: smooth_transition_to_zapis(vehicle_info_window)
    )
    zapis_na_polet_button.place(x=920, y=555, width=232, height=64)
    zapis_na_polet_button.bind("<Enter>", on_enter_zapis_na_polet)
    zapis_na_polet_button.bind("<Leave>", on_leave_zapis_na_polet)

    update_vehicle_info()

def get_vehicle_specifications(vehicle_type):
    conn = sqlite3.connect('uktus_airport.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT Vehicles.VehicleType, Vehicles.VehicleModel, VehicleSpecifications.History, VehicleSpecifications.Specification, VehicleSpecifications.Conveniences, VehicleSpecifications.VehiclePhoto
    FROM VehicleSpecifications
    JOIN Vehicles ON VehicleSpecifications.VehicleID = Vehicles.VehicleID
    WHERE Vehicles.VehicleType = ?
    ''', (vehicle_type.capitalize(),))
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

def open_park_vs():
    global park_vs_window
    park_vs_window = tk.Toplevel(W_main)
    park_vs_window.title("Парк ВС")
    park_vs_window.geometry("1200x700")
    park_vs_window.resizable(False, False)

    background_image_path = "fon_okon.png"
    background_image = Image.open(background_image_path)
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(park_vs_window, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0)

    # Добавление описания
    label_text = tk.Label(
        park_vs_window,
        text="Аэропорт Уктус является многолетним эксплуатантом самых современных воздушных судов.\n Наш парк регулярно обновляется.\n"
             "Вы можете изучить все типы воздушных судов, которые предоставляются в рамках наших услуг,\n"
              "путем перехода на вкладку соответствующего воздушного судна",
        font=("Segoe UI", 18, "bold"),
        bg="#9AC1CF",
        fg="#FFFFFF"
    )
    label_text.place(x=15, y=145)

    # Создание кнопки "Домой"
    home_button = tk.Button(park_vs_window, image=home_img, borderwidth=0, highlightthickness=0, relief="flat", activebackground="#9AC1CF",
                            command=return_park_vs_to_main)
    home_button.image = home_img
    home_button.place(x=1093, y=35)

    # Бинды для кнопки "Домой"
    home_button.bind("<Enter>", lambda e: home_button.config(image=home_temnee_img))
    home_button.bind("<Leave>", lambda e: home_button.config(image=home_img))

    # Создание кнопок для различных типов ВС
    global But_sam, But_vert, But_delta, But_shar, But_par

    But_sam = tk.Button(park_vs_window, image=sam_img, borderwidth=2, relief="ridge", command=lambda: open_vehicle_info("самолет"))
    But_sam.place(x=85, y=340, width=297, height=117)
    But_sam.bind("<Enter>", on_enter_sam)
    But_sam.bind("<Leave>", on_leave_sam)

    But_vert = tk.Button(park_vs_window, image=vert_img, borderwidth=2, relief="ridge", command=lambda: open_vehicle_info("вертолет"))
    But_vert.place(x=440, y=340, width=297, height=117)
    But_vert.bind("<Enter>", on_enter_vert)
    But_vert.bind("<Leave>", on_leave_vert)

    But_delta = tk.Button(park_vs_window, image=delta_img, borderwidth=2, relief="ridge", command=lambda: open_vehicle_info("дельтаплан"))
    But_delta.place(x=800, y=340, width=297, height=117)
    But_delta.bind("<Enter>", on_enter_delta)
    But_delta.bind("<Leave>", on_leave_delta)

    But_shar = tk.Button(park_vs_window, image=shar_img, borderwidth=2, relief="ridge", command=lambda: open_vehicle_info("воздушный шар"))
    But_shar.place(x=250, y=500, width=297, height=117)
    But_shar.bind("<Enter>", on_enter_shar)
    But_shar.bind("<Leave>", on_leave_shar)

    But_par = tk.Button(park_vs_window, image=par_img, borderwidth=2, relief="ridge", command=lambda: open_vehicle_info("парашют"))
    But_par.place(x=600, y=500, width=297, height=117)
    But_par.bind("<Enter>", on_enter_par)
    But_par.bind("<Leave>", on_leave_par)

def open_zapis():
    global zapis_window

    zapis_window = tk.Toplevel(W_main)
    zapis_window.title("Запись")
    zapis_window.geometry("1050x780")
    zapis_window.resizable(False, False)

    background_image_path = "fon_okon_zapis.png"
    background_image = Image.open(background_image_path)
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(zapis_window, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0)

    # Добавление текста сверху окна
    tk.Label(zapis_window, text="Благодарим за доверие к нашему аэропорту и обращаем ваше внимание,\nчто запись на полеты заканчивается за 30 минут до закрытия аэропорта.\nС режимом работы можно ознакомиться на вкладке \"О нас\".",
             font=("Segoe UI", 14),
             bg="#9AC1CF",
             fg="#FFFFFF",
             justify="left",
             ).place(x=263, y=27)

    zapis_window.option_add('*TCombobox*Listbox.font', ('Segoe UI', 13))

    # Создание элементов формы
    tk.Label(zapis_window, text="Заполните информацию о полете",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF"
             ).place(x=70, y=130)

    tk.Label(zapis_window, text="Выберите тип услуги",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF").place(x=120, y=180)
    service_combobox = ttk.Combobox(zapis_window, state="readonly", font=("Segoe UI", 13), width=21)
    service_combobox.place(x=135, y=220)

    tk.Label(zapis_window, text="Выберите модель ВС",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF").place(x=120, y=260)
    vehicle_combobox = ttk.Combobox(zapis_window, state="readonly", font=("Segoe UI", 13), width=21)
    vehicle_combobox.place(x=135, y=300)

    tk.Label(zapis_window, text="Ваш инструктор",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF"
             ).place(x=145, y=340)
    instructor_label = tk.Label(zapis_window, text="", bg="white", width=25, font=("Segoe UI", 11), anchor="w",
                                justify="left")

    instructor_label.place(x=138, y=380)

    tk.Label(zapis_window, text="Дата полета",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF"
             ).place(x=168, y=420)

    # Добавление иконки календаря и календаря для выбора даты
    date_entry = DateEntry(zapis_window, font=("Segoe UI", 13), width=20, date_pattern='yyyy-mm-dd', state='readonly')
    date_entry.place(x=138, y=460)

    tk.Label(zapis_window, text="Время полета",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF"
             ).place(x=162, y=500)

    # Создание Spinbox для выбора времени с 10:00 до 19:00 с шагом в 30 минут
    time_values = [f"{h:02}:{m:02}" for h in range(10, 20) for m in (0, 30)]
    time_var = tk.StringVar(value=time_values[0])
    time_spinbox = ttk.Spinbox(zapis_window, values=time_values, textvariable=time_var, font=("Segoe UI", 13), width=20)
    time_spinbox.place(x=138, y=540)

    tk.Label(zapis_window, text="Продолжительность полета",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF").place(x=90, y=580)

    # Создание Spinbox для выбора продолжительности полета с текстовыми значениями
    duration_values = ["30 минут", "1 час", "1 час 30 минут", "2 часа", "2 часа 30 минут", "3 часа"]
    duration_var = tk.StringVar(value=duration_values[0])
    duration_spinbox = ttk.Spinbox(zapis_window, values=duration_values, textvariable=duration_var, font=("Segoe UI", 13), width=20)
    duration_spinbox.place(x=138, y=620)

    tk.Label(zapis_window, text="Контактные данные",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF"
             ).place(x=660, y=132)

    tk.Label(zapis_window, text="Ваше ФИО",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF"
             ).place(x=705, y=181)
    fio_entry = tk.Entry(zapis_window, font=("Segoe UI", 13), width=30)
    fio_entry.place(x=640, y=223)

    tk.Label(zapis_window, text="Контактный телефон",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF"
             ).place(x=660, y=263)
    phone_entry = tk.Entry(zapis_window, font=("Segoe UI", 13), width=30)
    phone_entry.insert(0, "+7")
    phone_entry.place(x=640, y=303)

    tk.Label(zapis_window, text="Email",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF"
             ).place(x=735, y=341)
    email_entry = tk.Entry(zapis_window, font=("Segoe UI", 13), width=30)
    email_entry.place(x=640, y=381)

    tk.Label(zapis_window, text="Пожелания к бронированию",
             font=("Segoe UI", 17, "bold"),
             bg="#9AC1CF",
             fg="#FFFFFF"
             ).place(x=615, y=419)
    bron_entry = tk.Text(zapis_window, font=("Segoe UI", 13), width=30, height=8)  # width - количество символов, height - количество строк
    bron_entry.place(x=640, y=460)

    # Создание кнопки "ЗАПИСАТЬСЯ"
    global zapisatsa_button
    zapisatsa_button = tk.Button(
        zapis_window,
        image=zapisatsa_img,
        borderwidth=2,
        relief="ridge",
        command=lambda: save_booking(service_combobox.get(), vehicle_combobox.get(), instructor_label.cget("text"), date_entry.get(), time_var.get(), duration_var.get(), fio_entry.get(), phone_entry.get(), email_entry.get(), bron_entry.get("1.0", tk.END).strip(), zapis_window, background_photo)
    )
    zapisatsa_button.place(x=356, y=688, width=263, height=64)
    zapisatsa_button.bind("<Enter>", on_enter_zapisatsa)
    zapisatsa_button.bind("<Leave>", on_leave_zapisatsa)

    # Создание кнопки "Домой"
    home_button = tk.Button(zapis_window, image=home_img, borderwidth=0, highlightthickness=0, relief="flat", activebackground="#9AC1CF",
                            command=return_zapis_main)
    home_button.image = home_img
    home_button.place(x=950, y=35)

    # Бинды для кнопки "Домой"
    home_button.bind("<Enter>", lambda e: home_button.config(image=home_temnee_img))
    home_button.bind("<Leave>", lambda e: home_button.config(image=home_img))

    # Заполнение выпадающих списков
    conn = sqlite3.connect('uktus_airport.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ServiceName FROM Services")
    services = cursor.fetchall()
    service_combobox['values'] = [service[0] for service in services]

    cursor.execute("SELECT VehicleModel FROM Vehicles")
    vehicles = cursor.fetchall()
    vehicle_combobox['values'] = [vehicle[0] for vehicle in vehicles]

    conn.close()

    # Функция для обновления инструктора на основе выбранных значений
    def update_instructor():
        selected_service = service_combobox.get()
        selected_vehicle = vehicle_combobox.get()
        if selected_service and selected_vehicle:
            conn = sqlite3.connect('uktus_airport.db')
            cursor = conn.cursor()
            cursor.execute("""
            SELECT i.FirstName, i.LastName
            FROM Instructors i
            JOIN Vehicles v ON i.InstructorID = v.InstructorID
            JOIN VehicleServices vs ON v.VehicleID = vs.VehicleID
            JOIN Services s ON vs.ServiceID = s.ServiceID
            WHERE s.ServiceName = ? AND v.VehicleModel = ?
            """, (selected_service, selected_vehicle))
            instructor = cursor.fetchone()
            conn.close()
            if instructor:
                instructor_label.config(text=f"{instructor[0]} {instructor[1]}")
                print(f"Instructor found: {instructor[0]} {instructor[1]}")
            else:
                instructor_label.config(text="")
                print(f"No instructor found for service: {selected_service}, vehicle: {selected_vehicle}")

    # Функция для обновления списка типов ВС на основе выбранного типа услуги
    def update_vehicle_combobox(event):
        selected_service = service_combobox.get()
        if selected_service:
            conn = sqlite3.connect('uktus_airport.db')
            cursor = conn.cursor()
            if selected_service == "полет на самолете":
                cursor.execute("SELECT VehicleModel FROM Vehicles WHERE VehicleModel IN ('Pilatus PC-12', 'Cessna 172')")
            elif selected_service == "полет на вертолете":
                cursor.execute("SELECT VehicleModel FROM Vehicles WHERE VehicleModel IN ('Ми-8', 'Ка-226')")
            elif selected_service == "полет на дельтаплане":
                cursor.execute("SELECT VehicleModel FROM Vehicles WHERE VehicleModel IN ('C-15', 'Atlas')")
            elif selected_service == "полет на воздушном шаре":
                cursor.execute("SELECT VehicleModel FROM Vehicles WHERE VehicleModel IN ('Монгольфьер', 'Ultramagic M-Series')")
            elif selected_service == "прыжок с парашютом":
                cursor.execute("SELECT VehicleModel FROM Vehicles WHERE VehicleModel IN ('Д-1', 'PD Sabre')")
            else:
                cursor.execute("SELECT VehicleModel FROM Vehicles")
            vehicles = cursor.fetchall()
            conn.close()
            vehicle_combobox['values'] = [vehicle[0] for vehicle in vehicles]
            vehicle_combobox.set('')  # Очистка выбранного значения

    # Привязка функции обновления инструктора к изменению значений в выпадающих списках
    service_combobox.bind("<<ComboboxSelected>>", update_vehicle_combobox)
    vehicle_combobox.bind("<<ComboboxSelected>>", lambda e: update_instructor())

    def validate_data(service, vehicle, date, time, duration, fio, phone, email, parent):
        if not service:
            messagebox.showerror("Ошибка", "Пожалуйста, выберите тип услуги", parent=parent)
            return False
        if not vehicle:
            messagebox.showerror("Ошибка", "Пожалуйста, выберите модель воздушного судна", parent=parent)
            return False
        if not date:
            messagebox.showerror("Ошибка", "Пожалуйста, выберите дату полета", parent=parent)
            return False
        if datetime.strptime(date, '%Y-%m-%d').date() < datetime.now().date():
            messagebox.showerror("Ошибка", "Пожалуйста, выберите корректную дату", parent=parent)
            return False
        if not time:
            messagebox.showerror("Ошибка", "Пожалуйста, укажите время полета", parent=parent)
            return False
        if not duration:
            messagebox.showerror("Ошибка", "Пожалуйста, укажите продолжительность полета", parent=parent)
            return False
        if not fio:
            messagebox.showerror("Ошибка", "Пожалуйста, введите ваше ФИО", parent=parent)
            return False
        if not re.match(r"^[а-яА-ЯёЁ\s]+$", fio):
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректное ФИО", parent=parent)
            return False
        if len(fio.split()) < 3:
            messagebox.showerror("Ошибка", "Пожалуйста, введите вашу фамилию, имя и отчество", parent=parent)
            return False
        if not phone:
            messagebox.showerror("Ошибка", "Пожалуйста, введите номер телефона", parent=parent)
            return False
        if not re.match(r"^\+7\d{10}$", phone):
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректный номер телефона", parent=parent)
            return False
        if not email:
            messagebox.showerror("Ошибка", "Пожалуйста, укажите вашу электронную почту", parent=parent)
            return False
        if re.match(r"^\d+$", email) or not re.match(r"^[а-яА-ЯёЁa-zA-Z0-9]+@[а-яА-ЯёЁa-zA-Z]+\.(ru|com)$", email):
            messagebox.showerror("Ошибка", "Некорректный формат email", parent=parent)
            return False
        return True

    def save_booking(service, vehicle, instructor_name, date, time, duration, fio, phone, email, wishes, zapis_window, background_photo):
        if not validate_data(service, vehicle, date, time, duration, fio, phone, email, zapis_window):
            return

        # Сохранение данных в базу данных
        conn = sqlite3.connect('uktus_airport.db')
        cursor = conn.cursor()

        # Получение BookingID
        cursor.execute("SELECT MAX(BookingID) FROM ServiceBookings")
        booking_id = cursor.fetchone()[0]
        if booking_id is None:
            booking_id = 1
        else:
            booking_id += 1

        # Получение CustomerID
        cursor.execute("SELECT MAX(CustomerID) FROM Customers")
        customer_id = cursor.fetchone()[0]
        if customer_id is None:
            customer_id = 1
        else:
            customer_id += 1

        # Разбор ФИО
        fio_parts = fio.split()
        last_name = fio_parts[0]
        first_name = fio_parts[1]
        patronymic = fio_parts[2] if len(fio_parts) > 2 else ""

        # Вставка данных в таблицу Customers
        cursor.execute("""
        INSERT INTO Customers (CustomerID, LastName, FirstName, Patronymic, PhoneNumber, Email)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (customer_id, last_name, first_name, patronymic, phone, email))

        # Получение ServiceID на основе выбранной услуги
        cursor.execute("SELECT ServiceID FROM Services WHERE ServiceName = ?", (service,))
        service_id = cursor.fetchone()[0]

        # Получение InstructorID на основе имени инструктора
        instructor_name_parts = instructor_name.split()
        cursor.execute("""
        SELECT InstructorID
        FROM Instructors
        WHERE FirstName = ? AND LastName = ?
        """, (instructor_name_parts[0], instructor_name_parts[1]))
        instructor_id = cursor.fetchone()[0]

        # Вставка данных в таблицу ServiceBookings
        cursor.execute("""
        INSERT INTO ServiceBookings (BookingID, CustomerID, ServiceID, InstructorID, BookingDate, StartTime, Duration, Wishes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (booking_id, customer_id, service_id, instructor_id, date, time, duration, wishes))

        # Получение данных инструктора
        cursor.execute("""
        SELECT FirstName, LastName, PhoneNumber, Email
        FROM Instructors
        WHERE InstructorID = ?
        """, (instructor_id,))
        instructor_data = cursor.fetchone()

        # Получение типа воздушного судна
        cursor.execute("""
        SELECT VehicleType
        FROM Vehicles
        WHERE VehicleModel = ?
        """, (vehicle,))
        vehicle_type = cursor.fetchone()[0]

        # Получение стоимости услуги
        cursor.execute("""
        SELECT Price
        FROM Services
        WHERE ServiceID = ?
        """, (service_id,))
        service_price = cursor.fetchone()[0]

        conn.commit()
        conn.close()

        # Очистка всех полей ввода и кнопки "Запись"
        for widget in zapis_window.winfo_children():
            widget.destroy()

        # Пересоздание метки с фоном
        background_label = tk.Label(zapis_window, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0)

        # Создание кнопки "Домой"
        home_button = tk.Button(zapis_window, image=home_img, borderwidth=0, highlightthickness=0, relief="flat", activebackground="#9AC1CF",
                                command=return_zapis_main)
        home_button.image = home_img
        home_button.place(x=950, y=35)

        # Бинды для кнопки "Домой"
        home_button.bind("<Enter>", lambda e: home_button.config(image=home_temnee_img))
        home_button.bind("<Leave>", lambda e: home_button.config(image=home_img))

        # Отображение сообщения об успешной записи
        success_message = tk.Label(zapis_window, text=f"Поздравляем с успешной записью на полет на {vehicle_type}!\n"
                                                       f"Стоимость полета: {service_price} руб.\n\n"
                                                       f"С нетерпением будем ждать вас в аэропорту по адресу:\nтерритория аэропорт Уктус, здание 1.\n"
                                                       f"Дата и время полета: {date}, {time}\n\n"
                                                       f"Пожалуйста, прибудьте в аэропорт своевременно,\nза 30 минут до назначенного времени полета.\n "
                                                       f"Инструктору необходимо познакомиться с вами и\nпровести предполетный инструктаж.\n\n"
                                                       f"Ваш инструктор: {instructor_name}\n"
                                                       f"Номер телефона инструктора: {instructor_data[2]}\n"
                                                       f"Электронная почта инструктора: {instructor_data[3]}",
                                   font=("Segoe UI", 17), bg="#9AC1CF", fg="#FFFFFF")
        success_message.place(x=210, y=200)

        # Поднятие окна "Запись" на передний план
        zapis_window.attributes("-topmost", True)
        zapis_window.attributes("-topmost", False)

def get_airport_info():
    conn = sqlite3.connect('uktus_airport.db')
    cursor = conn.cursor()
    cursor.execute("SELECT InfoText, Website, Address, Phone, Email, OperatingMode FROM AirportInfo")
    result = cursor.fetchone()
    conn.close()

    if result:
        return result
    else:
        return None

def open_o_nas_window():
    global o_nas_window
    o_nas_window = tk.Toplevel(W_main)
    o_nas_window.title("О нас")
    o_nas_window.geometry("1200x770")
    o_nas_window.resizable(False, False)

    # Загрузка фона
    background_image_path = "fon_okon_o_nas.png"
    background_image = Image.open(background_image_path)
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(o_nas_window, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0)

    map_widget = tkintermapview.TkinterMapView(o_nas_window, width=1128, height=460, corner_radius=0)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    map_widget.place(x=35, y=133)
    map_widget.set_position(56.6989944, 60.7781077)  # Аэропорт Уктус
    map_widget.set_zoom(14)
    marker_1 = map_widget.set_position(56.6989944, 60.7781077, marker=True)
    marker_1.set_text("АЭРОПОРТ УКТУС")

    # Получаем информацию из базы данных
    airport_info = get_airport_info()
    if airport_info:  # если информация существует
        info_text = airport_info[0]
        site = airport_info[1]
        address = airport_info[2]
        phone = airport_info[3]
        email = airport_info[4]
        operating_mode = airport_info[5]

        info_label = tk.Label(o_nas_window, text=info_text, wraplength=810, bg="#9AC1CF", fg="#FFFFFF", anchor="w", font=('Segoe UI', 14), justify="left")
        info_label.place(x=260, y=14, width=900)

        site_label = tk.Label(o_nas_window, text=f"{site}", bg="#9AC1CF", fg="blue", cursor="hand2", font=('Segoe UI', 14))
        site_label.place(x=30, y=605)

        def open_site(event):
            webbrowser.open(site)  # открываем сайт в браузере

        site_label.bind("<Button-1>", open_site)  # связываем клик с функцией открытия сайта

        phone_label = tk.Label(o_nas_window, text=f"{phone}", bg="#9AC1CF", fg="#FFFFFF", font=('Segoe UI', 14))
        phone_label.place(x=30, y=635)

        email_label = tk.Label(o_nas_window, text=f"{email}", bg="#9AC1CF", fg="#FFFFFF", font=('Segoe UI', 14))
        email_label.place(x=30, y=665)

        address_label = tk.Label(o_nas_window, text=f"{address}", wraplength=1000, bg="#9AC1CF", fg="#FFFFFF", font=('Segoe UI', 14))
        address_label.place(x=30, y=695)

        operating_mode_label = tk.Label(o_nas_window, text=f"Режим работы: {operating_mode}", bg="#9AC1CF", fg="#FFFFFF", font=('Segoe UI', 14))
        operating_mode_label.place(x=30, y=725)

    else:
        messagebox.showerror("Ошибка", "Не удалось получить информацию о аэропорте.")

    # Создание кнопки "Домой"
    home_button = tk.Button(o_nas_window, image=home_img, borderwidth=0, highlightthickness=0, relief="flat", activebackground="#9AC1CF",
                            command=return_o_nas_to_main)
    home_button.image = home_img
    home_button.place(x=1093, y=35)

    # Бинды для кнопки "Домой"
    home_button.bind("<Enter>", lambda e: home_button.config(image=home_temnee_img))
    home_button.bind("<Leave>", lambda e: home_button.config(image=home_img))

But1 = tk.Button(W_main, image=o_nas_img, borderwidth=0, activebackground='white', command=open_o_nas_window)
But1.place(x=2, y=2, width=247, height=118)
But1.bind("<Enter>", on_enter_o_nas)
But1.bind("<Leave>", on_leave_o_nas)

But2 = tk.Button(W_main, image=park_vs_img, borderwidth=0, activebackground='white', command=open_park_vs)
But2.place(x=248, y=2, width=285, height=118)
But2.bind("<Enter>", on_enter_park_vs)
But2.bind("<Leave>", on_leave_park_vs)

But3 = tk.Button(W_main, image=zapis_img, borderwidth=0, activebackground='white', command=open_zapis)
But3.place(x=530, y=2, width=249, height=118)
But3.bind("<Enter>", on_enter_zapis)
But3.bind("<Leave>", on_leave_zapis)

But4 = tk.Button(W_main, image=instruktory_img, borderwidth=0, activebackground='white', command=open_instruktory)
But4.place(x=783, y=2, width=418, height=118)
But4.bind("<Enter>", on_enter_instruktory)
But4.bind("<Leave>", on_leave_instruktory)

vk_button = tk.Button(W_main, image=vk_img, borderwidth=0, activebackground='white', command=open_vk)
vk_button.place(x=520, y=650, width=50, height=50)
vk_button.bind("<Enter>", on_enter_vk)
vk_button.bind("<Leave>", on_leave_vk)

youtube_button = tk.Button(W_main, image=youtube_img, borderwidth=0, activebackground='white', command=open_youtube)
youtube_button.place(x=610, y=650, width=70, height=50)
youtube_button.bind("<Enter>", on_enter_youtube)
youtube_button.bind("<Leave>", on_leave_youtube)

def return_instructory_to_main():
    instruktory_window.destroy()
    W_main.deiconify()

def return_o_nas_to_main():
    o_nas_window.destroy()
    W_main.deiconify()

def return_park_vs_to_main():
    park_vs_window.destroy()
    W_main.deiconify()

def return_zapis_main():
    zapis_window.destroy()
    W_main.deiconify()

W_main.mainloop()