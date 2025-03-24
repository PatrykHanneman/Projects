def calculator():
    print("Prosty kalkulator")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    
    choice = input("Podaj numer operacji (1/2/3/4): ") #wybór działania przez użytkownika
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj druga liczbę: "))
        
        if choice == '1':
            print(f"Wynik: {num1 + num2}")
        elif choice == '2':
            print(f"Wynik: {num1 - num2}")
        elif choice == '3':
            print(f"Wynik: {num1 * num2}")
        elif choice == '4':
            try:
                print(f"Wynik: {num1 / num2}")
            except ZeroDivisionError: #obsługa wyjątku przy dzieleniu przez 0
                print("Błąd: Nie można dzielić przez zero!")
    else:
        print("Nieprawidłowy wybór!") #użytkownik podał znak poza zakresem
# uruchomienie programu
if __name__ == "__main__":
    calculator()
