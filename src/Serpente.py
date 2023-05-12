from tkinter import *

from Mela import *


class Serpente:
    rect = []
    foto = []

    def __init__(self, root, canvas, immagini, game_over):

        self.rect.append([300, 300])
        self.rect.append([280, 300])
        self.rect.append([260, 300])

        self.game_over = game_over

        # testa = PhotoImage(file="testa.png")
        # canvas.create_image(20, 20, image=immagini[-2], anchor="nw")

        self.immagini = immagini

        self.root = root
        self.canvas = canvas
        self.vx = +20
        self.vy = 0
        self.disegna()

        root.bind("<Key>", self.keypress)
        Mela(canvas, self, self.immagini[-1])
        self.muovi()

    def keypress(self, event):
        x1 = self.rect[0][0]
        y1 = self.rect[0][1]

        x2 = self.rect[-len(self.rect) + 1][0]
        y2 = self.rect[-len(self.rect) + 1][1]

        if event.keycode == 38 and y1 - 20 != y2:
            self.vy = -20
            self.vx = 0

        elif event.keycode == 40 and y1 + 20 != y2:
            self.vy = 20
            self.vx = 0

        elif event.keycode == 39 and x1 + 20 != x2:
            self.vx = 20
            self.vy = 0

        elif event.keycode == 37 and x1 - 20 != x2:
            self.vy = 0
            self.vx = -20

    def aggMela(self, mela):
        self.mela = mela

    def muovi(self):
        self.bordi()

        x = self.rect[0][0]
        y = self.rect[0][1]
        # trova intersezioni con le immagini presenti
        overlap = self.canvas.find_enclosed(x + self.vx - 1, y + self.vy - 1, x + self.vx + 21, y + self.vy + 21)

        if len(overlap) > 0 and self.mela not in overlap:
            self.canvas.create_image(300, 300, image=self.game_over, anchor="center")
            return
        # self.root.quit()

        self.rect.insert(0, [x + self.vx, y + self.vy])

        # self.canvas.moveto(self.prova[0], x + self.vx, y + self.vy)

        if self.mela not in overlap:
            # self.canvas.delete(self.rect[-1])
            self.rect.pop(-1)
        else:
            self.canvas.delete(self.mela)
            Mela(self.canvas, self, self.immagini[-1])

        self.disegna()
        self.canvas.after(200, self.muovi)

    def bordi(self):
        if self.rect[0][0] + self.vx > 600:
            self.rect[0] = [0, self.rect[0][1]]
        elif self.rect[0][0] + self.vx < -20:
            self.rect[0] = [+580, self.rect[0][1]]
        elif self.rect[0][1] + self.vy > 580:
            self.rect[0] = [self.rect[0][0], 0]
        elif self.rect[0][1] + self.vy < -20:
            self.rect[0] = [self.rect[0][0], 580]

    def disegna(self):

        vx = self.vx
        vy = self.vy

        for i in range(len(self.foto)):
            self.canvas.delete(self.foto[i])
        # testa
        if vx == 20:
            self.foto.append(self.canvas.create_image(self.rect[0][0], self.rect[0][1], image=self.immagini[3], anchor="nw"))
        elif vx == -20:
            self.foto.append(self.canvas.create_image(self.rect[0][0], self.rect[0][1], image=self.immagini[1], anchor="nw"))
        elif vy == 20:
            self.foto.append(self.canvas.create_image(self.rect[0][0], self.rect[0][1], image=self.immagini[2], anchor="nw"))
        elif vy == -20:
            self.foto.append(self.canvas.create_image(self.rect[0][0], self.rect[0][1], image=self.immagini[0], anchor="nw"))

        # corpo
        for i in range(1, len(self.rect) - 1):
            if (vx == 20 or vx == -20):
                if self.rect[i][1] == self.rect[i + 1][1]:
                    self.foto.append(self.canvas.create_image(self.rect[i][0], self.rect[i][1], image=self.immagini[5], anchor="nw"))

                elif vx == 20 and self.rect[i][1] > self.rect[i + 1][1]:
                    self.foto.append(self.canvas.create_image(self.rect[i][0], self.rect[i][1], image=self.immagini[8], anchor="nw"))
                    vx = 0
                    vy = 20
                elif vx == 20 and self.rect[i][1] < self.rect[i + 1][1]:
                    self.foto.append(self.canvas.create_image(self.rect[i][0], self.rect[i][1], image=self.immagini[11], anchor="nw"))
                    vx = 0
                    vy = -20

                elif vx == -20 and self.rect[i][1] > self.rect[i + 1][1]:
                    self.foto.append(self.canvas.create_image(self.rect[i][0], self.rect[i][1], image=self.immagini[9], anchor="nw"))
                    vx = 0
                    vy = 20
                elif vx == -20 and self.rect[i][1] < self.rect[i + 1][1]:
                    self.foto.append(self.canvas.create_image(self.rect[i][0], self.rect[i][1], image=self.immagini[10], anchor="nw"))
                    vx = 0
                    vy = -20
            elif (vy == 20 or vy == -20):
                if self.rect[i][0] == self.rect[i + 1][0]:
                    self.foto.append(self.canvas.create_image(self.rect[i][0], self.rect[i][1], image=self.immagini[6], anchor="nw"))

                elif vy == 20 and self.rect[i][0] > self.rect[i + 1][0]:
                    self.foto.append(self.canvas.create_image(self.rect[i][0], self.rect[i][1], image=self.immagini[10], anchor="nw"))
                    vx = 20
                    vy = 0
                elif vy == 20 and self.rect[i][0] < self.rect[i + 1][0]:
                    self.foto.append(self.canvas.create_image(self.rect[i][0], self.rect[i][1], image=self.immagini[11], anchor="nw"))
                    vx = -20
                    vy = 0

                elif vy == -20 and self.rect[i][0] > self.rect[i + 1][0]:
                    self.foto.append(self.canvas.create_image(self.rect[i][0], self.rect[i][1], image=self.immagini[9], anchor="nw"))
                    vx = 20
                    vy = 0
                elif vy == -20 and self.rect[i][0] < self.rect[i + 1][0]:
                    self.foto.append(self.canvas.create_image(self.rect[i][0], self.rect[i][1], image=self.immagini[8], anchor="nw"))
                    vx = -20
                    vy = 0

        # coda
        if vx == 20:
            self.foto.append(self.canvas.create_image(self.rect[-1][0], self.rect[-1][1], image=self.immagini[-2], anchor="nw"))
        elif vx == -20:
            self.foto.append(self.canvas.create_image(self.rect[-1][0], self.rect[-1][1], image=self.immagini[-4], anchor="nw"))
        elif vy == 20:
            self.foto.append(self.canvas.create_image(self.rect[-1][0], self.rect[-1][1], image=self.immagini[-3], anchor="nw"))
        elif vy == -20:
            self.foto.append(self.canvas.create_image(self.rect[-1][0], self.rect[-1][1], image=self.immagini[-5], anchor="nw"))
