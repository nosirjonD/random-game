# random-game
import random
a=random.randrange(1,10)
print(a)

ism = 110
savol = "1dan 10gacha bo'lgan son kiriting:  "
 

while int(ism) !=int(a):
   ism= int(input(savol))
   if int(ism) < a:
      print("uzr biz yashirgan son sal kattaroq")
   elif  int(ism) > a:
      print("uzr biz yashirgan son sal kichikroq")
   else:
       print("siz biz yashirgan sonni topdingiz")
