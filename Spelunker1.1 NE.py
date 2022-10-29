# import
import random
from colorama import Fore
import os

# Variables
links = ["Ga naar links", "ga naar links", "Ga Links", "ga links", "Links", "links", "L", "l"]
rechts = ["Ga naar rechts", "ga naar rechts", "Ga rechts", "ga rechts", "Rechts", "rechts", "R", "r"]
tent = ["Ga naar de tent", "ga naar de tent", "Ga naar tent", "ga naar tent", "Naar tent", "naar tent", "De tent", 
"de tent" "Ga tent", "ga tent", "Tent", "tent"]
gang = ["Ga naar de gang", "ga naar de gang", "Ga naar gang", "ga naar gang", "Naar gang", "naar gang", "De gang", 
"de gang", "Ga gang", "ga gang", "Gang", "gang"]
steen = ["Ga naar de steen", "ga naar de steen", "Ga naar steen", "ga naar steen", "Naar steen", "naar steen", "De steen", 
"de steen" "Ga steen", "ga steen", "Steen", "steen"]
terug = ["Ga terug", "ga terug", "Terug", "terug"]
mijnkar = ["Ga naar de mijnkar", "ga naar de mijnkar", "Ga naar mijnkar", "ga naar mijnkar", "Naar mijnkar", 
"naar mijnkar", "De mijnkar", "de mijnkar", "Ga mijnkar", "ga mijnkar", "Mijnkar", "mijnkar"]

sleutel = random.randint(1,2)
goud = random.randint(1,3)
instorting = random.randint(1,3)
doodgang = random.randint(1,2)
sleutelcheck = False
goudcheck = False

# Main Code

    #1e rij
def r1():
    print(Fore.CYAN)
    print("Welkom bij Spelunker.")
    print(Fore.RESET)
    print("Je staat voor de ingang van een grote grot.")
    print("Je denkt dat het wel grappig is om naar binnen te gaan.")
    print("Je gaat naar binnen en loopt door de donkere gang van de grot.")
    print("Het wordt zo donker dat je je zaklamp erbij pakt.")
    print("Na een lange tijd lopen kom je bij je eerste keuze.")
    print("")
    print("Het pad splitst in twee wegen.")
    print("Het linker pad buigt met een bocht naar rechts en is erg donker.")
    print("Het rechter pad is een recht pad dat naar een grote ruimte leidt waar licht vandaan komt.")
    print(Fore.YELLOW)
    print("Ga je naar links of naar rechts?")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in links:
        print(Fore.BLUE)
        print("Je loopt de donkere gang in.")
        print(Fore.RESET)
        r2a()
    elif choice in rechts:
        print(Fore.BLUE)
        print("Je loopt de gang in.")
        print(Fore.RESET)
        r2b()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r1()

    #2e rij
def r2a():
    print("Aan het eind van de gang heb je twee keuzes.")
    print("Aan de linkerkant loopt een tunnel die naar een grote ruimte leidt.")
    print("Aan de rechterkant loopt een smal donker gangetje dat naar links buigt.")
    print(Fore.YELLOW)
    print("Ga je naar links of naar rechts?")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in links:
        print(Fore.BLUE)
        print("Je loopt naar de grote ruimte.")
        print(Fore.RESET)
        r3a()
    elif choice in rechts:
        print(Fore.BLUE)
        print("Je gaat het smalle donkere gangetje in.")
        print(Fore.RESET)
        r3b()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r2a()

def r2b():
    print("Je gaat de kamer in.")
    print("In het midden staat een kampvuurtje.")
    print("Er staat een tent in de hoek van de kamer.")
    print("Er gaat een klein gangetje in een andere hoek van de kamer die verder de grot in lijkt te gaan.")
    print(Fore.YELLOW)
    print("Ga je naar de gang of ga je naar de tent?")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in tent:
        print(Fore.BLUE)
        print("Je loopt naar de tent.")
        print(Fore.RESET)
        r3d()
    elif choice in gang:
        print(Fore.BLUE)
        print("Je loopt de gang in.")
        print(Fore.RESET)
        r3c()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r2b()

    #3e rij
