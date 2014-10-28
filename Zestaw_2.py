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
           
print (nap)
