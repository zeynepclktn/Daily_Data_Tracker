# 📊 Daily Data Tracker

Günlük olarak **döviz kurları** (USD, EUR), **İstanbul sıcaklık verileri** ve **uyarı durumlarını** takip edip kaydeden bir Python projesi.  
Veriler CSV dosyalarında saklanır, ayrıca görselleştirilerek `visuals/` klasörüne kaydedilir.

---

## 🚀 Özellikler
- **Döviz Takibi**  
  - 1 USD ve 1 EUR’nun TL karşılığı anlık olarak çekilir.  
  - USD ve EUR için belirlenen eşik değerler üzerinden **uyarı kontrolü** yapılır.  

- **Hava Durumu Takibi**  
  - İstanbul için gün içerisindeki saatlik sıcaklık değerleri çekilir.  
  - Günlük ortalama sıcaklık hesaplanır.  
  - Anlık sıcaklık ile ortalama karşılaştırılır.  
  - Sıcaklık belirlenen eşik değerini aştığında **uyarı üretilir**.  

- **Veri Kaydı**  
  - `data/currency.csv` → Anlık döviz & sıcaklık verileri  
  - `data/analysis.csv` → Günlük analiz & uyarı sonuçları  

- **Görselleştirme**  
  - `visuals/temperature_daily.png` → Gün içerisindeki saatlik sıcaklık değişimleri (çizgi grafik)  
  - `visuals/temperature_vs_avg.png` → Anlık sıcaklık ve günlük ortalama karşılaştırması (bar chart + ortalama çizgisi)  
  - `visuals/warnings_bar.png` → Uyarı durumları (Normal → yeşil, AŞTI → kırmızı)  

---

## 🛠️ Kullanılan Teknolojiler
- Python 3.x  
- `requests` → API'den veri çekmek için  
- `pandas` → Veri işleme  
- `matplotlib` → Görselleştirme  

---

## 📂 Proje Yapısı
Daily_Data_Tracker/
│
├── data/ # Verilerin kaydedildiği CSV dosyaları
│ ├── currency.csv
│ └── analysis.csv
│
├── visuals/ # Otomatik oluşturulan grafikler
│ ├── temperature_daily.png
│ ├── temperature_vs_avg.png
│ └── warnings_bar.png
│
├── main.py # Ana Python scripti
└── README.md # Bu dosya
