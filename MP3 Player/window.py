from email.mime import image
from tkinter import *
from tkinter import filedialog
import tkinter
from turtle import bgcolor, width
import pygame
import time
from mutagen.mp3 import MP3
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import eyed3, io

def btn_clicked():
    print("Button Clicked")

def add_songs():
    songs = filedialog.askopenfilenames(initialdir="D:/Projects/D:UniCompiler/mp3 player/songs", title="Choose a Song", filetypes=(("mp3 files", "*.mp3"), ))
    for song in songs:
        song = song.replace("D:/Projects/UniCompiler/mp3 player/songs/", "")
        song = song.replace(".mp3", "")
        song_box.insert(END, song)

def delete_songs():
    stop()
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

def play():
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = f"D:/Projects/UniCompiler/mp3 player/songs/{song}.mp3"
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    play_time()

    # slider_position = int(song_length)
    # my_slider.config(to=slider_position, value=0)


global stopped
stopped = False

def stop():
    status_bar.config(text="")
    my_slider.config(value=0)
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    status_bar.config(text="")

    global stopped
    stopped = True

def play_time():

    if stopped:
        return
    current_time = pygame.mixer.music.get_pos() / 1000
    #slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}')
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    current_song = song_box.curselection()
    song = song_box.get(ACTIVE)

    song = f"D:/Projects/UniCompiler/mp3 player/songs/{song}.mp3"

    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length

    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    current_time += 1

    if int(my_slider.get() == int(song_length)):
        status_bar.config(text = f"Time Elapsed: {converted_song_length}")

    elif paused:
        pass

    elif int(my_slider.get()) == int(current_time):
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))

    else:
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))     
        converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))   
        status_bar.config(text = f"Time Elapsed: {converted_current_time}  of  {converted_song_length}")
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)

    # my_slider.config(value=int(current_time))

    #slider_position = int(song_length)
    #my_slider.config(to=slider_position, value=int(current_time))

    status_bar.after(1000, play_time)

def slide(x):
    # slider_label.config(text=f"{int(my_slider.get())} of {int(song_length)}")
    song = song_box.get(ACTIVE)
    song = f"D:/Projects/UniCompiler/mp3 player/songs/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

global paused
paused = False

def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    
    else:
        pygame.mixer.music.pause()
        paused = True

def next_song():

    status_bar.config(text="")
    my_slider.config(value=0)

    next_one = song_box.curselection()
    next_one = next_one[0] + 1
    song = song_box.get(next_one)

    song = f"D:/Projects/UniCompiler/mp3 player/songs/{song}.mp3"
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)

    song_box.activate(next_one)

    song_box.selection_set(next_one, last=None)

def previous_song():

    status_bar.config(text="")
    my_slider.config(value=0)
    
    next_one = song_box.curselection()
    next_one = next_one[0] - 1
    song = song_box.get(next_one)

    song = f"D:/Projects/UniCompiler/mp3 player/songs/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)

    song_box.activate(next_one)

    song_box.selection_set(next_one, last=None)

global window
window = Tk()
pygame.mixer.init()

window.geometry("1200x780")
window.configure(bg = "#f7ecde")
canvas = Canvas(
    window,
    bg = "#f7ecde",
    height = 780,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = previous_song,
    relief = "flat")

b0.place(
    x = 361, y = 667,
    width = 71,
    height = 71)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
   600.0, 318.5,
   image=background_img)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 1045, y = 666,
    width = 75,
    height = 72)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = play,
    relief = "flat")

b2.place(
    x = 620, y = 665,
    width = 87,
    height = 84)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = delete_songs,
    relief = "flat")

b3.place(
    x = 163, y = 0,
    width = 195,
    height = 34)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = add_songs,
    relief = "flat")

b4.place(
    x = 1, y = 0,
    width = 162,
    height = 34)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: pause(paused),
    relief = "flat")

b5.place(
    x = 707, y = 658,
    width = 85,
    height = 91)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = stop,
    relief = "flat")

b6.place(
    x = 792, y = 665,
    width = 86,
    height = 84)

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = next_song,
    relief = "flat")

b7.place(
    x = 478, y = 668,
    width = 71,
    height = 71)

song_box = Listbox(window, bg = "#F7ECDE", fg = "black", width = 60, selectbackground="#343A69", font="Inter")
song_box.place(
    x=803.0, y=86,
    width=359.0,
    height=408
)

status_bar = Label(window, text="", bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 2)

my_slider = ttk.Scale(window, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=800, style="slider.Horizontal.TScale")
my_slider.place(
    x=200.0, y=637
    #length=800
)

s=ttk.Style()
volume_slider = ttk.Scale(window, from_=1, to=0, orient=VERTICAL, value=1, command=volume, length=125, style='slider.Vertical.TScale')
volume_slider.place(
    x=1065.0, y=550
    #length=800
)

s.configure('slider.Vertical.TScale', background='#E4FBFF', foreground="maroon")
s.configure('slider.Horizontal.TScale', background='#E4FBFF', foreground="maroon")

#my_slider.pack(pady=20)

# slider_label = Label(window, text="0")
# slider_label.place(
#     x=200, y=650
# )

# song_image = PhotoImage(file = f'バキ - バキBGM(0).jpg')
# coolimage = Label(
#     image = song_image,
#     borderwidth = 0,
#     highlightthickness = 0,
#     relief = "flat")
# coolimage.place(x=0,y=34, width=762, height=530)

window.resizable(False, False)
window.mainloop()
