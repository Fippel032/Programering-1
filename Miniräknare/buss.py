
print("Hur gammal är du")

age = input()
age = int(age)

if age < 6:
    print("Bussbiljett för små barn kostar 0kr")

elif age >= 7 and age < 19:
    print("Bussbiljett för barn kostar 21kr")

elif age >= 20 and age < 64:
    print("Bussbiljett för vuxen kostar 32kr")

elif age >= 65 and age < 130:
    print("Bussbiljett för pensionärer kostar 21kr")


print("Vill du köpa årskort för endast 1000kr")

yes=input()

if yes=="ja":
    print("Tack så mycket")

else:
    print("Fuck you då!!")

    

