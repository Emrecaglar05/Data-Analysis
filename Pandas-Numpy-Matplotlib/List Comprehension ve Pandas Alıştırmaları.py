import pandas as pd
import seaborn as sns
import numpy as np

# Görünüm ayarları
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

#######################################
# CAR CRASHES VERİ SETİ
#######################################

# Veri setini yükle
df = sns.load_dataset("car_crashes")

# Numerik değişkenlerin başına NUM ekle ve tüm isimleri büyük yap
df.columns = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

# İsminin içinde 'NO' olmayan değişkenlerin sonuna FLAG ekle
df.columns = [col + "_FLAG" if "NO" not in col else col for col in df.columns]

# Belirli kolonları seçip yeni bir dataframe oluştur
og_list = ["ABBREV_FLAG", "NO_PREVIOUS"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]

#######################################
# TITANIC VERİ SETİ
#######################################

df = sns.load_dataset("titanic")

# Kadın ve erkek yolcu sayısı
print(df["sex"].value_counts())

# Her sütunun unique değer sayısı
print(df.nunique())

# Pclass unique değerleri
print(df["pclass"].unique())

# Pclass ve parch unique değer sayıları
print(df[["pclass", "parch"]].nunique())

# embarked değişkeninin tipi category olsun
df["embarked"] = df["embarked"].astype("category")

# embarked = 'C' olan yolcular
print(df[df["embarked"]=="C"])

# embarked != 'S' olan yolcular
print(df[~(df["embarked"]=="S")])

# 30 yaşından küçük kadın yolcular
print(df[(df["age"]<30) & (df["sex"]=="female")])

# Fare > 500 veya Age > 70 olan yolcular
print(df[(df["fare"]>500) | (df["age"]>70)])

# Boş değerlerin toplamı
print(df.isnull().sum())

# who değişkenini kaldır
df.drop("who", axis=1, inplace=True)

# deck değişkenindeki boş değerleri en sık tekrar eden değer (mode) ile doldur
df["deck"] = df["deck"].fillna(df["deck"].mode()[0])

# age değişkenindeki boş değerleri median ile doldur
df["age"] = df["age"].fillna(df["age"].median())

# survived kırılımı: pclass ve sex
print(df.groupby(["pclass","sex"]).agg({"survived": ["sum","count","mean"]}))

# age_flag değişkeni: 30 yaş altına 1, üstüne 0
df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)

#######################################
# TIPS VERİ SETİ
#######################################

df = sns.load_dataset("tips")

# Time (yemek saati) göre total_bill istatistikleri
print(df.groupby("time").agg({"total_bill": ["sum","min","mean","max"]}))

# Gün ve Time kırılımında total_bill istatistikleri
print(df.groupby(["day","time"]).agg({"total_bill": ["sum","min","mean","max"]}))

# Lunch ve kadın müşteriler için day'e göre istatistikler
print(df[(df["time"]=="Lunch") & (df["sex"]=="Female")].groupby("day").agg({
    "total_bill": ["sum","min","max","mean"],
    "tip": ["sum","min","max","mean"]
}))

# size < 3 ve total_bill > 10 olan siparişlerin ortalaması
print(df.loc[(df["size"]<3) & (df["total_bill"]>10), "total_bill"].mean())

# total_bill ve tip toplamını hesapla
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

# total_bill_tip_sum değerine göre azalan sırala ve ilk 30 kişiyi al
new_df = df.sort_values("total_bill_tip_sum", ascending=False).head(30)
print(new_df.shape)
print(new_df.head())
