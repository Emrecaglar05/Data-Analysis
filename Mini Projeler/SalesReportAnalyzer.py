import pandas as pd
import matplotlib.pyplot as plt

def veri_yukle(file_path):
    try:
        veri = pd.read_csv(file_path)
        print("Veri Yüklendi")
        return veri
    except Exception as e:
        print("Veri Yüklenemedi")
        return None

def veri_temizleme(veri):
    print("\nVeri Temizleniyor..")
    # İlk olarak boş yerleri doldurma
    veri['Product_Category'] = veri['Product_Category'].fillna("Bilinmeyen")
    veri = veri.dropna()

    # Dönüşüm İşlemleri
    veri['Date'] = pd.to_datetime(veri['Date'])
    veri['Sales_Amount'] = pd.to_numeric(veri['Sales_Amount'], errors='coerce')

    # Yeni kolon ekleme
    veri['Year_Month'] = veri['Date'].dt.to_period('M')
    if 'Quantity' in veri.columns and 'Price' in veri.columns:
        veri['Revenue'] = veri['Quantity'] * veri['Price']

    print("Veri Başarıyla Temizlendi")
    return veri

def veri_analizi(veri):
    aylık_satis = veri.groupby('Year_Month')['Sales_Amount'].sum()
    print("Aylık Satış :", aylık_satis)

    if 'Revenue' in veri.columns:
        eniyiurunler = veri.groupby('Product_Name')['Revenue'].sum().sort_values(ascending=False)
        print("En İyi Ürünler :", eniyiurunler)

    # Aylık satışı görselleştir
    aylık_satis.plot(kind='bar', figsize=(10, 6), color='red')
    plt.title("Aylık Satışlar")
    plt.xlabel("Ay")
    plt.ylabel("Toplam Satış")
    plt.xticks(rotation=45)
    plt.show()

def main():
    print("Satış Bildirme Analizine Hoşgeldiniz")

    file_path = input("CSV DOSYASININ YOLUNU GİRİNİZ: ")
    veri = veri_yukle(file_path)
    if veri is None:
        return
    veri = veri_temizleme(veri)

    veri_analizi(veri)

if __name__ == "__main__":
    main()
