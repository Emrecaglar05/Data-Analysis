import matplotlib.pyplot as plt
import pandas as pd

def grafik_ciz():
    print("Grafik Çiziciye Hoşgeldiniz")
    print("Lütfen bir grafik seçiniz:")
    print("1. Çizgi Grafik")
    print("2. Çubuk Grafik")
    print("3. Dağılım Grafiği")

    secim = input("Lütfen seçiminizi yapınız (1/2/3): ")

    if secim not in ["1", "2", "3"]:
        print("Geçersiz seçim.")
        return

    print("\nNasıl veri girmek istersiniz?")
    print("1. Kendiniz girin")
    print("2. CSV dosyası yükleyin")

    veri_secim = input("Bir seçim numarası giriniz (1/2): ")

    if veri_secim == "1":
        try:
            x = list(map(float, input("Boşluk bırakarak x değerlerini giriniz: ").split()))
            y = list(map(float, input("Boşluk bırakarak y değerlerini giriniz: ").split()))
        except ValueError:
            print("Geçersiz sayı formatı.")
            return
    elif veri_secim == "2":
        dosya_yolu = input("CSV dosyanızın yolunu girin: ")
        try:
            veri = pd.read_csv(dosya_yolu)
            x = veri.iloc[:, 0]
            y = veri.iloc[:, 1]
        except Exception as e:
            print("CSV dosyası okunamadı:", e)
            return
    else:
        print("Hatalı seçim.")
        return

    # Grafik çizimi
    plt.figure(figsize=(8, 6))

    if secim == "1":
        plt.plot(x, y, label="Çizgi Grafik", marker="o")
    elif secim == "2":
        plt.bar(x, y, color="skyblue", label="Çubuk Grafik")
    elif secim == "3":
        plt.scatter(x, y, color="red", label="Dağılım Grafiği")

    plt.title("Grafik Gösterimi")
    plt.xlabel("X Ekseni")
    plt.ylabel("Y Ekseni")
    plt.legend()
    plt.grid(True)

    # Grafik kaydetme tercihi
    save_choice = input("Grafiği kaydetmek ister misiniz? (yes/no): ").lower()
    if save_choice == "yes":
        file_name = input("Dosya adını girin (örnek: grafik.png): ")
        try:
            plt.savefig(file_name)
            print(f"Grafik '{file_name}' olarak kaydedildi.")
        except Exception as e:
            print("Kaydetme işlemi başarısız:", e)

    plt.show()


grafik_ciz()
