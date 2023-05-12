from tkinter import *

from PIL import ImageTk, Image


def crea_immagini():
    img = Image.open("img/snake-graphics.png").convert("RGBA")

    immagini = []

    mela = Image.open("img/mela.png").convert("RGBA").resize((20, 20))
    testa = img.crop([194, 0, 254, 62]).resize((20, 20))
    corpo_dritto = img.crop([60, 0, 120, 62]).resize((20, 20)).rotate(90)
    corpo_angolo = img.crop([0, 62, 64, 126]).resize((20, 20))
    coda = img.crop([193, 128, 255, 190]).resize((20, 20))

    immagini.append(ImageTk.PhotoImage(testa))
    immagini.append(ImageTk.PhotoImage(testa.rotate(90)))
    immagini.append(ImageTk.PhotoImage(testa.rotate(180)))
    immagini.append(ImageTk.PhotoImage(testa.rotate(-90)))

    immagini.append(ImageTk.PhotoImage(corpo_dritto))
    immagini.append(ImageTk.PhotoImage(corpo_dritto.rotate(90)))
    immagini.append(ImageTk.PhotoImage(corpo_dritto.rotate(180)))
    immagini.append(ImageTk.PhotoImage(corpo_dritto.rotate(-90)))

    immagini.append(ImageTk.PhotoImage(corpo_angolo))
    immagini.append(ImageTk.PhotoImage(corpo_angolo.rotate(90)))
    immagini.append(ImageTk.PhotoImage(corpo_angolo.rotate(180)))
    immagini.append(ImageTk.PhotoImage(corpo_angolo.rotate(-90)))

    immagini.append(ImageTk.PhotoImage(coda))
    immagini.append(ImageTk.PhotoImage(coda.rotate(90)))
    immagini.append(ImageTk.PhotoImage(coda.rotate(180)))
    immagini.append(ImageTk.PhotoImage(coda.rotate(-90)))

    immagini.append(ImageTk.PhotoImage(mela))

    return immagini
