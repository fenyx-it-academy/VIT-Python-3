# Soru-1:
# listem = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]
# Yukarida verilen liste ile ilgili asagidaki sorulari yanitlayiniz.
# 1-a: Kullanicidan bir sayi girmesini isteyiniz,
# 1-b: Bu sayiyi verilen listenin ilk elemani olacak sekilde listeye ekleyiniz.
# 1-c: Olusan yeni listenin icindeki tekli sayilari listeden cikarip tekli_sayilar adinda yeni bir liste olusturunuz.
# 1-d: Her iki listeyi buyukten kucuge olacak sekilde siralayip ekrana yazdiriniz.

listem = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]
sayi=int(input("Lütfen bir sayı giriniz...: "))
listem.insert(0,sayi)
print (listem)
tekSayilar=[]
listemIndex=0
for liste in listem:
    if liste%2==1:
        tekSayilar.append(liste)
        del listem[listemIndex]
    listemIndex+=1
tekSayilar.sort()
listem.sort()
print(tekSayilar)
print(listem)