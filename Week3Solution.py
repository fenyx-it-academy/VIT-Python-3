# VIT-Python-3.Hafta odevi

# Soru-1: 


#=======================================================================================
#* 1-a: Kullanicidan bir sayi girmesini isteyiniz,
listem = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]
sayi= int(input('Lutfen bir sayi giriniz  '))

print(listem)
# * 1-b: Bu sayiyi verilen listenin ilk elemani olacak sekilde listeye ekleyiniz.
listem.insert(0,sayi)
print(listem)
# * 1-c: Olusan yeni listenin icindeki tekli sayilari listeden cikarip tekli_sayilar adinda yeni bir liste olusturunuz.
listetekli=[x for x in listem if x%2==1 ]
print(listetekli)
# * 1-d: Her iki listeyi buyukten kucuge olacak sekilde siralayip ekrana yazdiriniz.
listem.sort(reverse=True)
print(listem)
listetekli.sort(reverse=True)
print(listetekli)

# -----------------------------------------------------------------------

# Soru-2: 


# -----------------------------------------------------------------------

# * 2-a: Verilen listenin icerisindeki "Nazan" elemanina ulasip print ediniz.
listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]
print(listem2[2][1])
# * 2-b: Listenin son elemanina ulasip, print ediniz.
print(listem2[len(listem2)-1:])
# * 2-c: Verilen listenin icerisindeki 34, 65, 33, 5.6 elemanlarina erisip, bu elemanlari yeni bir liste yapiniz.
print(listem2[3:7])
# * 2-d: Yeni listenin eleman sayisini yazdiriniz.
print(len(listem2[3:7]))
# * 2-e: List Comprehensions (liste uretecleri) metodu ile, 10 elemanli bir liste olusturunuz.
liste = [x for x in range (10) ]
print(liste)