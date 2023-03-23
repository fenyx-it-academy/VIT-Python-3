# Soru-1:

listem = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]

# Yukarida verilen liste ile ilgili asagidaki sorulari yanitlayiniz.


# 1-a: Kullanicidan bir sayi girmesini isteyiniz,

sayi=int(input("Lutfen bir sayi giriniz:"))


# 1-b: Bu sayiyi verilen listenin ilk elemani olacak sekilde listeye ekleyiniz.

listem.insert(0,sayi)
print(listem)


# 1-c: Olusan yeni listenin icindeki tekli sayilari listeden cikarip tekli_sayilar adinda yeni bir liste olusturunuz.

teksayilar=[i for i in listem if i%2==1 ]
print(teksayilar)



# 1-d: Her iki listeyi buyukten kucuge olacak sekilde siralayip ekrana yazdiriniz.

teksayilar.sort()
print(teksayilar)

listem.sort()
print(listem)

# Soru-2:

listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]

# 2-a: Verilen listenin icerisindeki "Nazan" elemanina ulasip print ediniz.

print(listem2[2][1])


# 2-b: Listenin son elemanina ulasip, print ediniz.

print(listem2[-1])


# 2-c: Verilen listenin icerisindeki 34, 65, 33, 5.6 elemanlarina erisip, bu elemanlari yeni bir liste yapiniz.

yeniListe=listem2[3:7]      
print(yeniListe) 

# 2-d: Yeni listenin eleman sayisini yazdiriniz.

print(len(yeniListe))


# 2-e: List Comprehensions (liste uretecleri) metodu ile, 10 elemanli bir liste olusturunuz.

listem3=[i for i in range(10)]
print(listem3)
