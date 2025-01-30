📊 Dashboard Analisis Kualitas Udara

Dashboard ini dibuat menggunakan Streamlit untuk menganalisis data kualitas udara berdasarkan data polutan utama dan faktor cuaca. Data yang digunakan mencakup periode 2013-2017 dari stasiun Aotizhongxin.

🎯 Fitur Utama

✅ Tren Kualitas Udara Aotizhongxin (2013-2017) - Menampilkan perubahan tingkat polusi udara selama periode waktu tertentu.
✅ Hubungan Polutan (PM2.5, PM10) & Cuaca - Visualisasi hubungan antara polutan utama dan faktor cuaca seperti suhu, tekanan, dan kelembaban.
✅ Pola Musiman - Mengidentifikasi pola musiman dalam tingkat polusi udara.
✅ Pengaruh Arah & Kecepatan Angin - Melihat bagaimana arah dan kecepatan angin mempengaruhi tingkat polusi udara.

🚀 Instalasi & Cara Menjalankan

1️⃣ Clone Repository

git clone https://github.com/ikhsaninr/Dashboard-Analisis-Kualitas-Udara.git
cd Dashboard-Analisis-Kualitas-Udara/dashboard

2️⃣ Buat Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # Untuk macOS/Linux
venv\Scripts\activate    # Untuk Windows
pip install -r requirements.txt

3️⃣ Jalankan Aplikasi Streamlit

streamlit run app.py

📁 Struktur Repository

📂 repository-name
│── 📂 dashboard
│   ├── app.py                 # Script utama Streamlit
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv  # Data polusi udara
│   ├── requirements.txt        # Dependency packages
│── 📂 data
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv  # Data polusi udara
│── Proyek_Analisis_Data_Kualitas_Udara.ipynb  # Dokumentasi proyek dalam jupyter notebook
│── README.md                  # Dokumentasi proyek
│── url.txt                  # Link Aplikasi yang terdeploy di streamlit


📌 Deployment di Streamlit Cloud

Push perubahan ke GitHub:

git add .
git commit -m "Deploy dashboard"
git push origin main

Buka Streamlit Cloud dan hubungkan dengan repository GitHub ini.

Atur file utama ke dashboard/app.py saat melakukan deployment.

Klik 'Deploy' dan tunggu beberapa saat hingga aplikasi berjalan! 🎉

🛠 Teknologi yang Digunakan

Python 🐍

Streamlit 📊

Pandas 📝

Matplotlib & Seaborn 📈



