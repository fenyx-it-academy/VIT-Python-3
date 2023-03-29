cevap1
# Kullanicidan bir sayi girmesini istiyoruz
listem = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]
number=int(input("Bir sayi giriniz:"))
# Bu sayiyi verilen listenin ilk elemani olacak sekilde listeye ekliyoruz
listem.insert(0,number)
print("Girilen sayi ilk eleman olarak ekleniyor ",listem)
#yeni listenin icindeki tekli sayilari listeden cikarip tekli_sayilar adinda yeni bir liste olusturunuz.
tekli_sayilar = []
deneme=tuple(listem)
for i in deneme:
    if i%2==1:
      tekli_sayilar.append(i)
      listem.remove(i)
#Her iki listeyi buyukten kucuge olacak sekilde siralayip ekrana yazdiriyoruz
tekli_sayilar.sort()
listem.sort()
print("Tekli sayilar buyukten kucuge ",tekli_sayilar[::-1])
print("listem buyukten kucuge:", listem[::-1])


cevap2
listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]
#Verilen listenin icerisindeki "Nazan" elemanina ulasip print ediyoruz
print(listem2[2][1])
#Listenin son elemanina ulasip, print ediyoruz
print(listem2[-1])
#Verilen listenin icerisindeki 34, 65, 33, 5.6 elemanlarina erisip, bu elemanlari yeni bir liste yapiyoruz.
#Yeni listenin eleman sayisini yazdiriyoruz
yeni_list=list((listem2[3:7]))
print(len(yeni_list))
#List Comprehensions (liste uretecleri) metodu ile, 10 elemanli bir liste olusturuyoruz
yeni_list=[i for i in range(10)]

print(yeni_list)
