import random

cpu1 = random.randint(0,10)
user1 = int(input("Bir sayı giriniz: "))
user= -1
counter= 0

def kiyas(user,cpu,counter=1):
  while not cpu == user:
    counter += 1
    if cpu < user:
      user = int(input("daha küçük bir değer giriniz: "))
     
    elif cpu > user:
      user = int(input("daha büyük bir değer giriniz: "))
      
  return user,counter
  


result = kiyas(user1,cpu1)

print("Tebrikler sonuc:",result[0],"Deneme:",result[1])

