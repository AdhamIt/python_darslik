class Pupil:
    def __init__(self, ism, fam, phone):
        self.name=ism
        self.fam=fam
        self.phone=phone

# O`quvchilarni qo`lda kiritadigan qilib ishlaymiz.

text = "yes"
uquvchilar = []
while text == "yes" or text=="":
    name=input("Foydalanuvchi ismini kiriting : ")
    fam=input("Foydalanuvchi familiyasini kiriting : ")
    phone=input("Foydalanuvchi tel raqamini kiriting : ")

    file = open("uquvchilar.txt", 'a')
    file.write("O`quvchi ismi: " + name+"\n")
    file.write("O`quvchi Familiyasi: " +fam+"\n")
    file.write("O`quvchi Telefon raqami: " +phone+"\n")

    file.write("======"+"\n")
    file.close()
    
    uquvchi = Pupil(name, fam, phone)
    uquvchilar.append(uquvchi)
    print("Yana o`quvchi kiritasizmi ?")
    text=input()

print("Jami o`quvchilar soni {} ga teng.".format(len(uquvchilar)))