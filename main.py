import tkinter as tk

import tensorflow as tf
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import os

from views.profile import profileWindow
from views.help import helpWindow
from utils.preprocess import extract_feature
from utils.search import *
from utils.evaluate import evaluate
from tensorflow.keras.models import load_model
from pickle import load

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)

root = tk.Tk()
root.geometry("1000x720")
root.minsize(1000, 720)
root.maxsize(1000, 720)
root.title("Image Caption Generator")
root.configure(background="#F0F0F0")


def classify(file_path, tokenizer, model, model_type):
    global label_packed

    tokenizer = load(open(tokenizer, "rb"))
    max_length = 34
    model = load_model(model)

    base = os.path.basename(file_path)
    key = os.path.splitext(base)[0]

    image = extract_feature(file_path, model_type)
    greedy = greedy_search(model, tokenizer, image, max_length)
    print(greedy)
    tgreedy.delete('1.0', END)
    tgreedy.insert(END, chars=greedy)

    bleu1, bleu2, bleu3, bleu4 = evaluate(greedy, key)
    tgreedy_bleu1.delete('1.0', END)
    tgreedy_bleu2.delete('1.0', END)
    tgreedy_bleu3.delete('1.0', END)
    tgreedy_bleu4.delete('1.0', END)
    tgreedy_bleu1.insert(END, chars=bleu1)
    tgreedy_bleu2.insert(END, chars=bleu2)
    tgreedy_bleu3.insert(END, chars=bleu3)
    tgreedy_bleu4.insert(END, chars=bleu4)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded = uploaded.resize((635, 510), Image.ANTIALIAS)
        im = ImageTk.PhotoImage(uploaded)
        image_pack.configure(image=im)
        image_pack.image = im

        proses1.configure(
            state=NORMAL, command=lambda: classify(file_path,
                                                   "./models/tokenizer/tokenizer.pkl",
                                                   "./models/h5/model1-ep003-loss3.462-val_loss3.782.h5",
                                                   "vgg16"))
        proses2.configure(
            state=NORMAL, command=lambda: classify(file_path,
                                                   "./models/tokenizer/tokenizer.pkl",
                                                   "./models/h5/model2-ep003-loss3.306-val_loss3.649.h5",
                                                   "inceptionv3"))
        proses3.configure(
            state=NORMAL, command=lambda: classify(file_path,
                                                   "./models/tokenizer/tokenizer.pkl",
                                                   "./models/h5/model3-ep003-loss3.276-val_loss3.670.h5",
                                                   "vgg16"))
        proses4.configure(
            state=NORMAL, command=lambda: classify(file_path,
                                                   "./models/tokenizer/tokenizer.pkl",
                                                   "./models/h5/model4-ep003-loss3.135-val_loss3.483.h5",
                                                   "inceptionv3"))
    except:
        pass


mToolsFrame = Frame(root, padx=40, pady=155)
mToolsFrame.configure(background="#FAFAFA")
mToolsFrame.grid(row=0, column=0, padx=5, pady=5, rowspan=4)

# Mendefinisikan button pada frame management tools
proses1 = Button(mToolsFrame, text="Proses Menggunakan Model 1",
                 width=25, state=DISABLED)
proses2 = Button(mToolsFrame, text="Proses Menggunakan Model 2",
                 width=25, state=DISABLED)
proses3 = Button(mToolsFrame, text="Proses Menggunakan Model 3",
                 width=25, state=DISABLED)
proses4 = Button(mToolsFrame, text="Proses Menggunakan Model 4",
                 width=25, state=DISABLED)
upload = Button(mToolsFrame, text="Masukkan Gambar",
                width=25, command=upload_image)
help = Button(mToolsFrame, text="Cara Penggunaan",
              width=25, command=helpWindow)

profile = Button(mToolsFrame, text="Tentang Aplikasi",
                 width=25, command=profileWindow)

# Mengubah tampilan pada button frame management tools
proses1.configure(
    background='#364156',
    foreground='white',
    font=('arial', 12, 'bold'),
)
proses2.configure(
    background='#364156',
    foreground='white',
    font=('arial', 12, 'bold')
)
proses3.configure(
    background='#364156',
    foreground='white',
    font=('arial', 12, 'bold')
)
proses4.configure(
    background='#364156',
    foreground='white',
    font=('arial', 12, 'bold')
)
upload.configure(
    background='#364156',
    foreground='white',
    font=('arial', 12, 'bold')
)
help.configure(
    background='#364156',
    foreground='white',
    font=('arial', 12, 'bold')
)
profile.configure(
    background='#364156',
    foreground='white',
    font=('arial', 12, 'bold')
)


proses1.pack(pady=12)
proses2.pack(pady=12)
proses3.pack(pady=12)
proses4.pack(pady=12)
upload.pack(pady=12)
help.pack(pady=12)
profile.pack(pady=12)

imageFrame = Frame(root, width=635, height=510, pady=15)

imageFrame.grid(row=0, column=1, pady=5)

imageFrame.configure(background="#000000")

image = Image.open("assets/thumbnail/default.png")
image = image.resize((635, 510), Image.ANTIALIAS)
photoimage = ImageTk.PhotoImage(image)
image_pack = Label(imageFrame, image=photoimage)
image_pack.pack(side=TOP)

outputFrame = LabelFrame(root, text="Hasil Prediksi", padx=3, pady=25)
outputFrame.configure(background="#F0F0F0", font=('Segoe UI', 14, 'bold'))
outputFrame.grid(row=1, column=1, padx=3)

greedy = Label(outputFrame, text="Deskripsi", pady=1, justify=LEFT)
greedy_bleu = Label(outputFrame, text="BLEU Score", pady=5, justify=LEFT)

tgreedy = Text(outputFrame, height=1, width=57, pady=5)
tgreedy_bleu1 = Text(outputFrame, height=1, width=13, pady=5)
tgreedy_bleu2 = Text(outputFrame, height=1, width=13, pady=5)
tgreedy_bleu3 = Text(outputFrame, height=1, width=13, pady=5)
tgreedy_bleu4 = Text(outputFrame, height=1, width=13, pady=5)

greedy.configure(font=('arial', 12))
greedy_bleu.configure(font=('arial', 12))
tgreedy.configure(font=('arial', 12))
tgreedy_bleu1.configure(font=('arial', 12))
tgreedy_bleu2.configure(font=('arial', 12))
tgreedy_bleu3.configure(font=('arial', 12))
tgreedy_bleu4.configure(font=('arial', 12))

# Output Label
greedy.grid(row=0, column=0, padx=5, pady=5)
tgreedy.grid(row=0, column=1, padx=5, pady=5, columnspan=4)
greedy_bleu.grid(row=1, column=0, padx=5, pady=5)
# Output Textbox
tgreedy_bleu1.grid(row=1, column=1, padx=5, pady=5)
tgreedy_bleu2.grid(row=1, column=2, padx=5, pady=5)
tgreedy_bleu3.grid(row=1, column=3, padx=5, pady=5)
tgreedy_bleu4.grid(row=1, column=4, padx=5, pady=5)
root.mainloop()
