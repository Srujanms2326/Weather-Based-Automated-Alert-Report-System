import schedule
import time

from weather_api import get_weather
from analyzer import analyze_weather
from alerts import send_email
from storage import save_to_csv
from report import generate_report
from config import CITY


def job():
    print("\n🔄 Running weather check...")

    data = get_weather(CITY)

    # ✅ FULL SAFE CHECK
    if not data or "list" not in data:
        print("❌ API Error:", data.get("message", "Invalid API response"))
        return

    try:
        alerts = analyze_weather(data)
        save_to_csv(data)

        if alerts:
            print("⚠️ Alerts detected:")
            for alert in alerts:
                print(alert)
            send_email(alerts)
        else:
            print("✅ No alerts")

        generate_report()

    except Exception as e:
        print(f"❌ Processing Error: {e}")
        print("DEBUG API RESPONSE:", data)


# TEST MODE
schedule.every(10).seconds.do(job)

def run_scheduler():
    print("🚀 Scheduler started...")
    while True:
        schedule.run_pending()
        time.sleep(1)