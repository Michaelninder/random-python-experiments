import random

APP_title = """
░██╗░░░░░░░██╗██╗░░░██╗███████╗██████╗░███████╗███████╗██╗░░░░░
░██║░░██╗░░██║██║░░░██║██╔════╝██╔══██╗██╔════╝██╔════╝██║░░░░░
░╚██╗████╗██╔╝██║░░░██║█████╗░░██████╔╝█████╗░░█████╗░░██║░░░░░
░░████╔═████║░██║░░░██║██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░██║░░░░░
░░╚██╔╝░╚██╔╝░╚██████╔╝███████╗██║░░██║██║░░░░░███████╗███████╗
░░░╚═╝░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚══════╝"""

print("\n\n", APP_title, "\n\n\n\n")

ergebnisse = []
#runden = int(input("Wie oft soll gewürfelt werden? "))

#for runde in range(runden):
for runde in range(int(input("Wie oft soll gewürfelt werden? "))):
    ergebnis = random.choice(range(1, 6))
    ergebnisse.append(ergebnis)
    print(f"Wurf {runde + 1} ergab {ergebnis}")

print(f"\nErgebnisliste: {ergebnisse}\n")

durchschnitt_helper = 0
for ergebnis in ergebnisse:
    durchschnitt_helper += ergebnis
    
#durchschnitt = durchschnitt_helper / len(ergebnisse)
#print(f"Der Durchschnitt aus {len(ergebnisse)} Würfen ist {durchschnitt}")
print(f"Der Durchschnitt aus {len(ergebnisse)} Würfen ist {durchschnitt_helper / len(ergebnisse)}")
input("Drücke Enter, um das Fenster zu schließen")