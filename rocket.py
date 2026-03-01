class Roket:
    def __init__(self, isim, yakit_seviyesi):
        self.isim = isim
        self.yakit_seviyesi = int(yakit_seviyesi)

    def yakit_doldur(self, miktar):
        self.yakit_seviyesi += int(miktar)
        print(f"Yakit eklendi. Yeni seviye: {self.yakit_seviyesi}")

    def firlat(self):
        if self.yakit_seviyesi >= 10:
            print("Roket başarıyla fırlatıldı! 🌍 -> 🌕")
            self.yakit_seviyesi -= 10
        else:
            print("Hata: Yetersiz yakıt! Lütfen yakıt doldurun.")


if __name__ == "__main__":
    r = Roket("Apollo 11", 5)
    r.firlat()
    r.yakit_doldur(10)
    r.firlat()
    r.firlat()
    print("Kalan yakıt:", r.yakit_seviyesi)