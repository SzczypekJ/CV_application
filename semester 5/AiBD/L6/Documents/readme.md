## Analiza i Bazy Danych

**Laboratorium 6 - Exploratory Data Analysis**

Pierwszym zadaniem było wybranie swojego zbioru do analizy. Zbiór wybierało się na podstawie sumy liter w imieniu i nazwisku.
U mnie zbiorem, który analizowałem jest zbiór o nazwie "13_WARMIN╠üSKO-MAZURSKIE" (Jakub Szczypek - 13 liter). Następnie utworzyłem 4 foldery o nazwach:
- AnalysisData
- CommandFiles
- Documents
- OriginalData

---------------
**AnalysisData**

- W tym folderze znajduję się zmodyfikowany plik o nazwie "WARMIŃSKO_MAZURSKIE_BEZ_bd"
- Plik ten powstał z oryginalnego pliku "13_WARMIN╠üSKO-MAZURSKIE" poprzez usunięcie z niego wierszy z klientami, którzy nie mieli określonej płci (bd. - brak danych)
oraz przez usunięcie wierszy gdzie wiek klienta był "NaN"
- Dokładny opis tego pliku znajduje się pod lokalizacją: Documents/dataAppendix.md.

---------------
**CommandFiles**
- W tym folderze znajduję się notebook o nazwie "raport.ipynb".
- Notebook zawiera kod programu odpowiadający za usunięcie wierszy gdzie nie mamy określonej płci oraz wieku klienta.
- Zawiera także ogólne informacje o plikach "13_WARMIN╠üSKO-MAZURSKIE" i "WARMIŃSKO_MAZURSKIE_BEZ_bd".
- Są tam także wykresy przedstawiające: czas pomiędzy zakupem a wystawieniem oceny, wiek kupujących, średnie oceny marek ze względu na płeć, płeć kupujących, oceny danych marek.

---------------
**Documents**
- Folder ten zawiera plik "readme.md" z ogólnym opisem wszytkich folderów.
- Zawiera także plik o nazwie "dataAppendix.md" z opisem pliku po analizie.

---------------
**OriginalData**
- W tym folderze znajduje się oryginalny plik ze zbiorem danych do analizy "13_WARMIN╠üSKO-MAZURSKIE".
- Plik "13_WARMIN╠üSKO-MAZURSKIE" zawiera dane o klientach którzy zakupili dokurzacze z różnych firm.
- W tym folderze znajduje się też przewodnik po metadanych "Metadata_guide" z dokładnym opisem pliku "13_WARMIN╠üSKO-MAZURSKIE".
- Plik z tymi danymi jest w formacie o rozszerzeniu ".csv", więc jest on już importowalny i nie trzeba zmieniać jego rozszerzenia.