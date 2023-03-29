# listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]

# 2-a: Verilen listenin icerisindeki "Nazan" elemanina ulasip print ediniz.
# 2-b: Listenin son elemanina ulasip, print ediniz.
# 2-c: Verilen listenin icerisindeki 34, 65, 33, 5.6 elemanlarina erisip, 
# bu elemanlari yeni bir liste yapiniz.
# 2-d: Yeni listenin eleman sayisini yazdiriniz.
# 2-e: List Comprehensions (liste uretecleri) metodu ile, 
# 10 elemanli bir liste olusturunuz.

listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]
print(listem2[2][1])
print(listem2[-1])
listeYeni=[]
listeYeni=listem2[3:7]
#del listem2[3:7]
print(listeYeni)
print(listem2)
print("Yeni listenin eleman sayısı : ", len(listeYeni))
copmListe=[i for i in range(1,31) if i%3==0]
print(copmListe)