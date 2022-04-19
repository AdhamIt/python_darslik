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
print(getattr(odam1, 'age'))
setattr(odam1, 'age', 20)
print(getattr(odam1, 'name'))
print(getattr(odam1, 'age'))

print(odam1.__dict__)
print(odam1.__doc__)
print(odam1.__module__)