import random

def generuj_postac():
    postac = {
        "imie": random.choice(["Legolas", "Aragorn", "Gandalf", "Frodo"]),
        "rasa": random.choice(["Człowiek", "Czarodziej", "Elf", "Hobbit"]),
        "siła": random.randint(1, 20),
        "zręczność": random.randint(5, 15),
    }

    print("TWOJA POSTAĆ RPG")
    for klucz, wartosc in postac.items():
        print(f"{klucz.capitalize()}: {wartosc}")

if __name__ == "__main__":
    generuj_postac()
