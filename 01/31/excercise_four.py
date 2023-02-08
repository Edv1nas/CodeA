# Create program that allows user to enter text
# Convert that text to Leet speak 1337

text = input("Please enter somethink!")

for letter in text:
    if letter =="a":
        text = text.replace("a", "4")
    elif letter =="b":
        text = text.replace("b", "8")
    elif letter =="c":
        text = text.replace("c", "<")
    elif letter =="d":
        text = text.replace("d", "|)")
    elif letter =="e":
        text = text.replace("e", "3")
    elif letter =="f":
        text = text.replace("f", "|=")
    elif letter =="g":
        text = text.replace("g", "[")
    elif letter =="h":
        text = text.replace("h", "#")
    elif letter =="i":
        text = text.replace("i", "1")
    elif letter =="j":
        text = text.replace("j", "|_")
    elif letter =="k":
        text = text.replace("k", "|<")
    elif letter =="l":
        text = text.replace("l", "|")
    elif letter =="m":
        text = text.replace("m", "44")
    elif letter =="n":
        text = text.replace("n", "|\|")
    elif letter =="o":
        text = text.replace("o", "0")
    elif letter =="p":
        text = text.replace("p", "|O")
    elif letter =="r":
        text = text.replace("r", "|2")
    elif letter =="s":
        text = text.replace("s", "5")
    elif letter =="t":
        text = text.replace("t", "7")
    elif letter =="u":
        text = text.replace("u", "|_|")
    elif letter =="v":
        text = text.replace("v", "\/")
    elif letter =="w":
        text = text.replace("w", "\/\/")
    elif letter =="x":
        text = text.replace("x", "%")
    elif letter =="y":
        text = text.replace("y", "y")
    elif letter =="z":
        text = text.replace("z", "5")
    
    else:
            pass


print(text)