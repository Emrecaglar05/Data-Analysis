# 📈 Bitcoin Fiyat Tahmini - XGBoost ile Zaman Serisi Modeli

Bu proje, `BTC-USD` günlük verilerini kullanarak bir zaman serisi tahmini modeli oluşturmayı amaçlamaktadır. Model, özellikleri çıkarılmış zaman damgalarını ve gecikme (lag) değerlerini kullanarak gelecekteki Bitcoin kapanış fiyatlarını tahmin etmek için **XGBoost Regressor** algoritmasını kullanır.

## 🚀 Proje Hedefi

Temel amaç, tarihsel fiyat verilerine dayalı özellikler (feature) oluşturarak ve güçlü bir gradient boosting modeli (XGBoost) eğiterek kısa vadeli Bitcoin fiyat hareketlerini tahmin etmektir.

## 🛠️ Proje İş Akışı

Bu notebook'taki analiz ve modelleme süreci aşağıdaki adımları içermektedir:

1.  **Veri Yükleme:** `BTC-USD.csv` veri seti yüklenir ve tarih (Date) sütunu zaman serisi indeksi olarak ayarlanır.
2.  **Veri Temizleme:** Kullanılmayan sütunlar (`Open`, `High`, `Low`, `Adj Close`, `Volume`) veri setinden çıkarılır ve eksik değerler (varsa) kontrol edilir.
3.  **Keşifsel Veri Analizi (EDA):** Kapanış (`Close`) fiyatının zaman içindeki değişimi görselleştirilir.
4.  **Özellik Mühendisliği (Feature Engineering):** Modelin zaman kalıplarını öğrenebilmesi için tarih indeksinden yeni özellikler türetilir:
    * Haftanın günü (`dayofweek`)
    * Çeyrek (`quarter`)
    * Ay (`month`)
    * Yıl (`year`)
    * Yılın günü (`dayofyear`)
    * Yılın haftası (`weekofyear`)
5.  **Gecikme Özellikleri (Lag Features):** Fiyatın geçmişteki değerlerini bir özellik olarak eklemek için 3 günlük gecikme (`lag1`, `lag2`, `lag3`) özellikleri oluşturulur.
6.  **Veri Bölümleme (Train/Test Split):**
    * Veri seti, zaman sırasını koruyacak şekilde bölünür.
    * **Eğitim Seti:** 2020-01-01 tarihinden önceki tüm veriler.
    * **Test Seti:** 2020-01-01 tarihi ve sonrasındaki veriler.
7.  **Modelleme (XGBoost):**
    * Bir `xgb.XGBRegressor` modeli oluşturulur ve eğitim verisi (`X_train`, `y_train`) ile eğitilir.
8.  **Model Değerlendirme:**
    * Modelin performansı test seti üzerinde değerlendirilir.
    * Gerçek değerler ve tahmin edilen değerler görselleştirilir.
    * Modelin hata oranı **RMSE (Kök Ortalama Kare Hata)** metriği ile hesaplanır.
9.  **Özellik Önemi (Feature Importance):**
    * Modelin hangi özelliklere (örn. `lag1`, `dayofyear`) daha fazla ağırlık verdiği görselleştirilir.
10. **Tahmin (Forecasting):**
    * Model, eğitim setinin son tarihinden itibaren bir haftalık (7 gün) gelecek tahmini yapar.

## 💻 Kullanılan Kütüphaneler

* **pandas:** Veri manipülasyonu ve analizi.
* **numpy:** Sayısal işlemler.
* **matplotlib & seaborn:** Veri görselleştirme.
* **scikit-learn (sklearn):** Model değerlendirme (RMSE).
* **xgboost:** Makine öğrenimi modeli (XGBRegressor).

## 🚀 Nasıl Çalıştırılır

1.  Bu repoyu klonlayın:
    ```bash
    git clone [https://github.com/kullanici-adiniz/bitcoin-tahmin-projesi.git](https://github.com/kullanici-adiniz/bitcoin-tahmin-projesi.git)
    ```
2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn xgboost
    ```
3.  Proje dizinine gidin ve Jupyter Notebook'u başlatın:
    ```bash
    cd bitcoin-tahmin-projesi
    jupyter notebook notebook.ipynb
    ```