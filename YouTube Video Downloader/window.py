from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox
from tkinter import Button, Entry, Label, PhotoImage

def Browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_path.set(download_directory)

def Download():
    Youtube_link = video_link.get()

    download_folder = download_path.get()

    getVideo = YouTube(Youtube_link)

    
    for stream in getVideo.streams:  
        print(stream)

    if output.get() == "audio":
        videoStream = getVideo.streams.filter(mime_type="audio/mp4").first()
    elif output.get() == "3gp":
            videoStream = getVideo.streams.filter(mime_type="video/3gpp", res=quality.get()).first()
    else:
        videoStream = getVideo.streams.filter(res=quality.get()).first()
    
    try:
        videoStream.download(download_folder)
    except:
        messagebox.showinfo("ERROR MESSAGE", "FORMAT NOT AVAILABLE :) TRY AGAIN")
        return

    messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN \n" + download_folder)


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#ffffff")
window.title("YT Video Downloader")
image_icon = PhotoImage(file="youtube_logo.png")
window.iconphoto(False, image_icon)

download_path = StringVar()
video_link = StringVar()

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    494.0, 210.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    542.0, 245.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0,
    textvariable=video_link)

entry0.place(
    x = 357.0, y = 225,
    width = 370.0,
    height = 38)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    542.0, 366.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0,
    textvariable=download_path)

entry1.place(
    x = 357.0, y = 346,
    width = 370.0,
    height = 38)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Browse,
    relief = "flat")

b0.place(
    x = 806, y = 341,
    width = 151,
    height = 52)

img1 = PhotoImage(file = f"img1.png")

global quality
quality = StringVar()
quality.set("720p")
b1 = OptionMenu(window, quality, "720p", "480p", "360p", "240p", "144p")
b1.place(x=780, y=228)
b1.config(bg="#D9D9D9", fg="BLACK", activebackground="#D9D9D9", activeforeground="BLACK", font="Swansea")
b1["menu"].config(bg="#D9D9D9", fg="BLACK", activebackground="#989898", activeforeground="BLACK", font="Swansea")

global output
output = StringVar()
output.set("mp4")
b2 = OptionMenu(window, output, "mp4", "audio", "3gp")
b2.place(x=886, y=228)
b2.config(bg="#D9D9D9", fg="BLACK", activebackground="#D9D9D9", activeforeground="BLACK", font="Swansea")
b2["menu"].config(bg="#D9D9D9", fg="BLACK", activebackground="#989898", activeforeground="BLACK", font="Swansea")

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = Download, 
    relief = "flat")

b5.place(
    x = 381, y = 467,
    width = 321,
    height = 66)

window.resizable(False, False)
window.mainloop()
