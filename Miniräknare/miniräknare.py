
def addera(x, y):
    return x + y

def gånger(x, y):
    return x * y

def delat(x, y):
    if y == 0:
        return "Fel: Division med noll!"
    return x / y

def minus(x, y):
    return x - y


while True:
    print("Vilka tal ska jag räkna?")
    number_1 = float(input("Första talet: "))
    number_2 = float(input("Andra talet: "))

    print("Vad vill du göra med", number_1, "och", number_2)
    print("1 +, 2 -, 3 /, 4 *")

    number = input("Välj operation 1-4: ")

    if number == "1":
        print("Resultat:",round(addera(number_1,number_2),2))
    elif number == "2":
        print("Resultat:",round(minus(number_1,number_2 ),2))
    elif number == "3":
        print("Resultat:",round(delat(number_1,number_2),2))
    elif number == "4":
        print("Resultat:",round(gånger(number_1,number_2),2))
    else:
        print("Fel: Ogiltigt svar!")
 
   


        
