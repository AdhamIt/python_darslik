class People:
    def __init__(self, ism, fam, yosh):
        self.name=ism
        self.surname=fam
        self.age=yosh
    
    def salom(self):
        print(("Assalomu aleykum do`stlar. Mening ismim {}").format(self.name))


odam1=People("Abduvohid", "Jumaniyazov", 17)
odam1.salom()
print(odam1.age)
print(type(odam1))
print(type(5))