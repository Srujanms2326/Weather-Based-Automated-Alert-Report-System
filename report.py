import pandas as pd

def generate_report():
    try:
        df = pd.read_csv("database.csv", names=["Date", "Temp", "Weather"])
        df.to_excel("weather_report.xlsx", index=False)
        print("Report generated successfully!")
    except:
        print("No data available for report.")