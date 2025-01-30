import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "PRSA_Data_Aotizhongxin_20130301-20170228.csv"
df = pd.read_csv(file_path)

# Data Cleaning
missing_percentage = (df.isnull().sum() / len(df)) * 100
columns_to_dropna = missing_percentage[missing_percentage < 5].index.tolist()
df = df.dropna(subset=columns_to_dropna)


# Sidebar
st.sidebar.header("Pengaturan")
selected_pollutant = st.sidebar.selectbox("Pilih Distribusi Data Polutan", ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'])
selected_analysis = st.sidebar.radio("Pilih Analisis Kualitas Udara", [
    "Tren Kualitas Udara",
    "Hubungan Polutan & Cuaca",
    "Pola Musiman",
    "Pengaruh Angin & Polusi"
])

#JUDUL
st.title("Dashboard Analisis Kualitas Udara")

# Statistik utama
st.subheader("Statistik Utama")
st.write(df.describe())

# Visualisasi Distribusi Polutan
st.subheader(f"Distribusi {selected_pollutant}")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(df[selected_pollutant], bins=30, kde=True, ax=ax)
ax.set_xlabel(selected_pollutant)
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

# Convert time columns
df['year'] = pd.to_datetime(df['year'], format='%Y')
df['month'] = df['month'].astype(str)

def plot_trend():
    """Menampilkan tren kualitas udara dari Stasiun Aotizhongxin 2013-2017"""
    st.subheader("Tren Kualitas Udara Aotizhongxin (2013-2017)")
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='year', y='PM2.5', label='PM2.5')
    sns.lineplot(data=df, x='year', y='PM10', label='PM10')
    plt.xlabel("Tahun")
    plt.ylabel("Konsentrasi Polutan")
    plt.title("Tren Kualitas Udara di Aotizhongxin")
    plt.legend()
    st.pyplot(plt)

def plot_correlation():
    """Menampilkan korelasi antara polutan utama dan faktor cuaca"""
    st.subheader("Hubungan Polutan dengan Faktor Cuaca")
    correlation_matrix = df[['PM2.5', 'PM10', 'TEMP', 'PRES', 'DEWP']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Korelasi antara Polutan dan Faktor Cuaca")
    st.pyplot(plt)

def plot_seasonal_pattern():
    """Menampilkan pola musiman dalam tingkat polusi udara"""
    st.subheader("Pola Musiman dalam Polusi Udara")
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df, x='month', y='PM2.5')
    plt.xlabel("Bulan")
    plt.ylabel("PM2.5")
    plt.title("Distribusi PM2.5 per Bulan")
    st.pyplot(plt)

def plot_wind_impact():
    """Menampilkan pengaruh arah dan kecepatan angin terhadap polusi"""
    st.subheader("Pengaruh Kecepatan Angin terhadap PM2.5")
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df, x='WSPM', y='PM2.5', hue='wd', palette='coolwarm')
    plt.xlabel("Kecepatan Angin (m/s)")
    plt.ylabel("PM2.5")
    st.pyplot(plt)



# Tampilkan Analisis yang Dipilih

if selected_analysis == "Tren Kualitas Udara":
    plot_trend()
elif selected_analysis == "Hubungan Polutan & Cuaca":
    plot_correlation()
elif selected_analysis == "Pola Musiman":
    plot_seasonal_pattern()
elif selected_analysis == "Pengaruh Angin & Polusi":
    plot_wind_impact()

st.write("\nSumber Data: PRSA Data Aotizhongxin (2013-2017)")



# Jalankan Streamlit
if __name__ == "__main__":
    st.write("Dashboard Siap Dijalankan!")
