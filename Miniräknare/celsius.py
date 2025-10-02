
print("skriv 1 om du vill skriva i celsius")
print("skriv 2 om du vill skriva i fahrenheit")

tal=input()

if tal=="1":
    print("Skriv tempraturen i fahrenheit")

    fahrenheit = float(input())



    resultat=fahrenheit/1.8-32
    print("Det blir",resultat,"grader celsius")

    

    
else:
    print("Skriv tempraturen i celsius")

    celsius = float(input())



    resultat=celsius*1.8+32
    print("Det blir",resultat,"grader fahrenheit")