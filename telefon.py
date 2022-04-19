class Phone:
    def __init__(self, model, hotira, rangi, narxi, uzunligi, ogirlig):
        self.model=model
        self.memory=hotira
        self.color=rangi
        self.cost=narxi
        self.height=uzunligi
        self.weight=ogirlig
    def tarif(self):
        if self.cost < 1500000:
            print("Telefoning pas akan " + "Telefon nomi : {}".format(self.model))

redmi5=Phone("RedMe", "32Gb", "Black", 1200000, "15sm", "200gr")
redmi5.tarif()
samsung_s_22=Phone("Samsung S 22", "128Gb", "Black", 9000000, "20sm", "350gr")
samsung_s_22.tarif()
iphone5=Phone("Iphone", "16Gb", "Gold", 1000000, '10sm', '150gr')
iphone5.tarif()