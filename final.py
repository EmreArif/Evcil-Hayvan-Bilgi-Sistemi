import sqlite3
con = sqlite3.connect("veriler.db")
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler (cins_TEXT, ad_TEXT, yas_TEXT )")
    con.commit()
tablo_olustur()
def veri_ekle(cins,ad,yas):
    cursor.execute("Insert into bilgiler VALUES (?,?,?)", (cins,ad,yas))
    con.commit()

class Dosyalar:
    def yavrukedi1(self):
        yavrukedi1=open("yavrukedi.txt")
        print("\n")
        print(yavrukedi1.read())
    def yavrukedi2(self):
        yavrukedi2=open("yavrukedi2.txt")
        print("\n")
        print(yavrukedi2.read())
    def yetiskinkedi(self):
        yetiskinkedi=open("yetiskinkedi.txt")
        print("\n")
        print(yetiskinkedi.read())
    def yetiskinkedi2(self):
        yetiskinkedi2=open("yetiskinkedi2.txt")
        print("\n")
        print(yetiskinkedi2.read())
    def yavrukopek1(self):
        yavrukopek1=open("yavrukopek.txt")
        print("\n")
        print(yavrukopek1.read())
    def yavrukopek2(self):
        yavrukopek2=open("yavrukopek2.txt")
        print("\n")
        print(yavrukopek2.read())
    def yetiskinkopek1(self):
        yetiskinkopek1=open("yetiskinkopek1.txt")
        print("\n")
        print(yetiskinkopek1.read())
    def yetiskinkopek2(self):
        yetiskinkopek2=open("yetiskinkopek2.txt")
        print("\n")
        print(yetiskinkopek2.read())

def tamam(a):

    if a=="1":
        return a
    elif a=="2":
        exit()




while True:
    dosya=Dosyalar()
    bilgiler=[]
    sozluk={"Evcil Hayvan Bilgileri":bilgiler}
    cins=input("Evcil hayvanınızın cinsi (Kedi? Köpek?):")
    bilgiler.append(cins)
    ad=input("\n{} adı:".format(cins))
    bilgiler.append(ad)
    yas=input("\n{} yavru ise 'Yavru' yetişkin ise 'Yetiskin' yazınız: ".format(ad))
    bilgiler.append(yas)
    veri_ekle(cins, ad, yas)
    con.close()
    print(sozluk)
    for i in bilgiler:
        if i =="Kedi" and yas=="Yavru":
            print("\n{} {} menüsüne gidiliyor....".format(yas,cins))
            scnk=input("\nAşı takvimini öğrenmek için '1' e Mama tavsiyeleri için '2' ye basınız:")
            if scnk=="1":
                dosya.yavrukedi1()
                a=input("\nAna menü için '1'e Çıkış için '2'ye basınız:")
                tamam(a)
            elif scnk=="2":
                dosya.yavrukedi2()
                a = input("\nAna menü için '1'e Çıkış için '2'ye basınız:")
                tamam(a)
        elif i=="Kedi" and yas=="Yetiskin":
            print("\n{} {} menüsüne gidiliyor....".format(yas, cins))
            scnk = input("\nAşı takvimini öğrenmek için '1' e Mama tavsiyeleri için '2' ye basınız:")
            if scnk == "1":
                dosya.yetiskinkedi()
                a = input("Ana menü için '1'e Çıkış için '2'ye basınız:")
                tamam(a)
            elif scnk == "2":
                dosya.yetiskinkedi2()
                a = input("\nAna menü için '1'e Çıkış için '2'ye basınız:")
                tamam(a)
        elif i=="Köpek" and yas=="Yavru":
            print("\n{} {} menüsüne gidiliyor...".format(yas,cins))
            scnk = input("\nAşı takvimini öğrenmek için '1' e Mama tavsiyeleri için '2' ye basınız:")
            if scnk == "1":
                dosya.yavrukopek1()
                a = input("\nAna menü için '1'e Çıkış için '2'ye basınız:")
                tamam(a)
            elif scnk == "2":
                dosya.yavrukopek2()
                a = input("\nAna menü için '1'e Çıkış için '2'ye basınız:")
                tamam(a)
        elif i=="Köpek" and yas=="Yetiskin":
            print("\n{} {} menüsüne gidiliyor...".format(yas,cins))
            scnk = input("\nAşı takvimini öğrenmek için '1' e Mama tavsiyeleri için '2' ye basınız:")
            if scnk == "1":
                dosya.yetiskinkopek1()
                a = input("\nAna menü için '1'e Çıkış için '2'ye basınız:")
                tamam(a)
            elif scnk == "2":
                dosya.yetiskinkopek2()
                a = input("\nAna menü için '1'e Çıkış için '2'ye basınız:")
                tamam(a)

