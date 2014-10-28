
#3.3
print
print "Zadanie 3.3"
for i in range(0, 31):
    if i % 3 != 0:
        print i


#3.4
print
print "Zadanie 3.4"
word=""

print "Wpisz liczbe ktora chcesz podniesc do potegi 3 lub stop aby zakonczyc"
while word!="stop":
    word=raw_input()
    if word != "stop":
        print word ,int(word)**3

#3.5
print
print "Zadanie 3.5"
print "Podaj dlugosc linijki: "
dlugosc = int(raw_input())
str2=""
str1=""
for i in range(0, dlugosc):
    if i<10:
        str2+="|...."
    else:
        str2+="|....."
str2+="|"

for i in range(0, dlugosc):
        str1+=str(i) + "    "

str1+=str(dlugosc)

print str2
print str1

#3.6
print
print "Zadanie 3.6"
print "Podaj ilosc kolumn"
l = int(raw_input())
print "Podaj ilosc wierszy"
h = int(raw_input())
table=[]
boxh=""
boxl=""

for i in range(0, l):
    boxh += "+---"
    boxl += "|   "

boxh += "+"
boxl += "|"

for k in range(0, h):
    table.append(boxh)
    table.append("\n")
    table.append(boxl)
    table.append("\n")

table.append(boxh)
print ''.join(table)

#3.8
print
print "Zadanie 3.8"
word1 = ["some","random","word","some","word"]
word2 = ["random","word","word","random","onion"]
new_word = []
word12 = []

for item1 in word1:
    for item2 in word2:
        if item1 == item2:
            if item1 not in new_word:
                new_word.append(item1)
        if item2 not in word12:
            word12.append(item2)
        elif item1 not in word12:
            word12.append(item1)



print new_word
print word12

#3.9
print
print "Zadanie 3.9"
lista = [[],[4],(1,2),[3,4],(5,6,7)]
wynik = []
suma = 0

for item in lista:
    for it in range(len(item)):
        suma+=item[it]
    wynik.append(suma)
    suma = 0


#[0,4,3,7,18]
print wynik

#3.10
print
print "Zadanie 3.10"
r = {'I' : 1, 'V' : 5, 'X' : 10, 'L': 50, 'C' : 100, 'D' : 500, 'M' : 1000}

roman = 'IDM'
normal = 0

for it in roman:
    normal += r.get(it)

print roman, " = ", normal

