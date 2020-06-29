#Создание сценария, вычисляющего операции сложения, вычитания, умножения, деления для двух операндов.

while True:
    s = input("Знак операции (+,-,*,/): ")
    if s in ('+','-','*','/'):
        x = float(input("x = "))
        y = float(input("y = "))
        if s == '+':
            print("%.2f" % (x + y))
        elif s == '-':
            print("%.2f" % (x - y))
        elif s == '*':
            print("%.2f" % (x * y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
