# ============================================
# Pandas ile Veri Temizleme - Çalışma Defteri
# ============================================

import pandas as pd

# --------------------------------------------
# 1. CSV DOSYASINI OKUMA
# --------------------------------------------
# CSV dosyasını okuyoruz (dosya aynı klasörde olmalı)
df = pd.read_csv("csv_dosyaları/eksik_veriler.csv")

# İlk 10 satırı görüntüle
print("İlk 10 Kayıt:")
print(df.head(10))

# Veri setinin satır ve sütun sayısı
print("\nVeri setinin boyutu (satır, sütun):")
print(df.shape)

# Sütunlardaki veri tiplerini göster
print("\nVeri tipleri:")
print(df.dtypes)

# Sayısal sütunlar için istatistiksel özet
print("\nSayısal sütunlar için istatistiksel özet:")
print(df.describe())

# --------------------------------------------
# 2. EKSİK DEĞER ANALİZİ
# --------------------------------------------
# Hangi sütunda kaç eksik değer var?
print("\nEksik değer sayıları:")
print(df.isnull().sum())

# --------------------------------------------
# 3. EKSİK DEĞERLERİ DOLDURMA
# --------------------------------------------

# Eksik isimleri 'Gülçin' ile doldur
df['isim'] = df['isim'].fillna("Gülçin")
print("\nEksik isimler dolduruldu:")
print(df.head(10))

# Eksik yaşları ortalama ile doldur
df['yaş'] = df['yaş'].fillna(df['yaş'].mean())

# Eksik meslek ve konumları 'Bilinmiyor' ile doldur
df['meslek'] = df['meslek'].fillna("Bilinmiyor")
df['konum'] = df['konum'].fillna("Bilinmiyor")

# --------------------------------------------
# 4. YİNELENEN (DUPLICATE) KAYITLARI SİLME
# --------------------------------------------

# Yinelenen kayıt sayısını göster
print("\nYinelenen kayıt sayısı:")
print(df.duplicated().sum())

# Yinelenenleri sil
df = df.drop_duplicates()

# --------------------------------------------
# 5. SÜTUN İSİMLERİNİ DEĞİŞTİRME
# --------------------------------------------

# 'isim' sütununu 'İsimler' olarak değiştiriyoruz
df = df.rename(columns={"isim": "İsimler"})

# --------------------------------------------
# 6. METİN VERİLERİ ÜZERİNDE İŞLEMLER
# --------------------------------------------

# İsimleri büyük harfe çevir (uppercase)
df["İsimler"] = df["İsimler"].str.upper()

# --------------------------------------------
# 7. SAYISAL VERİYİ NORMALLEŞTİRME (Z-Score)
# --------------------------------------------

# Z-Score: (değer - ortalama) / standart sapma
df["yaş_normalize"] = (df["yaş"] - df["yaş"].mean()) / df["yaş"].std()


# --------------------------------------------
# 8. SON VERİYİ GÖSTER
# --------------------------------------------
print("\nTemizlenmiş ve işlenmiş veri:")
print(df)

# --------------------------------------------
# 9. İSTEĞE BAĞLI: DOSYAYI KAYDET
# --------------------------------------------
# df.to_csv("temizlenmis_veri.csv", index=False)


