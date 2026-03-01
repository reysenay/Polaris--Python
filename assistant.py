class Asistan:
    def __init__(self, isim):
        self.isim = isim
        self.islem_sayisi = 0

    def selam_ver(self, kullanici_adi):
        self.islem_sayisi += 1
        print(f"Merhaba {kullanici_adi}, ben {self.isim}. Sana nasıl yardım edebilirim?")

    def durum_raporu(self):
        print(f"Bugüne kadar toplam {self.islem_sayisi} işlem gerçekleştirdim.")


if __name__ == "__main__":
    a = Asistan("SenaAsistan")
    a.selam_ver("Sena")
    a.selam_ver("Merve")
    a.selam_ver("İrem")
    a.durum_raporu()