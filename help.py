import json

numbers = [
    "02", "03", "04", "05", "06", "07", "09",
    "31", "33", "34", "21", "27", "11", "30",
    "28", "14", "20", "38", "26", "15", 
]

content = {
    "How much experience do you have using spreadsheets?": "",
    "How much experience do you have using tablets or similar large touchscreens?": "",
    "How much experience do you have using a digital pen or stylus?": "",
    "What is the direction of your native language?": "",
    "What is your age group?": "",
    "What is your gender?": ""
}

for nr in numbers:
    filename = f"dempgraphics_p{nr}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

print("Fertig: Dateien erstellt.")