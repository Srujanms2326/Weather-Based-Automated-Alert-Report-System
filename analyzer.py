from config import TEMP_THRESHOLD

def analyze_weather(data):
    alerts = []

    # ✅ SAFE ACCESS
    if "list" not in data:
        return alerts

    for entry in data["list"]:
        temp = entry.get("main", {}).get("temp", 0)
        condition = entry.get("weather", [{}])[0].get("main", "").lower()

        if temp > TEMP_THRESHOLD:
            alerts.append(f"🔥 High Temperature Alert: {temp}°C")

        if "rain" in condition:
            alerts.append("🌧️ Rain Expected")

        if "storm" in condition:
            alerts.append("⛈️ Storm Warning")

    return list(set(alerts))