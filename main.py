from colorama import Fore

mode = "Menu"
modes = ("Menu", "Length", "Speed", "Mass", "Temperature")

lengthNum = (0.001, 0.01, 1, 1000, 0.0254, 0.3048, 1609.344, 0.9144)
lengthName = ("Millimeter", "Centimeter", "Meter", "Kilometer", "Tommer", "Fod", "Mil", "Yard")
speedNum = (1, 0.0002777778, 1000, 0.2777778, 0.3048, 0.0000846667, 1609.344, 0.44704, 0.5144444444)
speedName = ("Meter i Sekundt", "Meter i Timen", "Kilometer i Sekundet", "Kilometer i Timen", "Fod i Sekundet", "Fod i Timen", "Mil i Sekundet", "Mil i Timen", "Knob")
massNum = (0.001, 1, 1000, 0.45359237, 0.0283495231)
massName = ("Gram", "Kilogram", "Ton", "Pund", "Ounce")
temperatureName = ("Celcius", "Fahrenheit", "Kelvin")

def update():
    if mode == "Menu":
        menu()
    elif mode == "Length":
        length()
    elif mode == "Speed":
        speed()
    elif mode == "Mass":
        mass()
    elif mode == "Temperature":
        temperature()

def menu():
    global mode
    global modes
    print(Fore.BLUE + "----------------------------------------")
    print(Fore.GREEN + "Vælg hvilke konventering du ville lave" + Fore.WHITE)
    print(Fore.YELLOW + "1. " + Fore.WHITE + "Længde")
    print(Fore.YELLOW + "2. " + Fore.WHITE + "Hastighed")
    print(Fore.YELLOW + "3. " + Fore.WHITE + "Masse")
    print(Fore.YELLOW + "4. " + Fore.WHITE + "Temperatur")
    print("")

    choice = int(input("Indtast dit svar: "))

    if choice >= 0 and choice <= 4:
        mode = modes[choice]
        update()
    else:
        print(Fore.RED + "INDTAST VENLIGST ET GYLDIGT NUMMER!")

def convertLength(aa, bb, xx):
    global lengthNum
    a = lengthNum[aa-1]
    b = 1/lengthNum[bb-1]
    x = a*xx*b
    return x

def convertSpeed(aa, bb, xx):
    global speedNum
    a = speedNum[aa-1]
    b = 1/speedNum[bb-1]
    x = a*xx*b
    return x

def convertMass(aa, bb, xx):
    global massNum
    a = massNum[aa-1]
    b = 1/massNum[bb-1]
    x = a*xx*b
    return x

def convertTemperature(aa, bb, xx):
    if aa == bb:
        return xx
    elif aa == 1 and bb == 3:
        return xx+273.15
    elif aa == 3 and bb == 1:
        return xx-273.15
    elif aa == 2 and bb == 1:
        a = xx-32
        return a/1.8
    elif aa == 1 and bb == 2:
        a = xx*1.8
        return a+32
    elif aa == 2 and bb == 3:
        a = xx-32
        b = a/1.8
        return b + 273.15
    elif aa == 3 and bb == 2:
        a = xx-273.15
        b = a*1.8
        return b+32

def length():
    global lengthName
    global mode
    global modes
    print(Fore.BLUE + "----------------------------------------" + Fore.WHITE)
    print(Fore.GREEN + "Hvilken enhed ville du konventere" + Fore.WHITE)
    print(Fore.YELLOW + "0." + Fore.WHITE + " Tilbage")
    print(Fore.YELLOW + "1." + Fore.WHITE + " Millimeter")
    print(Fore.YELLOW + "2." + Fore.WHITE + " Centimeter")
    print(Fore.YELLOW + "3." + Fore.WHITE + " Meter")
    print(Fore.YELLOW + "4." + Fore.WHITE + " Kilometer")
    print(Fore.YELLOW + "5." + Fore.WHITE + " Tommer")
    print(Fore.YELLOW + "6." + Fore.WHITE + " Fod")
    print(Fore.YELLOW + "7." + Fore.WHITE + " Mil")
    print(Fore.YELLOW + "8." + Fore.WHITE + " Yard")
    print("")
    a = int(input(Fore.WHITE + "Indsæt første valg: " + Fore.CYAN))
    if a == 0:
        mode = modes[0]
        update()

    b = int(input(Fore.WHITE + "Indsæt næste valg: " + Fore.CYAN))
    if b == 0:
        mode = modes[0]
        update()
 
    x = float(input(Fore.WHITE + "Indsæt hvor meget der skal omregnes: " + Fore.CYAN))
    print("")
    print(Fore.GREEN + str(x) + Fore.WHITE + " " + lengthName[a-1] + " svare til " + Fore.GREEN + str(convertLength(a, b, x)) + Fore.WHITE + " " + lengthName[b-1])
    print("")
    if input("Tast" + Fore.GREEN + " 0" + Fore.WHITE + " for at komme til hovedmenuen: ") == "0":
        mode = modes[0]
        update()

