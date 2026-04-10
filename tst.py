import pandas as pd

file_path = "Data_Study_KEO_Analyzing_Complete.xlsx"

# =========================
# Einstellungen
# =========================
cols_letters = ["A", "B", "C", "D"]  # 👈 gewünschte Spalten
MAX_ROWS = 20  # 👈 Zeilenlimit

# =========================
# Helper: Excel Buchstabe → Index
# =========================
def col_letter_to_index(letter):
    letter = letter.upper()
    return ord(letter) - ord("A")

cols_idx = [col_letter_to_index(c) for c in cols_letters]

# =========================
# Excel laden
# =========================
xls = pd.ExcelFile(file_path)

p_sheets = [s for s in xls.sheet_names if s.lower().startswith("p")]

if not p_sheets:
    print("Keine 'p'-Sheets gefunden.")
    exit()

reference = None
reference_name = None
differences_found = False

# =========================
# Hauptloop
# =========================
for sheet in p_sheets:
    df = pd.read_excel(xls, sheet_name=sheet)

    # nur gewählte Spalten (A, B, G, H ...)
    df_cut = df.iloc[:, cols_idx]

    # normalisieren
    data = df_cut.fillna("").astype(str).values.tolist()

    if reference is None:
        reference = data
        reference_name = sheet
        continue

    if data != reference:
        differences_found = True

        print("\n==============================")
        print(f"Unterschied in Sheet: {sheet}")
        print(f"Referenz: {reference_name}")
        print("==============================")

        max_rows = min(MAX_ROWS, max(len(data), len(reference)))

        for i in range(max_rows):

            # fehlende Zeilen
            if i >= len(reference):
                print(f"Zeile {i+1}: nur in {sheet} vorhanden")
                continue

            if i >= len(data):
                print(f"Zeile {i+1}: fehlt in {sheet}")
                continue

            # Spaltenvergleich
            for j, col_letter in enumerate(cols_letters):

                val_ref = reference[i][j]
                val_cur = data[i][j]

                if val_ref != val_cur:
                    print(f"Zeile {i+1}, Spalte {col_letter}:")
                    print(f"  Referenz ({reference_name}): {val_ref}")
                    print(f"  Sheet {sheet}:              {val_cur}")

print("\n========== ERGEBNIS ==========")

if not differences_found:
    print(f"Alle 'p'-Sheets sind in {cols_letters} (bis Zeile {MAX_ROWS}) identisch.")
else:
    print("Unterschiede gefunden (siehe oben).")