from datetime import date
n = int(input("ano em que nasceste? "))
a = date.today().year - n
if a <= 17:
    print("Muito jovem!")
elif a <= 18:
    print("Hora do recensiamento")
else:
    print("Passou da hora")