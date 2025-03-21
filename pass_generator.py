import random
import string

# Funkcja generująca losowe hasło o podanej długości
def generate_password(length):
    #przypisanie zestawów znaków do zmiennej (litery,cyfry i znaki specjalne)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for x in range(length)) #generowanie hasła o dł. length
    return password

# Główna funkcja programu
def main():
    print("Generator haseł")
    
    try:
        length = int(input("Podaj długość hasła: "))
        amount = int(input("Ile haseł wygenerować?: "))

        for x in range(amount):
            print(generate_password(length))
    # Obsługa błędu w przypadku podania niepoprawnej wartości
    except ValueError:
        print("Błąd: Podaj poprawną liczbę!")


# Uruchomienie programu
if __name__ == "__main__":
    main()