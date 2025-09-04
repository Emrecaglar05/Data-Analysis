import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8 ,10]

#  Çizgi Grafik
plt.plot(x, y, label="Line")
plt.title("Çizgi Grafik")
plt.xlabel("X-Ekseni")
plt.ylabel("Y-Ekseni")
plt.show()

# Çubuk Grafik
kategoriler = ["A", "B", "C", "D"]
degeler = [10, 20, 15, 30]

plt.bar(kategoriler, degeler, color="red")
plt.title("Çubuk Grafik")
plt.xlabel(kategoriler)
plt.ylabel(degeler)
plt.show()

# Dağılım Grafiği
x1 = [1, 2, 3, 4, 5]
y1 = [2.5, 3.7, 4.6, 8.0, 10.5]

plt.scatter(x, y, color="red")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt. show()

# Pasta grafiğini çiz
etiketler = ['Python', 'Java', 'C++', 'JavaScript']
# Her dilimin büyüklüğü (sayılar toplamı "bütün"ü oluşturur)
degerler = [35, 25, 20, 20]

plt.pie(
    degerler,               # Dilim büyüklükleri
    labels=etiketler,       # Dilim isimleri
    autopct='%1.1f%%',      # Yüzde gösterimi (örneğin: 25.0%)
    startangle=90           # Grafiğin başlangıç açısı (90 derece)
)
plt.title("Programlama Dilleri Tercihi")
# Dairenin düzgün görünmesini sağlar (eşit eksen oranı)
plt.axis('equal')
plt.show()

# Histogramı Grafiği Çiz
puanlar = [55, 60, 67, 68, 70, 72, 74, 75, 76, 80, 85, 88, 90, 91, 92, 95, 97, 100]

plt.hist(
    puanlar,                # Sayısal veri (tek boyutlu)
    bins=5,                 # Veriyi 5 eşit aralığa böl (örneğin: 50-60, 60-70, ...)
    color='skyblue',        # Sütun rengi
    edgecolor='black'       # Kenarlık rengi (her sütunu ayırır)
)
plt.title("Öğrenci Puan Dağılımı")
plt.xlabel("Puan Aralıkları")
plt.ylabel("Öğrenci Sayısı")
plt.grid(True)
plt.show()


# VERİLER
x2 = [1, 2, 3, 4, 5]
y2 = [2, 4, 6, 8, 10]
plt.plot(x2, y2, label="Line", color="green", linestyle="--", marker="o")
plt.title("Özelleştirilmiş Çizgi Grafiği")
plt.xlabel("X-Ekseni")
plt.ylabel("Y-Ekseni")
plt.grid(True) # Izgarayı göster
plt.annotate("En yüksek değer", xy=(5, 10), xytext=(4, 8),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.legend()
plt.show()


# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 3, 4, 5]

# Subplots Yani Alt grafikler
plt.subplot(1, 2, 1)
plt.plot(x, y1, color="blue")
plt.title("Graph 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2, color="red")
plt.title("Graph 2")

plt.tight_layout ()
plt. show( )

















