def r3a():
    print("Je staat in de grote ruimte en kijkt om je heen.")
    print("Aan de linkerkant loopt een klein gangetje.")
    print("Aan de rechterkant loopt een grotere gang die is ondersteund door houten palen.")
    print("Ook staat er een grote steen in het midden van de kamer.")
    print(Fore.YELLOW)
    print("Ga je naar links, rechts of naar de steen?")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in links:
        print(Fore.BLUE)
        print("Je loopt het gangetje in.")
        print(Fore.RESET)
        r4b()
    elif choice in rechts:
        print(Fore.BLUE)
        print("Je loopt de gang in.")
        print(Fore.RESET)
        r4c()
    elif choice in steen:
        print(Fore.BLUE)
        print("Je loopt naar de steen.")
        print(Fore.RESET)
        r4a()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r3a()

def r3b():
    global sleutelcheck
    print("Het kleine gangetje kom uit in een klein doodlopend kamertje.")
    print("In het kamertje staan een houten kist.")
    print("Je loopt naar de kist en doet hem open.")
    if sleutel == 1:
        print("In de kist ligt een klein sleuteltje.")
        print("Je stopt de sleutel in je zak.")
        print("Waar zou de sleutel voor zijn?")
        sleutelcheck = True
        print(Fore.YELLOW)
        print("Type 'ga terug' om weer terug te gaan.")
        print(Fore.GREEN)
        choice = input(">>> ")
        if choice in terug:
            print(Fore.BLUE)
            print("Je loopt weer terug naar waar je vandaan kwam.")
            print(Fore.RESET)
            r2a()
        else:
            print(Fore.RED)
            print("Verkeerde input.")
            print(Fore.RESET)
            r3b()
    elif sleutel == 2:
        print("In de kist zit helemaal niks.")
        print(Fore.YELLOW)
        print("Type 'ga terug' om weer terug te gaan.")
        print(Fore.GREEN)
        choice = input(">>> ")
        print(Fore.RESET)
        if choice in terug:
            print(Fore.BLUE)
            print("Teleurgesteld loop je weer terug naar waar je vandaan kwam.")
            print(Fore.RESET)
            r2a()
        else:
            print(Fore.RED)
            print("Verkeerde input.")
            print(Fore.RESET)
            r3b()

def r3c():
    print("Aan het eind van de gang heb je twee keuzes.")
    print("Aan de linkerkant loopt een grote gang die is ondersteund door houten palen.")
    print("Aan de rechterkant loopt een kleiner gangetje dat naar links afbuigt.")
    print(Fore.YELLOW)
    print("Ga je naar links of naar rechts?")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in links:
        print(Fore.BLUE)
        print("Je loopt door de grote gang.")
        print(Fore.RESET)
        r4c()
    elif choice in rechts:
        print(Fore.BLUE)
        print("Je gaat het smalle gangetje in.")
        print(Fore.RESET)
        r4d()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r3c()

def r3d():
    global sleutelcheck
    print("In de tent ligt een luchtbedje en een klein nachtkastje.")
    if sleutel == 2:
        print("Je opent het nachtkastje.")
        print("In het nachtkastje ligt een klein sleuteltje.")
        print("Je stopt de sleutel in je zak.")
        print("Waar zou de sleutel voor zijn?")
        sleutelcheck = True
        print(Fore.YELLOW)
        print("Type 'ga terug' om weer terug te gaan.")
        print(Fore.GREEN)
        choice = input(">>> ")
        if choice in terug:
            print(Fore.BLUE)
            print("Je stapt weer de tent uit.")
            print(Fore.RESET)
            r2b()
        else:
            print(Fore.RED)
            print("Verkeerde input")
            print(Fore.RESET)
            r3d()
    elif sleutel == 1:
        print("In het nachtkastje zit helemaal niks.")
        print(Fore.YELLOW)
        print("Type 'ga terug' om weer terug te gaan.")
        print(Fore.GREEN)
        choice = input(">>> ")
        if choice in terug:
            print(Fore.BLUE)
            print("Teleurgesteld stap je weer de tent uit.")
            print(Fore.RESET)
            r2b()
        else:
            print(Fore.RED)
            print("Verkeerde input.")
            print(Fore.RESET)
            r3b()
