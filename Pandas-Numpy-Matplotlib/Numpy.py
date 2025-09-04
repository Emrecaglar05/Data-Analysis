# ========================================================
# MATRİS HESAPLAYICI – NUMPY İLE TEMEL MATRİS İŞLEMLERİ
# ========================================================
# Bu program kullanıcıdan iki matris alır ve şu işlemleri yapar:
#
# 1. Toplama (A + B):
#    Aynı boyuttaki iki matrisin karşılık gelen elemanlarını toplar.
#
# 2. Çıkarma (A - B):
#    Aynı boyuttaki iki matrisin karşılık gelen elemanlarını birbirinden çıkarır.
#
# 3. Eleman Bazlı Çarpma (A * B):
#    Aynı boyuttaki iki matrisin karşılık gelen elemanlarını çarpar.
#    (Hadamard Çarpımı olarak da bilinir.)
#
# 4. Matris Çarpımı (Dot Product, A @ B veya np.dot(A, B)):
#    Lineer cebirde kullanılan çarpma işlemidir.
#    A matrisinin sütun sayısı, B matrisinin satır sayısına eşit olmalıdır.
#
# 5. Transpoz (A.T):
#    Matrisin satır ve sütunlarının yer değiştirmesidir.
#    (Satırlar sütun olur, sütunlar satır.)
#
# 6. Determinant (np.linalg.det(A)):
#    Sadece kare matrisler için tanımlıdır (örn. 2x2, 3x3 gibi).
#    Matrisin çözümlenebilirliğini (invertible olup olmadığını) belirler.
#    Determinant = 0 ise matrisin tersi yoktur.
#
# 7. Ters Matris (np.linalg.inv(A)):
#    Yine sadece kare ve determinantı sıfır olmayan matrisler için geçerlidir.
#    Ters matris, matris çarpımında birim matris (I) verecek şekilde davranır:
#    A * A⁻¹ = I
# ========================================================

import numpy as np


# Kullanıcıdan matris girişi alan fonksiyon
def matris_al():
    try:
        # Satır ve sütun sayısı alınıyor
        satir = int(input("Satır sayısını girin: "))
        sutun = int(input("Sütun sayısını girin: "))
        print("Matrisi satır satır girin (her satır için sayıları boşlukla ayırın):")

        elemanlar = []
        for _ in range(satir):
            # Satır verisi alınıp sayıya çevriliyor
            satir_verisi = list(map(float, input().split()))
            if len(satir_verisi) != sutun:
                raise ValueError("Girilen sütun sayısı eşleşmiyor.")
            elemanlar.append(satir_verisi)

        # NumPy dizisine dönüştürülüyor
        return np.array(elemanlar)

    except ValueError as e:
        print("Hata:", e)
        return None


# İki matrisle çeşitli işlemler yapan fonksiyon
def matris_islemleri(A, B):
    print("\nMatris A:\n", A)
    print("\nMatris B:\n", B)

    # Toplama işlemi
    try:
        print("\nToplama (A + B):\n", A + B)
    except ValueError:
        print("\nToplama: Matris boyutları aynı olmalı.")

    # Çıkarma işlemi
    try:
        print("\nÇıkarma (A - B):\n", A - B)
    except ValueError:
        print("\nÇıkarma: Matris boyutları aynı olmalı.")

    # Eleman bazlı çarpma (Hadamard çarpımı)
    try:
        print("\nEleman Bazlı Çarpma (A * B):\n", A * B)
    except ValueError:
        print("\nEleman Bazlı Çarpma: Matris boyutları aynı olmalı.")

    # Matris çarpımı (Dot Product)
    try:
        print("\nMatris Çarpımı (A @ B):\n", np.dot(A, B))
    except ValueError:
        print("\nMatris Çarpımı: A'nın sütun sayısı, B'nin satır sayısına eşit olmalı.")

    # Transpozlar
    print("\nA Matrisinin Transpozu (A^T):\n", A.T)
    print("\nB Matrisinin Transpozu (B^T):\n", B.T)

    # Determinant ve ters alma işlemleri sadece kare matrisler için geçerli
    try:
        print("\nA Matrisinin Determinantı:\n", np.linalg.det(A))
    except np.linalg.LinAlgError:
        print("\nDeterminant: A matrisi kare olmalı.")

    try:
        print("\nA Matrisinin Tersi:\n", np.linalg.inv(A))
    except np.linalg.LinAlgError:
        print("\nTers: A matrisi terslenemez (determinantı sıfır olabilir ya da kare değil).")


# Ana fonksiyon: Programın başlangıç noktası
def ana():
    print("=== Matris Hesaplayıcı ===")
    print("Matris A'yı giriniz:")
    A = matris_al()
    if A is None:
        return

    print("\nMatris B'yi giriniz:")
    B = matris_al()
    if B is None:
        return

    # Matris işlemleri başlatılıyor
    matris_islemleri(A, B)


# Eğer bu dosya direkt çalıştırılırsa ana fonksiyonu çağır
if __name__ == "__main__":
    ana()
