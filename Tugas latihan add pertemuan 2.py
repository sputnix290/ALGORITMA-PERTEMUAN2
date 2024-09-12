from collections.abc import ByteString
import numpy as np
A=[1, 2, 3]
B=[4,5,6]
print(A+B)

def getFirst(list):
   print(list[0])

def getSecond(list):
  print(list[1])

nilai_mhs= np.array([7,8,9,9,7,9,8,9,10,3,5])
print(nilai_mhs[1], nilai_mhs[4])

getFirst(nilai_mhs)
getSecond(nilai_mhs)


nama =input("Masukan nama anda ")
NIM = int(input("Masukan NIM anda "))

print(f"nama saya {nama}")
print(f"nim saya {NIM}")

A= int (input("masukan angka "))
B= int (input("masukan angka "))

if A>B: 
  print(" A lebih dari B")

else: 
  print(" B lebiih kecil dari A")

