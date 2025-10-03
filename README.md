
## PDF to Audiobook

Prosty projekt w Pythonie, który zamienia wybrany plik **PDF** na audiobooka w formacie **MP3** z wykorzystaniem biblioteki [gTTS](https://pypi.org/project/gTTS/).

---

## Funkcjonalności
- Wybór pliku PDF przez **okno dialogowe** (`tkinter.filedialog`).
- Odczyt tekstu z każdej strony PDF dzięki **PyPDF2**.
- Generowanie audiobooka w formacie **MP3**.
- Automatyczne odtworzenie gotowego pliku na Windows.

---

## Wymagania
- Python **3.10+** (testowane na 3.13)
- Biblioteki:
  ```bash
  pip install PyPDF2 gTTS
