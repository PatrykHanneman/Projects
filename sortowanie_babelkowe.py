import random #moduł potrzebny do wygenerowania losowych liczb
def bubble_sort(arr):
    """
    Funkcja implementujaca sortowanie babelkowe.
    Algorytm polega na wielokrotnym przechodzeniu przez liste i zamienianiu miejscami sasiednich elementow,
    jesli sa w zlej kolejnosci. Proces powtarza sie, az lista bedzie posortowana.

    """
    n = len(arr)  # przypisanie dlugosci listy do zmiennej n

    for i in range(n - 1):
        swapped = False  # Zmienna do sledzenia, czy nastapila zamiana elementow

        # Porownujemy sasiednie elementy i zamieniamy je, jesli sa w zlej kolejnosci
        for j in range(n - 1 - i):  # Z kazdym przebiegiem najwiekszy element "wyplywa" na koniec
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Zamiana elementów
                swapped = True  # Oznaczamy, że nastąpiła zamiana

        # Jeśli nie było zamiany w danym przebiegu, lista jest już posortowana
        if not swapped:
            break
    return arr  # Zwracamy posortowana liste

def random_list_generator(): #funkcja zwracajaca liste 15 losowych liczb z zakresu 0-100
    return [random.randint(0,100)for x in range(15)]

if __name__ == "__main__":
    numbers = random_list_generator()
    print("Lista przed sortowaniem:", numbers)
    sorted_numbers = bubble_sort(numbers)
    print("Lista po sortowaniu:", sorted_numbers)
