# Importeer functie 2 (opgave 12)
from algemene_functies import mijn_functie_2

# Functie aanbieding 1 (opgave 5)
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."

# Functie totaal inkomsten (opgave 7)
def inkomsten_totaal(inkomsten, btw_percentage):
    totaal = 0
    for dagomzet in inkomsten:
        totaal += dagomzet
    btw = totaal * btw_percentage
    return f"Het totaal van alle inkomsten deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden."

# Functie laagste en hoogste waarde (opgave 8)
def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

# Functie gemiddelde (opgave 9 en 10)
def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten van deze week zijn {bedrag:.2f} euro."

# Functie meervoudig - zet de twee elementen om in een list
def meervoudig(invoer_lijst):
    return list(laag_en_hoog(invoer_lijst))

# Combinatiefunctie aangepast n.a.v. opmerkingen docent
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2) # Hoogste en laatste waarde
    return mijn_functie_2(korte_lijst[0], korte_lijst[1]) # Geef som, verschil, product, quotient

# Test functies
print(aanbieding_1("aardbei",4,0.1)) # Opdracht 5
print(inkomsten_totaal([1,2,3,4,5,6,7],0.09)) # Opdracht 6 en 7
print(laag_en_hoog([1,2,3,4,5,6,7])) # Opdracht 8
print(gemiddelde([1,2,3,4,5,6,7])) # Opdracht 9 en 10
print(meervoudig([1,2,3,4,5,6,7])) # Opdracht 11
print(combinatie([1,2,3,4,5,6,7])) # Opdracht 12