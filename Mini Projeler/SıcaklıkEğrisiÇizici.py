import pandas as pd
import matplotlib.pyplot as plt


def veri_yukle(dosya_yolu):
    """CSV dosyasından sıcaklık verisini yükler."""
    try:
        veri = pd.read_csv(dosya_yolu, parse_dates=["Date"])
        print("Veri başarıyla yüklendi!")
        return veri
    except Exception as e:
        print("Veri yüklenirken hata oluştu:", e)
        return None


def sicaklik_grafigi_ciz(veri, kaydet_dosya_adi=None):
    """Sıcaklık eğilimlerini ve anomali noktalarını çizer."""

    # 7 günlük hareketli ortalama hesapla
    veri["7 Günlük Ortalama"] = veri["Temperature"].rolling(window=7).mean()

    # Anomalileri tespit et
    ortalama = veri["Temperature"].mean()
    std_sapma = veri["Temperature"].std()
    veri["Anomali"] = (veri["Temperature"] > ortalama + 2 * std_sapma) | \
                      (veri["Temperature"] < ortalama - 2 * std_sapma)

    # Grafik çizimi
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.figure(figsize=(10, 6))
    plt.plot(veri["Date"], veri["Temperature"], label="Günlük Sıcaklık", color="blue")
    plt.plot(veri["Date"], veri["7 Günlük Ortalama"], label="7 Günlük Ortalama", linestyle="--", color="orange")
    plt.scatter(veri[veri["Anomali"]]["Date"], veri[veri["Anomali"]]["Temperature"],
                color="red", label="Anomaliler")

    plt.title("Sıcaklık Eğilimleri")
    plt.xlabel("Tarih")
    plt.ylabel("Sıcaklık (°C)")
    plt.legend()
    plt.grid(True)

    # Grafiği kaydet veya göster
    if kaydet_dosya_adi:
        plt.savefig(kaydet_dosya_adi)
        print(f"Grafik {kaydet_dosya_adi} olarak kaydedildi.")
    else:
        plt.show()


def main():
    print("🌡️ Sıcaklık Grafiği Oluşturucuya Hoş Geldiniz!")

    # Veri Yükleme
    dosya_yolu = input("📄 Sıcaklık verisi içeren CSV dosyasının yolunu giriniz: ")
    veri = veri_yukle(dosya_yolu)
    if veri is None:
        return

    # Grafiği kaydetme seçeneği
    kaydet = input("📸 Grafiği kaydetmek ister misiniz? (evet/hayır): ").lower()
    if kaydet == "evet":
        dosya_adi = input("Kaydedilecek dosya adını giriniz (örnek: grafik.png): ")
        sicaklik_grafigi_ciz(veri, kaydet_dosya_adi=dosya_adi)
    else:
        sicaklik_grafigi_ciz(veri)


if __name__ == "__main__":
    main()