#4e rij
def r4a():
    print("Op de steen staat met grote letters goudmijn.")
    print("Onder de grote letters staan kleinere letters met een hele hoop namen.")
    print("Waarschijnlijk van de mensen die hier gewerkt hebben.")
    print(Fore.YELLOW)
    print("Type 'ga terug' om weer terug te gaan.")
    print(Fore.GREEN)
    choice = input(">>> ")
    print(Fore.RESET)
    if choice in terug:
        print(Fore.BLUE)
        print("Je loopt weer terug naar waar je vandaan kwam.")
        print(Fore.RESET)
        r3a()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r4a()

def r4b():
    if instorting <= 2:
        print("Het gangetje loopt dood en er is niks te vinden.")
        print(Fore.YELLOW)
        print("Type 'ga terug' om weer terug te gaan.")
        print(Fore.GREEN)
        choice = input(">>> ")
        if choice in terug:
            print(Fore.BLUE)
            print("Je loopt weer terug naar waar je vandaan kwam.")
            print(Fore.RESET)
            r3a()
        else:
            print(Fore.RED)
            print("Verkeerde input.")
            print(Fore.RESET)
            r4b()
    elif instorting == 3:
        print("Het gangetje loopt dood en er is niks te vinden.")
        print(Fore.YELLOW)
        print("Type 'ga terug' om weer terug te gaan.")
        print(Fore.GREEN)
        choice = input(">>> ")
        if choice in terug:
            print(Fore.BLUE)
            print("Je loopt weer terug naar waar je vandaan kwam.") 
            print(Fore.RESET)
            print("Voordat je terug kon lopen stort de grot voor je in.")
            print("Er liggen allemaal stenen in de weg en ze zijn te zwaar om te bewegen.")
            print("Je schreeuwt voor hulp maar niemand kan je horen.")
            print(Fore.MAGENTA)
            print("Einde 1")
            print(Fore.RESET)
            exit()
        else:
            print(Fore.RED)
            print("Verkeerde input.")
            print(Fore.RESET)
            r4b()

def r4c():
    print("Je komt in een grote kamer terecht.")
    print("Aan de linkerkant staan twee kleine hutjes.")
    print("Aan de rechterkant loopt een gang.")
    print("Ook staat er in de kamer een mijnkar.")
    print(Fore.YELLOW)
    print("Ga je naar links, rechts of naar de mijnkar.")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in links:
        print(Fore.BLUE)
        print("Je loopt naar de hutjes.")
        print(Fore.RESET)
        r5a()
    elif choice in rechts:
        print(Fore.BLUE)
        print("Je loopt naar de gang.")
        print(Fore.RESET)
        r5c()
    elif choice in mijnkar:
        print(Fore.BLUE)
        print("Je loopt naar de mijnkar.")
        print(Fore.RESET)
        r5b()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r3a()

def r4d():
    global goudcheck
    print("Aan het eind van de gang kom je een kistje tegen.")
    if goud == 2:
        print("Je opent het kistje en er zitten gouden munten in.")
        print("Wat een geluk!")
        goudcheck = True
    else:
        print("Je opent het kistje maar er zit niks in.")
        print("Wat een teleurstelling")
    print("")
    print("Aan de linkerkant loopt een rechte tunnen die naar een mijschacht lijkt te gaan.")
    print("Aan de rechterkant loopt een klein gangetje dat naar links buigt.")
    print(Fore.YELLOW)
    print("Ga je naar links of naar rechts?")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in links:
        print(Fore.BLUE)
        print("Je loopt door de gang die is ondersteund door houten balken.")
        print(Fore.RESET)
        r5c()
    elif choice in rechts:
        print(Fore.BLUE)
        print("Je gaat het gangetje in.")
        print(Fore.RESET)
        r5d()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r4d()

    #5e rij
def r5a():
    print("Je bekijkt de hutjes.")
    print("het linker hutje is op slot.")
    if sleutelcheck == True:
        print("Gelukkig heb je de sleutel gevonden.")
    else:
        print("Zonder sleutel kun je deze deur helaas niet openen.")
    print("Het rechter hutje staat open en er schijnt licht binnen.")
    print(Fore.YELLOW)
    print("Ga je naar links, rechts of ga je terug naar waar je vandaan kwam.")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in links:
        if sleutelcheck == True:
            print(Fore.BLUE)
            print("Je loopt het linker hutje in.")
            print(Fore.RESET)
            r6a()
        else:
            print(Fore.RED)
            print("Je kan hier niet naar binnen.")
            print(Fore.RESET)
            r5a()
    elif choice in rechts:
        print(Fore.BLUE)
        print("Je loopt het rechter hutje in.")
        print(Fore.RESET)
        r6b()
    elif choice in terug:
        print(Fore.BLUE)
        print("Je gaat terug naar waar je vandaan kwam.")
        print(Fore.RESET)
        r4c()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r5a()

