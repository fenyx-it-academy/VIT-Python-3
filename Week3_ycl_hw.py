# Soru-1:

# listem = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]

# Yukarida verilen liste ile ilgili asagidaki sorulari yanitlayiniz.

# 1-a: Kullanicidan bir sayi girmesini isteyiniz,
# 1-b: Bu sayiyi verilen listenin ilk elemani olacak sekilde listeye ekleyiniz.
# 1-c: Olusan yeni listenin icindeki tekli sayilari listeden cikarip 
# tekli_sayilar adinda yeni bir liste olusturunuz.
# 1-d: Her iki listeyi buyukten kucuge olacak sekilde siralayip ekrana yazdiriniz.

listem = [2, 12, 9, 50, 7, 66, 91, 14, 143, 23, 48, 19, 100, 71, 28]

sayi=int(input("Lutfen bir sayi giriniz: "))

listem.insert(0, sayi)

tekli_sayilar = [x for x in listem if x % 2 != 0]  

listem = [i for i in listem if i not in tekli_sayilar]

listem.sort(reverse=True)
tekli_sayilar.sort(reverse=True)    
    
print(listem)
print(tekli_sayilar)

# Soru-2:

# listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]

# 2-a: Verilen listenin icerisindeki "Nazan" elemanina ulasip print ediniz.
# 2-b: Listenin son elemanina ulasip, print ediniz.
# 2-c: Verilen listenin icerisindeki 34, 65, 33, 5.6 elemanlarina erisip, 
# bu elemanlari yeni bir liste yapiniz.
# 2-d: Yeni listenin eleman sayisini yazdiriniz.
# 2-e: List Comprehensions (liste uretecleri) metodu ile, 
# 10 elemanli bir liste olusturunuz.

listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]

print(listem2[2][1])                 # "Nazan" elemanina ulasiliyor.
print(listem2[-1])                   #  Son elemana ulasiliyor.
yeni_liste = listem2[3:7]            #  Istenen araliktaki liste uretiliyor.
print(yeni_liste)                    #  Bu liste ekrana yazdiriliyor. 
print(len(yeni_liste))               #  Listenin eleman sayisi yazdiriliyor. 

new_list = list(range(10))           #  10 elemanli liste uretiliyor.
print(len(new_list))

new_list2 = [i for i in range(10)]   #  10 elemanli liste uretiliyor.
print(len(new_list2))
