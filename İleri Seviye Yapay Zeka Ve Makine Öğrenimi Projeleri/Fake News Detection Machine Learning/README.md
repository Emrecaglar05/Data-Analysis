# 📰 Makine Öğrenimi ile Yalan Haber Tespiti (Fake News Detection)

Bu proje, bir haber makalesinin metnine dayanarak "GERÇEK" (REAL) veya "YALAN" (FAKE) olarak sınıflandırılması için geliştirilmiş bir makine öğrenimi modelidir.

Bu çözüm, metin verilerini sayısal özelliklere dönüştürmek için `TfidfVectorizer` ve sınıflandırma için `PassiveAggressiveClassifier` kullanır.

## 🤖 Kullanılan Model ve Yöntem

Model, iki ana `scikit-learn` bileşeninden oluşur:

1.  **TfidfVectorizer (Term Frequency-Inverse Document Frequency):**
    * Haber metinlerini sayısal özellik vektörlerine dönüştürür.
    * Yaygın İngilizce "stop words" (durdurma kelimeleri) kaldırır (`stop_words='english'`).
    * Bir kelimenin bir belgede ne kadar önemli olduğunu, tüm belgelerdeki (corpus) sıklığına göre ağırlıklandırarak hesaplar.

2.  **PassiveAggressiveClassifier:**
    * Bu, büyük ölçekli metin sınıflandırma görevleri için oldukça verimli olan bir online öğrenme (online learning) algoritmasıdır.
    * Gelen her yeni veriye göre modelin ağırlıklarını "pasif" (eğer sınıflandırma doğruysa) veya "agresif" (eğer sınıflandırma yanlışsa) bir şekilde günceller.

## 📊 Proje İş Akışı

Betik (`fake_news_detector.py`) aşağıdaki adımları sırasıyla uygular:

1.  **Veri Yükleme:** `news.csv` dosyasını bir pandas DataFrame'e yükler.
2.  **Veri Hazırlama:** Veri setini metin (`df['text']`) ve etiketler (`df['label']`) olarak ayırır.
3.  **Eğitim ve Test Bölümlemesi:** Veri seti, %80 eğitim ve %20 test verisi olacak şekilde (`train_test_split`) bölünür.
4.  **Özellik Çıkarımı (TF-IDF):** `TfidfVectorizer` kullanılarak eğitim ve test metinleri TF-IDF matrislerine dönüştürülür.
5.  **Model Eğitimi:** `PassiveAggressiveClassifier` modeli, `tfidf_train` verisi ile eğitilir.
6.  **Model Değerlendirme:**
    * Eğitilen model, `tfidf_test` verisi üzerinde tahminler yapar.
    * Modelin doğruluğu (accuracy score) hesaplanır ve konsola yazdırılır.
    * Modelin performansını detaylı görmek için bir karışıklık matrisi (confusion matrix) oluşturulur ve yazdırılır.

## ⚙️ Gereksinimler

Projenin çalışması için aşağıdaki Python kütüphaneleri gereklidir:

* pandas
* numpy
* scikit-learn (sklearn)

Bu bağımlılıkları `requirements.txt` dosyası oluşturup şu komutla yükleyebilirsiniz:
```bash
pip install -r requirements.txt