def r5b():
    global goudcheck
    print("Je kijkt in de mijnkar.")
    if goud == 1:
        print("In de mijnkar zitten gouden munten.")
        print("Wat een geluk!")
        goudcheck = True
    else:
        print("Helaas zit er helemaal niks in.")
    print(Fore.YELLOW)
    print("Type 'ga terug' om weer terug te gaan.")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in terug:
        print(Fore.BLUE)
        print("Je loopt weer terug naar waar je vandaan kwam.")
        print(Fore.RESET)
        r4c()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r5b()

def r5c():
    print("Aan het eind van de gang kom je in een kleine kamer terecht met een bordje.")
    print("Op het bordje staat mijnschacht geschreven.")
    print("Als je om je heen kijkt zie je twee gangen die waarschijnlijk zijn gegraven door mijnwerkers.")
    print("Aan de linkerkant loopt een gang met een bocht naar rechts.")
    print("Aan de rechterkant loopt een gang met een bocht naar links.")
    print(Fore.YELLOW)
    print("Ga je naar links of naar rechts?")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in links:
        print(Fore.BLUE)
        print("Je loopt door de gang.")
        print(Fore.RESET)
        r6c()
    elif choice in rechts:
        print(Fore.BLUE)
        print("Je gaat de gang in richting de andere kamer.")
        print(Fore.RESET)
        r6d()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r5c()
    
def r5d():
    print("Aan het eind van het gangetje kom je een oude man tegen.")
    print("De man schreeuwt naar je: 'wat kom je hier doen!'")
    print("Je antwoord met weet ik eigenlijk niet")
    print("De man vertelt je weg te gaan en kijkt je heel boos aan.")
    print("Zonder enige aarzeling loop je de grot weer uit.")
    print(Fore.MAGENTA)
    print("Einde 2")
    print(Fore.RESET)
    exit()

    #6e rij
def r6a():
    print("Het huis is erg vervallen van binnen.")
    print("Er staat een oude openhaard met daar boven een bordje.")
    print("Op het bordje staat mr. Krasser.")
    print("Meneer Krasser was waarschijnlijk de eigenaar van het huis.")
    print(Fore.YELLOW)
    print("Type 'ga terug' om weer terug te gaan.")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in terug:
        print(Fore.BLUE)
        print("Je loopt weer terug naar waar je vandaan kwam.")
        print(Fore.RESET)
        r5a()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r6a()

def r6b():
    print("In het huis staat een bank, TV en een grote kast.")
    print("Op de grote kast staat een foto van een oude man.")
    print("Dit huis lijkt op het moment nog steeds leefbaar te zijn.")
    print(Fore.YELLOW)
    print("Type 'ga terug' om weer terug te gaan.")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in terug:
        print(Fore.BLUE)
        print("Je loopt weer terug naar waar je vandaan kwam.")
        print(Fore.RESET)
        r5a()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r6b()

def r6c():
    if doodgang == 1:
        print("Aan het eind van het gangetje is een lege kamer.")
        print("Dat is jammer.")
        print(Fore.YELLOW)
        print("Type 'ga terug' om weer terug te gaan.")
        print(Fore.GREEN)
        choice = input(">>> ")
        if choice in terug:
            print(Fore.BLUE)
            print("Je loopt weer terug naar waar je vandaan kwam.")
            print(Fore.RESET)
            r5c()
        else:
            print(Fore.RED)
            print("Verkeerde input.")
            print(Fore.RESET)
            r6c()
    elif doodgang == 2:
        print("Je komt in een kamer terecht waar je twee keuzes hebt.")    
        print("Links loopt een gang waar mysterieus gefluit vandaan komt.")
        print("Rechts loopt een donkere kleine gang die naar links afbuigt.")
        print(Fore.YELLOW)
        print("Ga je naar links of naar rechts?")
        print(Fore.GREEN)
        choice = input(">>> ")
        if choice in links:
            print(Fore.BLUE)
            print("Je loopt door de grote gang.")
            print(Fore.RESET)
            r7a()
        elif choice in rechts:
            print(Fore.BLUE)
            print("Je gaat het smalle gangetje in.")
            print(Fore.RESET)
            r7b()
        else:
            print(Fore.RED)
            print("Verkeerde input.")
            print(Fore.RESET)
            r6c()

