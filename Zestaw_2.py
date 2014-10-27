"""
line = "Just follow the following simple steps to"
    # 2.10
item = line.split()
size = len(item)
print (size)
     
    # 2.11
newitem = "_".join(item)
print (newitem)
     
    # 2.12
result = ""
res= ""
suma=""
longer=""
for sth in item:
  if len(sth)>len(longer):
    longer=sth
  suma = suma + sth
  result = result + sth[0]
  res = res + sth[len(sth)-1]
   
     
print (result)
print (res)
     
     
print (len(suma)) # 2.13
 
# 2.14    
print (longer)
print (len(longer))
     
    # 2.15
napis=""
L = [10, 20, 30, 40, 50, 60, 70]
for item in L:
 napis+=str(item)
print (napis)
     
    # 2.16
linia = "GvR jakis GvR text"
print (linia.replace("GvR","Guido van Rossum"));
     
    # 2.17
     
print (sorted(linia.split()))
print (sorted(linia.split(),key=len))
     
    # 2.18
     
i = 100324050
count=0
for it in str(i):
  if it=="0":
    count+=1
print (count)
     
    # 2.19
     
lista = [1,3,54,87,100,443,10]
nap=""
for number in lista:
  print (str(number).zfill(3))
  nap+= str(number).zfill(3)
           
print (nap)"""

#3.3
"""for i in range(0, 31):
    if i % 3 != 0:
        print i
"""

#3.4
"""
dupa=""

while dupa!="stop":
    dupa=raw_input()
    if dupa != "stop":
        print dupa ,int(dupa)**3"""

#3.5
"""
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
print str1"""

#3.6
"""
l = int(raw_input())
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
print ''.join(table)"""

#3.8
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