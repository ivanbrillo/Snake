from random import randint


class Mela:

    def __init__(self, canvas, serp, img):
        self.canvas = canvas
        self.img = img
        self.creaMela()

        while len(self.canvas.find_enclosed(self.xmela - 1, self.ymela - 1, self.xmela + 21, self.ymela + 21)) > 1:
            canvas.delete(self.mela)
            self.creaMela()

        serp.aggMela(self.mela)

    def creaMela(self):
        self.xmela = randint(0, 29) * 20
        self.ymela = randint(0, 29) * 20

        self.mela = self.canvas.create_image(self.xmela, self.ymela, image=self.img, anchor="nw")
