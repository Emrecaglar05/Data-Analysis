import pandas as pd
import seaborn as sns
from streamlit.testing.v1.element_tree import Dataframe

# Örnek veri seti
df = sns.load_dataset("titanic")


################################################################
def grab_col_names(df, cat_th=10, car_th=20):
    """
    Veri setindeki kategorik, sayısal ve cardinal değişkenleri otomatik tespit eder.
    cat_th: sayısal ama az sınıflı değişkenleri kategorik kabul etmek için eşik
    car_th: kategorik ama çok fazla sınıfa sahip değişkenler için eşik
    """
    # Klasik kategorik değişkenler
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ['object', 'category', 'bool']]

    # Sayısal ama az sınıflı değişkenler (kategorik gibi kullanılabilir)
    num_but_cat = [col for col in df.columns if df[col].nunique() < cat_th and df[col].dtypes in ['int64', 'float64']]

    # Kategorik ama çok fazla sınıfa sahip değişkenler (cardinal)
    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > car_th and str(df[col].dtypes) in ['object', 'category']]

    # Nihai kategorik değişkenler
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # Sayısal değişkenler
    num_cols = [col for col in df.columns if df[col].dtypes in ['int64', 'float64']]
    num_cols = [col for col in num_cols if col not in cat_cols]

    return cat_cols, num_cols, cat_but_car

################################################################
def cat_summary(df, col_name):
    """
    Kategorik değişkenin değerlerini ve oranlarını yazdırır.
    """
    summary = pd.DataFrame({
        col_name: df[col_name].value_counts(),
        "Ratio": 100 * df[col_name].value_counts() / len(df)
    })
    print(summary)
    print("####################################")

################################################################
def num_summary(df, num_cols):
    """
    Sayısal değişkenlerin temel istatistiklerini yazdırır.
    """
    print(df[num_cols].describe().T)

################################################################
def analyze_df(df, cat_th=10, car_th=20):
    """
    Tüm veri setini analiz eden fonksiyon.
    """
    print("########## VERI SETI BILGILERI ##########")
    print(df.shape)
    print(df.dtypes)
    print(df.isnull().sum())
    print("#########################################\n")

    # Kolonları tespit et
    cat_cols, num_cols, cat_but_car = grab_col_names(df, cat_th, car_th)

    print(f"Kategorik kolonlar: {cat_cols}")
    print(f"Sayısal kolonlar: {num_cols}")
    print(f"Cardinal kolonlar (çok sınıflı): {cat_but_car}\n")
    ################################################################
    print("########## KATEGORIK DEGISKEN OZETI ##########")
    for col in cat_cols:
        cat_summary(df, col)

    print("########## SAYISAL DEGISKEN OZETI ##########")
    num_summary(df, num_cols)

# Fonksiyonu çalıştır
analyze_df(df)
################################################################


####################
# HEDEF DEGISKENIN KATEGORIK DEGISKENLER ILE ANALIZI #
####################

################################################################

# Kategorik ve sayısal kolonları tespit eden fonksiyon
def grab_col_names(df, cat_th=10, car_th=20):
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ['object', 'category', 'bool']]
    num_but_cat = [col for col in df.columns if df[col].nunique() < cat_th and df[col].dtypes in ['int64', 'float64']]
    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > car_th and str(df[col].dtypes) in ['object', 'category']]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in df.columns if df[col].dtypes in ['int64', 'float64']]
    num_cols = [col for col in num_cols if col not in cat_cols]
    return cat_cols, num_cols, cat_but_car

################################################################
cat_cols, num_cols, cat_but_car = grab_col_names(df)

# Hedef değişken analizi fonksiyonu
def target_summary(df, target, cat_cols, num_cols, bins=5):

    print("### KATEGORIK DEGISKENLER ###\n")  # Kategorik değişkenler için hedef değişkenin ortalamasını gösterir.
    for col in cat_cols:
        summary = df.groupby(col)[target].mean()
        print(f"--- {col} ---")
        print(summary)
        print("##########################\n")

    print("### SAYISAL DEGISKENLER ###\n")  # Sayısal değişkenleri  kategorilere ayırıp hedef ortalamasını göster
    for col in num_cols:
        summary = df.groupby(col )[target].mean()
        print(f"--- {col} ---")
        print(summary)
        print("##########################\n")

# Kullanımı
target_summary(df, target="survived", cat_cols=cat_cols, num_cols=num_cols)
































