from tkinter import *
import webbrowser


def profileWindow():
    global profile_img
    pWindow = Toplevel()
    pWindow.title("Tentang Pengembang")
    pWindow.geometry("500x300")
    # pWindow.minsize(500, 500)
    # pWindow.maxsize(500, 500)

    # imageFrame = Frame(pWindow)
    # imageFrame.pack()
    # mask = Image.open("assets/mask.png").convert("L")
    # mask = mask.resize((170, 170), Image.ANTIALIAS)

    # image = Image.open("assets/profile/profile-edited.jpeg")
    # image = image.resize((170, 170), Image.ANTIALIAS)
    # image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    # image.putalpha(mask)

    # profile_img = ImageTk.PhotoImage(image)
    # profile_label = Label(imageFrame, image=profile_img).pack(pady=20)

    title = Label(
        pWindow, text="Tentang Aplikasi Image Captioning")
    name = Label(pWindow, text="Author: Dzikri Syafi Auliya")
    email = Label(pWindow, text="dzikriauliya@gmail.com")
    title.configure(font=('Segoe UI', 16, 'bold'))
    name.configure(font=('Segoe UI', 12))
    email.configure(font=('Segoe UI', 12), foreground="#707070")

    title.pack()
    name.pack()
    email.pack()

    dFrame = LabelFrame(pWindow, text='Deskripsi Aplikasi', padx=5, pady=5)
    dFrame.pack(padx=5, pady=10)
    desc = Label(dFrame, text="Aplikasi image captioning merupakan aplikasi untuk mengha-\nsilkan keterangan pada gambar secara automatis. Pada\naplikasi ini terdapat 4 model image captioning yang\ndapat digunakan untuk melakukan proses pendeskripsian.", anchor="e", justify=LEFT)
    desc.configure(font=('arial', 12))
    desc.pack()

    smFrame = LabelFrame(pWindow, padx=145, pady=10)
    smFrame.pack()
    github = Button(smFrame, text="Github", command=lambda: openUrl(
        "https://github.com/dzikrisyafi/"))
    github.configure(
        background='#364156',
        foreground='white',
        font=('Segoe UI', 10, 'bold')
    )
    github.grid(row=0, column=0, padx=5)
    ig = Button(smFrame, text="Instagram", command=lambda: openUrl(
        "https://instagram.com/dzikrisyafi/"))
    ig.configure(
        background='#364156',
        foreground='white',
        font=('Segoe UI', 10, 'bold')
    )
    ig.grid(row=0, column=1, padx=5)


def openUrl(url):
    webbrowser.open(url, new=1)
