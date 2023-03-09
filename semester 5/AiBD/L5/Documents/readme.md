## Analiza i Bazy Danych

**Laboratorium 5 - TIER protocol i Tidy data**

Pierwszym zadaniem było wybranie swojego zbioru do analizy. Zbiór wybierało się na podstawie wzoru (N mod 5) + 1, gdzie N to liczba liter w nazwisku.
U mnie zbiorem, który analizowałem był zbiór o nazwie "drinks.csv" (Szczypek: N = 8). Następnie utworzyłem 4 foldery o nazwach: 
-AnalysisData
-CommandFiles
-Documents
-OriginalData

---------------
**AnalysisData**

- W tym folderze znajduję się zmodyfikowany plik o nazwie "drinks_without_zero_consumption".
- Plik ten powstał z oryginalnego pliku "drinks.csv" poprzez usunięcie z niego wierszy z krajami o zerowym spożyciu alkoholu.
- Dokładny opis tego pliku znajduje się pod lokalizacją: Documents/dataAppendix.md.

---------------
**CommandFiles**
- W tym folderze znajduję się notebook o nazwie "raport.ipynb".
- Notebook zawiera kod programu odpowiadający za usunięcie wierszy gdzie spożycie alkoholu w danym kraju jest równe zero.
- Zawiera także ogólne informacje o plikach "drinks.csv" i "drinks_without_zero_consumption".
- Są tam także wykresy przedstawiające średnie spożycie danego alkholu, bądź wykresy pokazujące kraje z największym spożyciem danego trunku.

---------------
**Documents**
- Folder ten zawiera plik "readme.md" z ogólnym opisem wszytkich folderów.
- Zawiera także plik o nazwie "dataAppendix.md" z opisem pliku po analizie.

---------------
**OriginalData**
- W tym folderze znajduje się oryginalny plik ze zbiorem danych do analizy "drinks.csv".
- Plik "drinks.csv" zawiera dane o badaniu przeprowadzonym przez WHO dotyczącym spożycia różnych alkoholi w 193 krajach.
- W tym folderze znajduje się też przewodnik po metadanych "Metadata_guide" z dokładnym opisem pliku "drinks.csv".
- Plik z tymi danymi jest w formacie o rozszerzeniu ".csv", więc jest on już importowalny i nie trzeba zmieniać jego rozszerzenia.
