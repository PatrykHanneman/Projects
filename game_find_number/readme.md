# Gra "Zgadnij Liczbę"

## Opis projektu

Gra "Zgadnij Liczbę" to prosta aplikacja stworzona w języku Python, która pozwala użytkownikowi na zgadywanie losowej liczby w przedziale od 1 do 100.
Gra przechowuje dane o imieniu gracza oraz liczbie prób, jakie były potrzebne, aby odgadnąć liczbę. 
Wyniki są zapisywane do pliku CSV, a następnie są wizualizowane za pomocą wykresu słupkowego w Jupyter Notebook.

## Funkcje

- **Zgadnij liczbę**: Gracz wpisuje liczbę, a aplikacja informuje, czy jest ona za mała, za duża, czy trafiona.
- **Licznik prób**: Aplikacja śledzi liczbę prób gracza.
- **Zapis wyników**: Imię gracza oraz liczba prób są zapisywane do pliku CSV.
- **Wizualizacja wyników**: Zebrane wyniki można wizualizować za pomocą wykresu słupkowego, który pokazuje liczbę prób dla każdego gracza oraz średnią liczbę prób.

## Instalacja

### Wymagania

Do uruchomienia projektu wymagane są następujące biblioteki:
- `tkinter` (standardowa biblioteka Pythona dla interfejsów graficznych)
- `pandas` (do pracy z danymi i zapisywania wyników)
- `matplotlib` (do wizualizacji wyników)
- `seaborn` (do tworzenia estetycznych wykresów)

Możesz zainstalować wymagane biblioteki za pomocą poniższych poleceń:

```bash
pip install pandas matplotlib seaborn