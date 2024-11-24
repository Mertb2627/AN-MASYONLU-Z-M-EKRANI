#Bu kod Mert Bülbül (220502006) tarafından hazırlanmıştır


import tkinter as tk
import random

#Uygulama Çerçevesi
root = tk.Tk()
root.title("Ball Animation")
root.geometry("800x600")

#Topların animasyonunun olucağı bölüm
canvas = tk.Canvas(root, width=800, height=500, bg="lightgrey")
canvas.pack()

#Renk ve Boyut değişkenleri
Seçili_Renk = None
Seçili_Boyut = None

#Toplar için bir sınıf
class Ball:
    def __init__(self, canvas, x, y, size, color, dx, dy):
        self.canvas = canvas
        self.size = size
        self.color = color
        self.dx = dx
        self.dy = dy
        self.id = canvas.create_oval(x, y, x + size, y + size, fill=color)

    def move(self):
        coords = self.canvas.coords(self.id)
        #Kenarlara geldiğinde çarpışmasını sağlama
        if coords[0] + self.dx <= 0 or coords[2] + self.dx >= 800:
            self.dx = -self.dx
        if coords[1] + self.dy <= 0 or coords[3] + self.dy >= 500:
            self.dy = -self.dy
        self.canvas.move(self.id, self.dx, self.dy)

#Toplarında birbirine çarpmasını sağlayan kısım
def çarpışma():
    for i in range(len(toplar)):
        for j in range(i + 1, len(toplar)):
            top1 = toplar[i]
            top2 = toplar[j]
            kordinat_1 = canvas.coords(top1.id)
            kordinat_2 = canvas.coords(top2.id)
            mesafe = ((kordinat_1[0] + top1.size / 2 - (kordinat_2[0] + top2.size / 2))**2 +
                        (kordinat_1[1] + top1.size / 2 - (kordinat_2[1] + top2.size / 2))**2)**0.5
            if mesafe < (top1.size + top2.size) / 2:
                top1.dx, top2.dx = -top1.dx, -top2.dx
                top1.dy, top2.dy = -top1.dy, -top2.dy

#Topların listesini tutar ve uyguluma durumu
toplar = []
animation_running = False
speed_multiplier = 1

#Başlat
def start_animation():
    global animation_running
    if not animation_running:
        animation_running = True
        animate()

def animate():
    for ball in toplar:
        ball.move()
    çarpışma()
    if animation_running:
        root.after(int(20 / speed_multiplier), animate)

#Durdur
def stop_animation():
    global animation_running
    animation_running = False

#Resetle
def reset_canvas():
    global toplar, animation_running
    animation_running = False
    for ball in toplar:
        canvas.delete(ball.id)
    toplar = []

#Renk seçimi
def select_color(color):
    global Seçili_Renk
    Seçili_Renk = color

#Boyut seçimi
def select_size(size):
    global Seçili_Boyut
    Seçili_Boyut = size

#Top ekleme
def add_selected_ball():
    if Seçili_Renk and Seçili_Boyut:
        x = random.randint(0, 800 - Seçili_Boyut)
        y = random.randint(0, 500 - Seçili_Boyut)
        dx = random.choice([-3, 3])
        dy = random.choice([-3, 3])
        ball = Ball(canvas, x, y, Seçili_Boyut, Seçili_Renk, dx, dy)
        toplar.append(ball)
    else:
        print("Lütfen renk ve boyut seçin!")

#Hızı değiştirme
def change_speed(amount):
    global speed_multiplier
    speed_multiplier = max(1, speed_multiplier + amount)
    print(f"Hız: {speed_multiplier}")

#Arayüz
control_frame = tk.Frame(root)
control_frame.pack()

#Renkler için buton
colors = ["red", "blue", "yellow", "green", "purple", "orange", "pink"]
color_frame = tk.Frame(control_frame)
color_frame.grid(row=0, column=0, padx=10)

tk.Label(color_frame, text="Renk Seç:").pack()
for color in colors:
    tk.Button(color_frame, bg=color, width=2, command=lambda c=color: select_color(c)).pack(side=tk.LEFT)

#Boyutlar için buton
sizes = [20, 40, 60]
size_frame = tk.Frame(control_frame)
size_frame.grid(row=0, column=1, padx=10)

tk.Label(size_frame, text="Boyut Seç:").pack()
for size in sizes:
    tk.Button(size_frame, text=str(size), command=lambda s=size: select_size(s)).pack(side=tk.LEFT)

#Butonlar
button_frame = tk.Frame(control_frame)
button_frame.grid(row=0, column=2, padx=10)

start_button = tk.Button(button_frame, text="START", command=start_animation)
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(button_frame, text="STOP", command=stop_animation)
stop_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(button_frame, text="RESET", command=reset_canvas)
reset_button.pack(side=tk.LEFT, padx=5)

add_ball_button = tk.Button(button_frame, text="Add Ball", command=add_selected_ball)
add_ball_button.pack(side=tk.LEFT, padx=5)

speed_up_button = tk.Button(button_frame, text="Speed Up", command=lambda: change_speed(1))
speed_up_button.pack(side=tk.LEFT, padx=5)

speed_down_button = tk.Button(button_frame, text="Speed Down", command=lambda: change_speed(-1))
speed_down_button.pack(side=tk.LEFT, padx=5)


root.mainloop()
