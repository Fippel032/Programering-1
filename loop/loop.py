sentence = "Hej på dig"

for letter in sentence:
    print(letter)

for i in range(1, 11):
    print(i)
    
    if i == 5:
        continue

gambling = True

while gambling:
    print("$$$$$$")

    if input() == "stop":
        break


print("mata in ett nummer")


number_1 = input()

try:
     number_1 = int(number_1)
        
except:
    print("Försök igen")



word_1 = "hassan"

if "a" in word_1:
    print("Ja finns ")

else:
    print("Ned de finns inte")