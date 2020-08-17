import random

cpu = random.randint(0,100)
counter = 0
print(cpu)

print("Merhaba 0-100 arası bir sayı tutunuz")
user = int(input(":"))

while not cpu == user:
  counter += 1
  if cpu > user: 
    user = int(input("Daha büyük bir değer girin: "))
  else:
    user = int(input("Daha küçük bir sayı girin: "))

basari = 100 - int(counter) * 10

print(f"Tebrikler! doğru tahmin: {cpu} ve puan: {basari}")
