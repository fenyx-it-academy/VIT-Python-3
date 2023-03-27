# Soru-1:

listem = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]

# Yukarida verilen liste ile ilgili asagidaki sorulari yanitlayiniz.

# 1-a: Kullanicidan bir sayi girmesini isteyiniz,
# 1-b: Bu sayiyi verilen listenin ilk elemani olacak sekilde listeye ekleyiniz.
# 1-c: Olusan yeni listenin icindeki tekli sayilari listeden cikarip tekli_sayilar adinda yeni bir liste olusturunuz.
# 1-d: Her iki listeyi buyukten kucuge olacak sekilde siralayip ekrana yazdiriniz.

number = int(input('Sayi giriniz :'))

listem.insert(0,number)

print(listem)

tekli_sayilar = [i for i in listem if i % 2 == 1 ]

tekli_sayilar.sort(),tekli_sayilar.reverse()

listem.sort(), listem.reverse()

print(listem)

print(tekli_sayilar)

print("----------------------------------------------------------------")

# Soru-2:

listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]

# 2-a: Verilen listenin icerisindeki "Nazan" elemanina ulasip print ediniz.
# 2-b: Listenin son elemanina ulasip, print ediniz.
# 2-c: Verilen listenin icerisindeki 34, 65, 33, 5.6 elemanlarina erisip, bu elemanlari yeni bir liste yapiniz.
# 2-d: Yeni listenin eleman sayisini yazdiriniz.
# 2-e: List Comprehensions (liste uretecleri) metodu ile, 10 elemanli bir liste olusturunuz.

print(listem2[2][1])

print(listem2[-1])

newlist = [i for i in listem2 if i == 34 or i == 65 or i == 33 or i == 5.6]

print(len(newlist))

lastlist = [i for i in range(10)]
