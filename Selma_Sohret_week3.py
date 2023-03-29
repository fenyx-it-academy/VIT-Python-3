#cevap1
#1a
listem = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]
sayi=int(input("Lutfen bir sayi giriniz."))

#1b
listem.insert(0,sayi)
print(listem)

#1c
tekli_sayilar=[]
for i in listem:
	if i%2:
		tekli_sayilar.append(i)
		
print(tekli_sayilar)

#1d
listem.sort()
print(listem)
tekli_sayilar.sort()
print(tekli_sayilar)

#cevap2a
listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6,"elma","Hollanda"]
print(listem2[2][1])

#2b
print(listem2[-1])

#2c
listem3=listem2[3:7]
print(listem3)

#2d
eleman_sayisi=len(listem3)
print(eleman_sayisi)

#2e
liste = [i for i in range(10)]
print(liste)
