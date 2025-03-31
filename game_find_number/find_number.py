import tkinter as tk
import random
import csv
import os

# Ścieżka do pliku wyników
FILE_PATH = os.path.join(os.getcwd(), "game_find_number", "wyniki.csv")

def save_score(name, attempts):
    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, attempts])

def load_leaderboard():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        reader = csv.reader(file)
        scores = sorted([(row[0], int(row[1])) for row in reader], key=lambda x: x[1])
    return scores[:10]  # Zwroc 10 najlepszych wyników

def show_leaderboard():
    leaderboard_window = tk.Toplevel(root)
    leaderboard_window.title("Top 10 Leaderboard")
    leaderboard_window.geometry("250x250")
    
    tk.Label(leaderboard_window, text="Top 10", font=("Arial", 12, "bold")).pack()
    leaderboard = load_leaderboard()
    
    for i, (name, attempts) in enumerate(leaderboard, start=1):
        tk.Label(leaderboard_window, text=f"{i}. {name}: {attempts} times").pack()

def reset_game():
    global number_to_guess, attempts, leaderboard_button
    number_to_guess = random.randint(1, 100)
    attempts = 0
    result_label.config(text="Zgadnij liczbę od 1 do 100")
    attempts_label.config(text="Liczba prób: 0")
    entry.delete(0, tk.END)
    check_button.config(state=tk.NORMAL)
    if leaderboard_button:
        leaderboard_button.pack_forget()  # Ukrywa przycisk, jeśli istnieje

def check_guess(event=None):
    global attempts, leaderboard_button
    try:
        guess = int(entry.get())
        attempts += 1
        attempts_label.config(text=f"Liczba prób: {attempts}")
        if guess < number_to_guess:
            result_label.config(text="Za mało! Spróbuj ponownie.")
        elif guess > number_to_guess:
            result_label.config(text="Za dużo! Spróbuj ponownie.")
        else:
            result_label.config(text=f"Gratulacje! Odgadłeś liczbę w {attempts} próbach!")
            check_button.config(state=tk.DISABLED)
            save_score(user_name, attempts)
            leaderboard_button = tk.Button(root, text="Leaderboards", command=show_leaderboard)
            leaderboard_button.pack()
    except ValueError:
        result_label.config(text="Wpisz poprawną liczbę!")

def ask_name():
    def save_name():
        global user_name
        user_name = name_entry.get()
        name_window.destroy()
        root.deiconify()
    
    name_window = tk.Toplevel(root)
    name_window.title("Podaj swoje imię")
    name_window.geometry("150x100")
    tk.Label(name_window, text="Podaj swoje imię:").pack()
    name_entry = tk.Entry(name_window)
    name_entry.pack()
    tk.Button(name_window, text="OK", command=save_name).pack()

root = tk.Tk()
root.title("Zgadnij Liczbę")
root.geometry("250x200")
root.withdraw()
ask_name()

number_to_guess = random.randint(1, 100)
attempts = 0
leaderboard_button = None

# UI
label = tk.Label(root, text="Wpisz liczbę:")
label.pack()
entry = tk.Entry(root)
entry.pack()
entry.bind("<Return>", check_guess)  # Obsługa Entera
check_button = tk.Button(root, text="Sprawdź", command=check_guess)
check_button.pack()
result_label = tk.Label(root, text="Zgadnij liczbę od 1 do 100")
result_label.pack()
attempts_label = tk.Label(root, text="Liczba prób: 0")
attempts_label.pack()
reset_button = tk.Button(root, text="Nowa gra", command=reset_game)
reset_button.pack()

# Zatrzymanie okna gry na wierzchu
root.lift()
root.attributes("-topmost", True)
root.after_idle(root.attributes, "-topmost", False)

root.mainloop()
