sentence = input("Skriv en mening: ")
new_sentence = ""
for letter in sentence:
   
    if letter.lower() == "ö":
        new_sentence += "o"
    elif letter.lower() == "ä":
        new_sentence += "a"
    elif letter.lower() == "å":
        new_sentence+= "o"
    else:
        new_sentence += letter

print(new_sentence)