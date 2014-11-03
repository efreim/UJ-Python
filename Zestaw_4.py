__author__ = 'Jakub Balazinski'

#4.1
print
print "Zadanie 4.1"
    #3.5
def linijka(dlugosc):
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

def prostokat (l,h):
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

print
print "Podaj dlugosc linijki: "
dlugosc = int(raw_input())
linijka(dlugosc)
print
print "Podaj ilosc kolumn"
l = int(raw_input())
print "Podaj ilosc wierszy"
h = int(raw_input())
prostokat(l,h)

#4.3
print
print "Zadanie 4.3"
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print "Podaj liczbe ktorej silnie chcesz obliczyc"
num = int(raw_input())
print factorial(num)

#4.4
print
print "Zadanie 4.4"
def fibonacci(m):
    if m == 0:
        return 0
    a = 1
    b = 1
    for i in range(0, m-2):
        tmp = a
        a = b
        b = tmp
        b += a
    return b
print "Podaj dla ktorego chcesz obliczyc n-ty wyraz ciag Fibonacciego"
num = int (raw_input())
print fibonacci(num)

#4.5
print
print "Zadanie 4.5"
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print L
def odwracanie(L, left, right):
    it = 0
    for item in range(left, right):
        if it < right/2:
            t = L[item]
            L[item] = L[right - it]
            L[right - it] = t
            it += 1
    return L
print "Odwracam liste od 3 do 7"
print odwracanie(L, 3, 7)


#4.6
print
print "Zadanie 4.6"
seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print seq
def sum_seq(sequnce):
    suma = 0
    for item in sequnce:
        if isinstance(item, (list, tuple)) == True:
            suma += sum_seq(item)
        else:
            suma += item

    return suma
print
print sum_seq(seq)

#4.7
print
print "Zadanie 4.7"
seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print seq
def flatten(sequnce, tmp):
    for item in sequnce:
        if isinstance(item, (list, tuple)) == True:
            flatten(item, tmp)
        else:
            tmp.append(item)
    return tmp
print
print flatten(seq, [])