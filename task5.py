# У солдата Райана есть AK47
# Солдаты могут стрелять ("тиги-тигитиш").
# Оружие может стрелять пулями.
# Пушки могут заполнять патроны - увеличивать количество пуль (перезаряжать)

class Soldier:

    def __init__(self, name):
        self.name = name

class Guns:

    def __init__(self):
        self.bullets = 30

    def ak47(self):
        print(f"\tСолдат {self.name.title()} крикнул атата")
        print(f"\t\tAK47 сделал:")
        if self.bullets:
            piy = 0
            for i in range(self.bullets):
                piy += 1
                self.bullets -= 1
                print("\t\t\tтиги-тигитиш", piy)
        else:
            print(f"Патронов не нету")
        self.patrons()

    def patrons(self):
        print(f"\t\t\tПатронов: {self.bullets} шт")

    def reload(self):
        self.bullets = 40
        print(f"\t\t\t\tСолдат {self.name.title()} крикнул атата перезарядка")

class Act_of_Shooting(Soldier, Guns):
    def __init__(self, name):
        Soldier.__init__(self, name)
        Guns.__init__(self)
        print(f"\t\t\tПатронов: {self.bullets} шт")



soldat = Act_of_Shooting("ryan")
soldat.ak47()
# soldat.ak47(30)


# soldat.reload()
# soldat.patrons()
# soldat.ak47()
# soldat.ak47()




