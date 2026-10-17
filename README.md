# Prediksi Kuat Tekan Beton Berbasis Machine Learning

## Deskripsi Proyek
Proyek ini merupakan aplikasi machine learning untuk memperkirakan kuat tekan beton berdasarkan komposisi material dan umur beton. Dataset yang digunakan berisi informasi bahan penyusun beton serta nilai kuat tekannya.

## Algoritma
Penelitian ini membandingkan dua algoritma regresi:
- Linear Regression
- Random Forest Regression

## Hasil Evaluasi Model

| Algoritma | MAE | MSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 8.895 | 125.246 | 0.580 |
| Random Forest Regression | 3.484 | 27.559 | 0.908 |

Berdasarkan hasil evaluasi, Random Forest Regression memberikan hasil prediksi yang lebih baik pada pengujian yang dilakukan.

## Fitur Aplikasi
- Prediksi kuat tekan beton dalam MPa.
- Perbandingan hasil evaluasi kedua algoritma.
- Monitoring riwayat prediksi.
- Unduh catatan monitoring dalam format CSV.

## Teknologi
- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit

## Deployment
Aplikasi dapat diakses melalui:
https://prediksi-kuat-tekan-beton.streamlit.app

## Cara Menjalankan Secara Lokal
1. Instal library yang tercantum dalam `requirements.txt`.
2. Pastikan `app.py`, `model_random_forest.pkl`, dan `fitur_model.pkl` berada di folder proyek yang sama.
3. Jalankan perintah:

```bash
streamlit run app.py
```

