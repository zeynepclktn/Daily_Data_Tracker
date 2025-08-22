import requests
import pandas as pd
import os
from datetime import datetime

import matplotlib.pyplot as plt

now = datetime.now()
current_time = now.strftime("%H")
current_date = now.strftime("%Y-%m-%d")
temp_threshold= 30
usd_threshold = 41
eur_threshold = 45

response = requests.get("https://open.er-api.com/v6/latest/USD")
data = response.json()
df = pd.DataFrame(data["rates"].items(), columns=["Currency","Rate"])
TRY = df[df["Currency"]=="TRY"]["Rate"].values[0]
df["Rate_In_TRY"] = df["Rate"] / TRY

USD = data["rates"]["TRY"]
EUR = (1/data["rates"]["EUR"]) * USD
TRY_MAX = df[df["Rate_In_TRY"]== df["Rate_In_TRY"].max()][["Currency","Rate_In_TRY"]]
TRY_MIN = df[df["Rate_In_TRY"]== df["Rate_In_TRY"].min()][["Currency","Rate_In_TRY"]]

response_2 = requests.get("https://api.open-meteo.com/v1/forecast?latitude=41.0138&longitude=28.9497&hourly=temperature_2m")
data_2 = response_2.json()
hourly = data_2["hourly"]
for i, time_str in enumerate(hourly['time']):
        if time_str[0:10] == current_date and time_str[-5:-3] == current_time:
            weather= {
                'time': time_str,
                'temperature_2m': hourly['temperature_2m'][i]
            }
mean_temp = pd.DataFrame(hourly["temperature_2m"]).mean().values[0]

row = {
    'Datetime': now,
    'TRY_to_USD': USD,
    'TRY_to_EUR': EUR,
    'Time': weather["time"],
    'Temperature': weather["temperature_2m"]
}
analysis = {
    'Avg_Temp': mean_temp,
    'USD_Warning': "AŞTI" if USD >= usd_threshold else "Normal",
    'EUR_Warning': "AŞTI" if EUR >= eur_threshold else "Normal",
    'Temp_Warning': "AŞTI" if weather["temperature_2m"] >= temp_threshold else "Normal"
}

dff = pd.DataFrame([row])
df_analysis = pd.DataFrame([analysis])

dff.to_csv("Daily_Data_Tracker/data/currency.csv", mode="a", header = not os.path.exists("Daily_Data_Tracker/data/currency.csv"),index=False, encoding="utf-8")
df_analysis.to_csv("Daily_Data_Tracker/data/analysis.csv", mode="a", header = not os.path.exists("Daily_Data_Tracker/data/analysis.csv"),index=False, encoding="utf-8")
plt.figure(figsize=(12,5))  # genişliği büyüt, okunaklı olur
plt.plot(hourly["time"], hourly["temperature_2m"], label="Saat/Sıcaklık")
plt.xticks(hourly["time"][::3], rotation=45)
plt.xlabel("Saat")
plt.ylabel("Sıcaklık (°C)")
plt.title("Gün içerisindeki sıcaklık değişimleri")
plt.legend()
plt.tight_layout()
plt.savefig("Daily_Data_Tracker/visuals/temperature_daily.png", dpi=300)
plt.show()

#İkinci grafik
plt.figure(figsize=(10,6))
plt.bar(dff["Time"], dff["Temperature"], color="skyblue", label="Anlık Sıcaklık")

# Ortalama çizgisi
plt.axhline(df_analysis["Avg_Temp"].iloc[-1], color="red", linestyle="--", 
            label=f"Ortalama: {df_analysis['Avg_Temp'].iloc[-1]:.1f}°C")

plt.xticks(rotation=45)
plt.xlabel("Saat")
plt.ylabel("Sıcaklık (°C)")
plt.title("Saatlik sıcaklıklar ve günlük ortalama")
plt.legend()
plt.tight_layout()
plt.savefig("Daily_Data_Tracker/visuals/temperature_vs_avg.png", dpi=300)
plt.show()



last = df_analysis.iloc[-1][["USD_Warning","EUR_Warning","Temp_Warning"]]
labels = last.index  
values = [1]*len(labels)  
colors = ["green" if val=="Normal" else "red" for val in last.values]
plt.figure(figsize=(6,4))
plt.bar(labels, values, color=colors)

plt.title("Uyarı Durumları")
plt.ylabel("Durum")
plt.yticks([])  # Y eksenini gizle
for i, val in enumerate(last.values):
    plt.text(i, 1.02, val, ha="center", fontsize=10, color="black")
plt.savefig("Daily_Data_Tracker/visuals/warnings_bar.png", dpi=300)
plt.show()