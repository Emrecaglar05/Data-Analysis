import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veri = pd.read_csv("csv_dosyaları/sales_data.csv")
print(veri.head())

# Veri kümesinin özeti

print(veri.info())

print(veri.describe())

# Eksik değerlere bak
print(veri.isnull().sum())

# Eksik değerleri doldurma ya da eksik değerleri olan satırları silme

veri["Product_Category"] = veri["Product_Category"].fillna("Bilinmeyen") # DOLDURMA
veri = veri.dropna() # Eksik değerleri silme

# Tarih Sutununu değiştirme
veri["Date"] = pd.to_datetime(veri["Date"])


veri["Sales_Amount"] = pd.to_numeric(veri["Sales_Amount"], errors="coerce")

# Yıl, Ay, Gelir sütunu ekleme

veri['Yıl_Ay'] = veri['Date'].dt.to_period('M')
veri['Revenue'] = veri['Quantity'] * veri['Price']


# Aylık satışlara göre gruplama

aylık_Satis = veri.groupby("Yıl_Ay")['Sales_Amount'].sum()
print(aylık_Satis)

# En çok gelir getiren 5 ürün

enıyı_urunler = veri.groupby('Product_Name')['Revenue'].sum().sort_values(ascending=False).head(5)
print(enıyı_urunler)

# Aylık satışları çizme

aylık_Satis.plot(kind="bar", figsize=(10, 6), color="red")
plt.title("Aylık Satışlar")
plt.xlabel("Ay")
plt.ylabel("Toplam Satış")
plt.xticks(rotation=0)
plt.show()