def r6d():
    if doodgang == 2:
        print("Aan het eind van het gangetje is een lege kamer.")
        print("Dat is jammer.")
        print(Fore.YELLOW)
        print("Type 'ga terug' om weer terug te gaan.")
        print(Fore.GREEN)
        choice = input(">>> ")
        if choice in terug:
            print(Fore.BLUE)
            print("Je loopt weer terug naar waar je vandaan kwam.")
            print(Fore.RESET)
            r5c()
        else:
            print(Fore.RED)
            print("Verkeerde input.")
            print(Fore.RESET)
            r6d()
    elif doodgang == 1:
        print("Je komt in een kamer terecht waar je twee keuzes hebt.")    
        print("links loopt een gang waar mysterieus gefluit vandaan komt.")
        print("Rechts loopt een donkere kleine gang die naar links afbuigt.")
        print(Fore.YELLOW)
        print("Ga je naar links of naar rechts?")
        print(Fore.GREEN)
        choice = input(">>> ")
        if choice in links:
            print(Fore.BLUE)
            print("Je loopt door de grote gang.")
            print(Fore.RESET)
            r7a()
        elif choice in rechts:
            print(Fore.BLUE)
            print("Je gaat het smalle gangetje in.")
            print(Fore.RESET)
            r7b()
        else:
            print(Fore.RED)
            print("Verkeerde input.")
            print(Fore.RESET)
            r6c()

    #7e rij
def r7a():
    print("Als je door de gang bent gelopen zie je een bewaker.")
    print("Je probeert voorbij de bewaker te lopen.")
    print("Voordat je ook maar een stap kon zetten schreeuwt de bewaker halt!")
    print("Je stopt en kijkt de bewaker aan.")
    print("De bewaker vertelt je dat je alleen door mag lopen als je hem gouden munten geeft.")
    if goudcheck == True:
        print(Fore.BLUE)
        print("Je geeft de bewaker het geld en loopt voorbij de bewaker.")
        print(Fore.RESET)
        r8()
    else:
        print("Je vertelt de bewaker dat je geen gouden munten hebt.")
        print("De bewaker kijkt je aan en vertelt je om dan maar weg te gaan.")
        print("Je loopt teleurgesteld weer de grot uit.")
        print(Fore.MAGENTA)
        print("Einde 3")
        print(Fore.RESET)
        exit()
        
def r7b():
    global goudcheck
    print("Aan het eind van de kom je een kistje tegen.")
    if goud == 3:
        print("Je opent het kistje en er zitten gouden munten in.")
        print("Wat een geluk!")
        goudcheck = True
    else:
        print("Je opent het kistje maar er zit niks in.")
        print("Wat een teleurstelling.")
        print("")
    print("Er gaat een klein gangetje naar links waar ook het mysterieuse gefluit vandaan komt.")
    print("Type 'ga naar de gang' om door te gaan.")
    print(Fore.GREEN)
    choice = input(">>> ")
    if choice in gang:
        print(Fore.BLUE)
        print("Je loopt op het gefluit af.")
        print(Fore.RESET)
        r7a()
    else:
        print(Fore.RED)
        print("Verkeerde input.")
        print(Fore.RESET)
        r7b()

    #8e rij
def r8():
    print("Nu je voorbij de bewaker bent gekomen kom je bij een grote stenen deur waar je een sleutel voor nodig hebt.")
    if sleutelcheck == True:
        print("Je pakt je sleutel en opent de deur.")
        print("De deur gaat open en er komt een verblindend licht naar binnen.")
        print("De grot blijkt gewoon een shortcut te zijn door de berg.")
        print("Was dit het ontdekken wel waard?")
        print(Fore.MAGENTA)
        print("Einde 5")
        print(Fore.RESET)
        exit()
    else:
        print("Je probeert de deur te openen maar het lukt niet.")
        print("Je loopt teleurgesteld weer de grot uit.")
        print(Fore.MAGENTA)
        print("Einde 4")
        print(Fore.RESET)
        exit()


    #opstarten
os.system("cls")
r1()