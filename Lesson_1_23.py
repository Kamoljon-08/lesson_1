import os

if os.path.exists("lesson_1/Lesson_1_23/tesla.text"):
    print("Bunday file mavjud")

else: 
    print("Bunday file mavjud emas")

papka = open("lesson_1/Lesson_1_23/tesla.text", "w")
papka_list = "olma, anor, nok, shaftoli, banan"
print(papka.write(papka_list))
papka.close()

papka_2 = open("lesson_1/Lesson_1_23/tesla.text", "r")
print(papka_2.read(20))
papka_2.close()

if os.path.exists("Lesson_1/Lesson_1_23/fayl_nomi.txt"):
    os.text("Lesson_1/Lesson_1_23/fayl_nomi.txt")
else:
    print("Bunday fayl mavjud emas")

papka_3 = open("Lesson_1/Lesson_1_23/fayl_nomi.txt", "w")
papka_list = "olma, anor, nok, shaftoli, banan"
print(papka_3.write(papka_list))
papka_3.close()

# x = 1

# try:
#  print(x)
# except:
#  print("x o'zgaruvchi mavjud emas")
