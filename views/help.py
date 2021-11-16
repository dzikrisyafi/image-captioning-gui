from tkinter import *


def helpWindow():
    hWindow = Toplevel()
    hWindow.title("Cara Penggunaan")
    hWindow.geometry("600x250")

    help = LabelFrame(hWindow, text="Cara Penggunaan", padx=20, pady=20)
    help.configure(font=('Segoe UI', 20, 'bold'))
    help.pack(padx=20, pady=20)

    desc = Label(
        help, text="1. Tekan tombol masukkan gambar.\n2. Pilih gambar yang ingin diprediksi.\n3. Tekan tombol proses dengan model yang diinginkan.\n4. Tunggu proses prediksi selesai.\n5. Prediksi akan tampil pada frame output.", justify=LEFT, padx=10)
    desc.configure(font=('Arial', 14))
    desc.grid(row=1, column=0, columnspan=7)
