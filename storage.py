import csv
import os

FILE = "database.csv"

def save_to_csv(data):
    if "list" not in data:
        return

    file_exists = os.path.isfile(FILE)

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Temp", "Weather"])

        for entry in data["list"]:
            writer.writerow([
                entry.get("dt_txt", ""),
                entry.get("main", {}).get("temp", ""),
                entry.get("weather", [{}])[0].get("description", "")
            ])

    print("💾 Data saved")