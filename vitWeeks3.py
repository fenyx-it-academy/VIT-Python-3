# Soru 1 Cevaplari

listem = [2, 12, 9, 50, 7, 66, 91, 14, 143, 23, 48, 19, 100, 71, 28]

# 1-a
sayi = int(input("Lutfen bir sayi giriniz: "))

# 1-b
listem.insert(0, sayi)
print('Yeni liste: ', listem)

# 1-c

tek = [i for i in listem if i % 2 == 1]

print('Tek sayilar: ', tek)

# 1-d
listem.sort(reverse=True)
print('Buyuktek kucuge sayilar: ', listem)

tek.sort(reverse=True)
print('Buyukten kucuge tek sayilar:', tek)


# Soru 2 Cevaplari

listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"],
           34, 65, 33, 5.6, "elma", "Hollanda"]

# 2-a

print(listem2[2][1])

# 2-b

print('Son Eleman: ', listem2[-1])

# 2-c
sayiList = listem2[3:7]
print(sayiList)

# 2-d
print(len(sayiList))

# 2-e
yeniListe = [i+1 for i in range(10)]
print('List Comprehensions ile 10 elemanli liste: ', yeniListe)
