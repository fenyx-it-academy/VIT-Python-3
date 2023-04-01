#Soru-1
listem = [2,12, 9, 50, 7, 66,91,14, 143,23, 48, 19,100,71,28]
#1-a:
my_number = int(input("Sayi giriniz: "))
#1-b:
listem.insert(0,my_number)
#1-c:
tekli_sayilar=[i for i in listem if i % 2 == 1]
#1-d:
print(sorted(listem, reverse=True), sorted(tekli_sayilar, reverse=True), sep="\n")


#Soru-2 (Not: Listeye yeni elemanlar ekledim.)
listem2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33,"Nazan", 5.6,"elma",["Nazan", "Zeynep"],"Hollanda"]
#2-a:
for index, item in enumerate(listem2):
    if item == "Nazan":
        print(f"Index {index}=> {listem2[index]}")
    # print(index, item) 
    else:
        if type(item) != list:
            continue
        else:
            for index2, item2 in enumerate(item):
                if item2 == "Nazan":
                    print(f"In index-{index}, index-{index2} => {listem2[index][index2]}")

#2-b:
print(listem2[-1])

#2-c:
int_list = []
for item in listem2:
    if type(item) == int or type(item) == float:
        int_list.append(item)
print(int_list)

#2-d:
print(len(int_list))

#2-e:
while True:
    check_number = int(input("Type an integer: ")) #For right answer type -> 151 -  165
    
    my_list_10 = [f"{i}-> Fizz" if i %10 ==0 else f"{i} -> Buzz"  for i in range(1,check_number) if i % 3 == 0 if i%5 == 0]
    
    if len(my_list_10) != 10:
        print(f"Sorry len of {check_number} is {len(my_list_10)}, Try again!")
        continue
    else:
        print(f"List of {len(my_list_10)}:  {my_list_10}")
        break


