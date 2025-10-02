print("Hej hej vad vill du köpa?")
print("Vi har glass,varmkorv,läsk och godis")
print("Glass 20kr")
print("Varmkorv är 15kr")
print("Läsk är 15kr")
print("Godis är 10kr")

svar = input("Vad vill du köpa? ")

if svar == "varmkorv":
    antal = int(input("Hur många vill du ha? "))
    
    if antal >= 10:
        print("Det är för många!")
    else:
        pris = 15 * antal
        print(f"Det blir {pris}kr")

if svar == "glass":
    antal = int(input("Hur många vill du ha? "))
    
    if antal >= 10:
        print("Det är för många!")
    else:
        pris = 20 * antal
        print("Det blir {pris}kr")


if svar == "läsk":
    antal = int(input("Hur många vill du ha? "))
    
    if antal >= 10:
        print("Det är för många!")
    else:
        pris = 15 * antal
        print(f"Det blir {pris}kr")

if svar == "godis":
    antal = int(input("Hur många vill du ha? "))
    
    if antal >= 10:
        print("Det är för många!")
    else:
        pris = 10 * antal
        print(f"Det blir {pris}kr")

print("Har du en rabattkod?")

rabatt=5

yes = input()

if yes=="ja":
    print(f"De nya priset är {pris-rabatt}")



   



