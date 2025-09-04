#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

import pandas as pd

# Görünüm ayarları
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: '%.2f' % x)

#############################################
# GÖREV 1: Veri Genel Bilgileri
#############################################

# 1. Veri setini yükle
df = pd.read_excel("gezinomi.xlsx")

print(df.head())
print(df.shape)
print(df.info())

# 2. Kaç unique şehir vardır? Frekansları nedir?
print("Unique şehir sayısı:", df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

# 3. Kaç unique Concept vardır?
print("Unique Concept sayısı:", df["ConceptName"].nunique())

# 4. Hangi Concept’ten kaçar tane satış olmuş?
print(df["ConceptName"].value_counts())

#############################################
# GÖREV 2: EB_Score Değişkeni
#############################################

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)

#############################################
# GÖREV 3: Pivot Tablolar ile Kırılımlar
#############################################

# 1. Şehir-Concept-EB_Score kırılımı
pivot_eb = pd.pivot_table(
    df,
    values="Price",
    index=["SaleCityName", "ConceptName"],
    columns="EB_Score",
    aggfunc=["mean", "count"]
)

# 2. Şehir-Concept-Sezon kırılımı
pivot_season = pd.pivot_table(
    df,
    values="Price",
    index=["SaleCityName", "ConceptName"],
    columns="Seasons",
    aggfunc=["mean", "count"]
)

# 3. Şehir-Concept-CInDay kırılımı
pivot_day = pd.pivot_table(
    df,
    values="Price",
    index=["SaleCityName", "ConceptName"],
    columns="CInDay",
    aggfunc=["mean", "count"]
)

#############################################
# GÖREV 4: City-Concept-Season Kırılımını PRICE’a Göre Sıralama
#############################################

agg_df = (df.groupby(["SaleCityName", "ConceptName", "Seasons"])
            .agg({"Price": "mean"})
            .sort_values("Price", ascending=False))

agg_df.reset_index(inplace=True)

#############################################
# GÖREV 5: Yeni Level-Based Satış Tanımı
#############################################

agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]] \
                                .agg(lambda x: "_".join(x).upper(), axis=1)

#############################################
# GÖREV 6: Segmentasyon
#############################################

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])

# Segmentlerin genel özeti
print(agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]}))

#############################################
# GÖREV 7: Yeni Kullanıcı Örneği
#############################################

# Antalya – Herşey Dahil – High segmenti
new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
print(agg_df[agg_df["sales_level_based"] == new_user])

#############################################
# SONUÇ: Pivot tabloları kaydet
#############################################

with pd.ExcelWriter("pivot_kirilimlar.xlsx") as writer:
    pivot_eb.to_excel(writer, sheet_name="EB_Score")
    pivot_season.to_excel(writer, sheet_name="Seasons")
    pivot_day.to_excel(writer, sheet_name="CheckInDay")
    agg_df.to_excel(writer, sheet_name="Segmentler", index=False)
