# Perbandingan Linear Regression dan Random Forest Regression untuk Prediksi Kuat Tekan Beton

## Deskripsi Proyek

Proyek ini membahas penerapan Machine Learning untuk memprediksi kuat tekan beton berdasarkan komposisi material penyusun dan umur beton. Dua algoritma regresi yang digunakan adalah Linear Regression dan Random Forest Regression.

Tujuan proyek ini adalah membandingkan kinerja kedua algoritma dalam menghasilkan prediksi kuat tekan beton berdasarkan data yang tersedia.

## Dataset

Dataset yang digunakan adalah `concrete_data.csv`, yang berisi data komposisi material beton dan nilai kuat tekannya.

Dataset memiliki 8 fitur masukan, yaitu:

- Cement
- Blast Furnace Slag
- Fly Ash
- Water
- Superplasticizer
- Coarse Aggregate
- Fine Aggregate
- Age

Variabel target adalah `concrete_compressive_strength`, yaitu nilai kuat tekan beton.

## Metode

Tahapan pengerjaan proyek meliputi:

1. Memuat dan memahami dataset.
2. Memeriksa data kosong dan data duplikat.
3. Menghapus data duplikat.
4. Membagi data menjadi data latih dan data uji dengan perbandingan 80:20.
5. Melatih model Linear Regression dan Random Forest Regression.
6. Mengevaluasi hasil prediksi menggunakan MAE, MSE, dan R².
7. Membandingkan hasil kedua model dan membuat visualisasi.

## Hasil Evaluasi

| Metrik | Linear Regression | Random Forest Regression |
|---|---:|---:|
| MAE | 8.895 | 3.484 |
| MSE | 125.246 | 27.559 |
| R² | 0.580 | 0.908 |

Berdasarkan hasil pengujian, Random Forest Regression memberikan hasil yang lebih baik pada data uji yang digunakan. Model ini memiliki nilai MAE dan MSE lebih rendah serta nilai R² lebih tinggi dibandingkan Linear Regression.

## Kesimpulan

Pada pengujian ini, Random Forest Regression lebih baik dalam memprediksi kuat tekan beton dibandingkan Linear Regression. Hasil tersebut menunjukkan bahwa Random Forest Regression lebih sesuai untuk dataset yang digunakan dalam proyek ini. Kesimpulan ini terbatas pada dataset, pembagian data, dan pengaturan model yang diterapkan.

## Teknologi

- Python
- Jupyter Notebook
- Pandas
- Matplotlib
- Scikit-learn

## File Proyek

- `Proyek_Machine_Learning_Prediksi_Kuat_Tekan_Beton.ipynb`: notebook berisi proses pengolahan data, pelatihan model, evaluasi, dan visualisasi.
- `concrete_data.csv`: dataset yang digunakan dalam penelitian.
