import json
import os

def create_task_files(pid):
    output_dir = f"DATA/participant_{pid}/"
    # Vorlage-Daten
    template = {
        "Result Cell understood (1 / 0)": {
            "explicitly mentioned": 0,
            "implied understand": 0
        },
        "each operation understood (1 point for each)": {
            "explicitly mentioned": 0,
            "implied understanding": 0
        },
        "each expected operand understood (1 point for each)": {
            "explicitly mentioned": 0,
            "implied understanding": 0
        },
        "Result Type understood (1.0/0.5/0)": {
            "explicitly mentioned": 0,
            "implied understanding": 0
        },
        "time taken (sec)": "",
        "start (of new slide)": "",
        "timestamp where participant realizes": "",
        "end of this slide": "",
        "notes": ""
    }

    # Ordner erstellen, falls nicht vorhanden
    os.makedirs(output_dir, exist_ok=True)

    # Dateien erzeugen
    for tid in range(1, 18):  # 1 bis 17
        filename = f"task_{pid}_{tid}.json"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(template, f, indent=2, ensure_ascii=False)

        print(f"Erstellt: {filepath}")

# Beispiel-Aufruf
