# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
import pandas as pd

df = pd.read_csv("persona.csv")
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: '%.2f' % x)

#############################################
# GÖREV 1: Veri Genel Bilgileri
#############################################
print(df.head())
print(df.shape)
print(df.info())
#-----------------------------------
print(df["SOURCE"].nunique())
print(df["SOURCE"].value_counts())
#-----------------------------------
print(df["PRICE"].nunique())
print(df["PRICE"].value_counts())

print(df.groupby("COUNTRY")["PRICE"].nunique())
print(df.groupby("COUNTRY").agg({"PRICE": "sum"}))

print(df.groupby("SOURCE").agg({"PRICE": "sum"}))

print(df.groupby("COUNTRY").agg({"PRICE": "mean"}))
print(df.groupby("SOURCE").agg({"PRICE": "mean"}))

country_source_mean = df.groupby(["COUNTRY", "SOURCE"])["PRICE"].mean()
print(country_source_mean)

# Pivot table ile COUNTRY-SOURCE-SEX-AGE kırılımında PRICE ortalamaları
pivot_table_avg = pd.pivot_table(
    df,
    values="PRICE",               # Hesaplanacak değer
    index=["COUNTRY", "SOURCE", "SEX", "AGE"],  # Kırılım kolonları
    aggfunc="mean"                # Ortalama hesapla
)

# Pivot table'ı yazdır
print(pivot_table_avg)
# COUNTRY, SOURCE, SEX, AGE kırılımında PRICE ortalamaları
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

# PRICE'a göre azalan sırala
agg_df = agg_df.sort_values("PRICE", ascending=False)

# Sonucu yazdır
print(agg_df.head(20))  # İlk 20 satırı göster

# İNDEXLERİ SÜTUNA ÇEVİRİYORUZ
agg_df = agg_df.reset_index()

print(agg_df.head(15))

# Age değişkenini kategorik hale getirme
bins = [0, 18, 23, 30, 40, 70]   # yaş aralıkları
labels = ["0_18", "19_23", "24_30", "31_40", "41_70"]  # kategori etiketleri

df["AGE_CAT"] = pd.cut(df["AGE"], bins=bins, labels=labels, right=True)

print(df[["AGE", "AGE_CAT"]].head(20))

print(df.head(20))

# Yeni seviye tabanlı müşteriler (persona) oluşturma
df["customers_level_based"] = (
    df["COUNTRY"].str.upper() + "_" +
    df["SOURCE"].str.upper() + "_" +
    df["SEX"].str.upper() + "_" +
    df["AGE_CAT"].astype(str)
)

# Tekilleştirme: aynı persona birden fazla kez olabilir, ortalama PRICE alıyoruz
persona_df = df.groupby("customers_level_based").agg({"PRICE": "mean"}).reset_index()

print(persona_df.head(20))


# Segmentlere ayırma (4 eşit parçaya böler, A en yüksek fiyatlı segment)
persona_df["SEGMENT"] = pd.qcut(persona_df["PRICE"], 4, labels=["D", "C", "B", "A"])

# Segmentleri betimleme (ortalama, maksimum, toplam kazanç)
segment_summary = persona_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]}).reset_index()

print(persona_df.head(20))
print("\nSEGMENT ÖZETİ:\n")
print(segment_summary)

# 33 yaşında, Android kullanan Türk kadını
# 33 yaş hangi kategoriye giriyor? 31-40 arası → AGE_CAT = 31_40
new_user1 = "TUR_ANDROID_FEMALE_31_40"
result1 = persona_df[persona_df["customers_level_based"] == new_user1]

# 35 yaşında, IOS kullanan Fransız kadını
# 35 yaş yine 31-40 arası → AGE_CAT = 31_40
new_user2 = "FRA_IOS_FEMALE_31_40"
result2 = persona_df[persona_df["customers_level_based"] == new_user2]

print("33 yaşındaki Türk kadın (ANDROID):\n", result1, "\n")
print("35 yaşındaki Fransız kadın (IOS):\n", result2)























