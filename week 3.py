#1.Sorunun Cevabı

listem = [2,12,9,50,7,66,91,14,143,23,48,19,100,71,28]
listemtek=[]
listem.insert(0, int(input("Lütfen bir sayı giriniz:  "))) #kullanıcıdan bir sayı girmesini istiyoruz ve bunu listemizin ilk elemamı olarak ekliyoruz
print(listem)

for i in listem:
    
    if i%2==1:            #listedeki sayıların tek mi çift mi olduğunu kontrol ediyoruz
        listemtek.append(i)     #eğer sayı tek ise yeni listeye ekliyoruz ve eski listeden siliyoruz
        listem.remove(i)

listemtek.sort()       #listeyi küçükten büyüğe sıralıyoruz
listemtek.reverse()    #büyükten küçüğe istendiği için ters çeviriyoruz  ve yazdırıyoruz
listem.sort()
listem.reverse()
print("Tek Sayılar:   ",listemtek)
print("Çift Sayılar :  ",listem)
    
#-----------------------------------------
#2. Sorunun Cevabı
listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]
print(listem2[2][1])
print(listem2[-1:])
yeniliste=listem2[3:7]
##yeniliste=[x  for x in listem2 if x==34 or x==65 or x==33 or x==5.6]   bu metod ilede yapılabilir
print(yeniliste)
print("YENİ LİSTENİN ELEMENAN SAYISI:  ",len(yeniliste))
listeolustur=[x for x in "ILYASCAN@VIT" ]
print(listeolustur)
