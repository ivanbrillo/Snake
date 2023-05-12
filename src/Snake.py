from Serpente import *
from image import *

root = Tk()
# root.geometry("600x600")
root.geometry("300x500")
root.config(bg="gray30")
root.resizable(False, False)
root.title("Snake")
root.iconbitmap("img/bitmap.ico")

playimg = PhotoImage(file="img/play.png")
cambiasf = PhotoImage(file="img/cambiasf.png")
skinimg = PhotoImage(file="img/skin.png")
sfondo = PhotoImage(file="img/sfondo2.png")
game_over = PhotoImage(file="img/game_over.png")

def gioca():
    play.destroy()
    skin.destroy()
    cambia_sfondo.destroy()
    root.geometry("600x600")
    canvas = Canvas(root, bg="white", borderwidth=0)
    canvas.place(x=0,y=0, width=600, height=600)
    canvas.create_image(0, 0, image=sfondo, anchor="nw")
    Serpente(root, canvas, crea_immagini(), game_over)


play = Button(root, image=playimg, borderwidth=0, command=gioca)
play.place(rely=0.025, relx=0.5, anchor=N, relheight=0.3, relwidth=0.9)

skin = Button(root, image=skinimg, borderwidth=0)
skin.place(rely=0.35, relx=0.5, anchor=N, relheight=0.3, relwidth=0.9)

cambia_sfondo = Button(root, image=cambiasf, borderwidth=0)
cambia_sfondo.place(rely=0.675, relx=0.5, anchor=N, relheight=0.3, relwidth=0.9)


root.mainloop()