def speed():
    global speedName
    global mode
    global modes
    print(Fore.BLUE + "----------------------------------------" + Fore.WHITE)
    print(Fore.GREEN + "Hvilken enhed ville du konventere" + Fore.WHITE)
    print(Fore.YELLOW + "0." + Fore.WHITE + " Tilbage")
    print(Fore.YELLOW + "1." + Fore.WHITE + " Meter i Sekundt")
    print(Fore.YELLOW + "2." + Fore.WHITE + " Meter i Timen")
    print(Fore.YELLOW + "3." + Fore.WHITE + " Kilometer i Sekundet")
    print(Fore.YELLOW + "4." + Fore.WHITE + " Kilometer i Timen")
    print(Fore.YELLOW + "5." + Fore.WHITE + " Fod i Sekundet")
    print(Fore.YELLOW + "6." + Fore.WHITE + " Fod i Timen")
    print(Fore.YELLOW + "7." + Fore.WHITE + " Mil i Sekundet")
    print(Fore.YELLOW + "8." + Fore.WHITE + " Mil i Timen")
    print(Fore.YELLOW + "9." + Fore.WHITE + " Knob")
    print("")
    a = int(input(Fore.WHITE + "Indsæt første valg: " + Fore.CYAN))
    if a == 0:
        mode = modes[0]
        update()

    b = int(input(Fore.WHITE + "Indsæt næste valg: " + Fore.CYAN))
    if b == 0:
        mode = modes[0]
        update()
 
    x = float(input(Fore.WHITE + "Indsæt hvor meget der skal omregnes: " + Fore.CYAN))
    print("")
    print(Fore.GREEN + str(x) + Fore.WHITE + " " + speedName[a-1] + " svare til " + Fore.GREEN + str(convertSpeed(a, b, x)) + Fore.WHITE + " " + speedName[b-1])
    print("")
    if input("Tast" + Fore.GREEN + " 0" + Fore.WHITE + " for at komme til hovedmenuen: ") == "0":
        mode = modes[0]
        update()

def mass():
    global massName
    global mode
    global modes
    print(Fore.BLUE + "----------------------------------------" + Fore.WHITE)
    print(Fore.GREEN + "Hvilken enhed ville du konventere" + Fore.WHITE)
    print(Fore.YELLOW + "0." + Fore.WHITE + " Tilbage")
    print(Fore.YELLOW + "1." + Fore.WHITE + " Gram")
    print(Fore.YELLOW + "2." + Fore.WHITE + " Kilogram")
    print(Fore.YELLOW + "3." + Fore.WHITE + " Ton")
    print(Fore.YELLOW + "4." + Fore.WHITE + " Pund")
    print(Fore.YELLOW + "5." + Fore.WHITE + " Ounce")
    print("")
    a = int(input(Fore.WHITE + "Indsæt første valg: " + Fore.CYAN))
    if a == 0:
        mode = modes[0]
        update()

    b = int(input(Fore.WHITE + "Indsæt næste valg: " + Fore.CYAN))
    if b == 0:
        mode = modes[0]
        update()
 
    x = float(input(Fore.WHITE + "Indsæt hvor meget der skal omregnes: " + Fore.CYAN))
    print("")
    print(Fore.GREEN + str(x) + Fore.WHITE + " " + massName[a-1] + " svare til " + Fore.GREEN + str(convertMass(a, b, x)) + Fore.WHITE + " " + massName[b-1])
    print("")
    if input("Tast" + Fore.GREEN + " 0" + Fore.WHITE + " for at komme til hovedmenuen: ") == "0":
        mode = modes[0]
        update()

def temperature():
    global temperatureName
    global mode
    global modes
    print(Fore.BLUE + "----------------------------------------" + Fore.WHITE)
    print(Fore.GREEN + "Hvilken enhed ville du konventere" + Fore.WHITE)
    print(Fore.YELLOW + "0." + Fore.WHITE + " Tilbage")
    print(Fore.YELLOW + "1." + Fore.WHITE + " Celcius")
    print(Fore.YELLOW + "2." + Fore.WHITE + " Fahrenheit")
    print(Fore.YELLOW + "3." + Fore.WHITE + " Kelvin")
    print("")
    a = int(input(Fore.WHITE + "Indsæt første valg: " + Fore.CYAN))
    if a == 0:
        mode = modes[0]
        update()

    b = int(input(Fore.WHITE + "Indsæt næste valg: " + Fore.CYAN))
    if b == 0:
        mode = modes[0]
        update()
 
    x = float(input(Fore.WHITE + "Indsæt hvor meget der skal omregnes: " + Fore.CYAN))
    print("")
    print(Fore.GREEN + str(x) + Fore.WHITE + " " + temperatureName[a-1] + " svare til " + Fore.GREEN + str(convertTemperature(a, b, x)) + Fore.WHITE + " " + temperatureName[b-1])
    print("")
    if input("Tast" + Fore.GREEN + " 0" + Fore.WHITE + " for at komme til hovedmenuen: ") == "0":
        mode = modes[0]
        update()

update()   