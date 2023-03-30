#Soru_1

listem = [2, 12, 9, 50, 7, 66, 91, 14, 143, 23, 48, 19, 100, 71, 28]

sayi = int(input("Lütfen sayı giriniz: "))

listem.insert(0, sayi)

tekli_sayilar = [i for i in listem if i % 2 == 1]

print("yeni_listem : ", sorted(listem, reverse=True))

print("tekli_sayilar : ", sorted(tekli_sayilar, reverse=True))



#Soru_2

listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"],34, 65, 33, 5.6, "elma", "Hollanda"]

print(listem2[2][1])

print(listem2[-1])

yeni_liste = listem2[3:7]

print(len(yeni_liste))

son_liste = [i for i in range(20) if i % 2 == 0]
print(son_liste)
