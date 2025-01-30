📊 Dashboard Analisis Kualitas Udara

Dashboard ini dibuat menggunakan Streamlit untuk menganalisis data kualitas udara berdasarkan data polutan utama dan faktor cuaca. \n
Data yang digunakan mencakup periode 2013-2017 dari stasiun Aotizhongxin.

🎯 Fitur Utama

✅ Tren Kualitas Udara Aotizhongxin (2013-2017) - Menampilkan perubahan tingkat polusi udara selama periode waktu tertentu.\n
✅ Hubungan Polutan (PM2.5, PM10) & Cuaca - Visualisasi hubungan antara polutan utama dan faktor cuaca seperti suhu, tekanan, dan kelembaban.\n
✅ Pola Musiman - Mengidentifikasi pola musiman dalam tingkat polusi udara.\n
✅ Pengaruh Arah & Kecepatan Angin - Melihat bagaimana arah dan kecepatan angin mempengaruhi tingkat polusi udara.\n

🚀 Instalasi & Cara Menjalankan

1️⃣ Clone Repository

git clone https://github.com/ikhsaninr/Dashboard-Analisis-Kualitas-Udara.git \n
cd Dashboard-Analisis-Kualitas-Udara/dashboard

2️⃣ Buat Virtual Environment & Install Dependencies

python -m venv venv \n
source venv/bin/activate  # Untuk macOS/Linux \n
venv\Scripts\activate    # Untuk Windows \n
pip install -r requirements.txt \n

3️⃣ Jalankan Aplikasi Streamlit

streamlit run app.py \n

📁 Struktur Repository \n
\n\n
📂 repository-name \n
│── 📂 dashboard \n
│   ├── app.py                 # Script utama Streamlit \n
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv  # Data polusi udara \n
│   ├── requirements.txt        # Dependency packages \n
│── 📂 data \n
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv  # Data polusi udara \n
│── Proyek_Analisis_Data_Kualitas_Udara.ipynb  # Dokumentasi proyek dalam jupyter notebook \n
│── README.md                  # Dokumentasi proyek \n
│── url.txt                  # Link Aplikasi yang terdeploy di streamlit \n


📌 Deployment di Streamlit Cloud

Push perubahan ke GitHub:

git add . \n
git commit -m "Deploy dashboard" \n
git push origin main \n
 
Buka Streamlit Cloud dan hubungkan dengan repository GitHub ini. \n

Atur file utama ke dashboard/app.py saat melakukan deployment. \n

Klik 'Deploy' dan tunggu beberapa saat hingga aplikasi berjalan! 🎉 \n

🛠 Teknologi yang Digunakan \n

Python 🐍 \n

Streamlit 📊 \n

Pandas 📝 \n

Matplotlib & Seaborn 📈 \n



