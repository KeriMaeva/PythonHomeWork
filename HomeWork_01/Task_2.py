# 2*. Напишите программу для
# проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

flag = True
for X in (0, 1):
    for Y in (0, 1):
        for Z in (0, 1):
            f = not (X or Y or Z) == (not X and not Y and not Z)
            if f == False:
                flag = False
            print(X, Y, Z, f)
if flag:
    print('Доказано')
else:
    print('Нет, не всех случаях')
