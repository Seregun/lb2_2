n = int(input("Введите кол-во школьников: "))
k = int(input("Введите кол-во яблок: "))
apples_to_pupils = k//n
apples_left = k%n12
print("Кол-во яблок для каждого школьника: ", apples_to_pupils)
print("Кол-во яблок осталось: ", apples_left)