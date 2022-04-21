class Inson:
    def __init__(self, ism, familiyasi, yoshi, jinsi ):
        self.ism = ism
        self.familiyasi=familiyasi
        self.yoshi=yoshi
        self.jinsi=jinsi

class Pupil(Inson):
    def __init__(self, ism, familiyasi, yoshi, jinsi, sinfi, tartib_raqami):
        super().__init__(ism, familiyasi, yoshi, jinsi)
        self.sinfi = sinfi
        self.tartib_raqami=tartib_raqami

uq1 = Pupil("Ilhom", "Iskandarov", 16, "Erkak",7, 15)
print(uq1)
print(uq1.ism)