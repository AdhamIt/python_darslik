class Futbolchi:
    def __init__(self, name, number, position, gools, accist):
        self.name=name
        self.number=number
        self.position=position
        self.gools=gools
        self.accist=accist

MYu = [
    Futbolchi("Ronoldo", 7, "Hujumchi", 800, 800),
    Futbolchi("Reshford", 10, "Hujumchi", 150, 100),
    Futbolchi("Sancho", 11, "Hujumchi", 100,150),
    Futbolchi("Pogba", 6, "Yarim himoya", 300,300),
    Futbolchi("Bruno Frenandesh", 18, "Yarim himoya", 150, 150),
    Futbolchi("Fred", 17, "Yarim himoya", 50,80),
    Futbolchi("Mc Tominay", 39, "Yarim himoya", 10,20),
    Futbolchi("Maguire", 5, "Himoyach", 10,5),
    Futbolchi("Degea", 4, "Darvoza", 0,0),
    Futbolchi("Wan Bissaca", 6, "Himoyachi", 2,4),
    Futbolchi("Varan", 3, "Himoyachi", 6,9)
]
# print(MYu)
for x in MYu:
    print(x.number, x.name)