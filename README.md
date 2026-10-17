# Prediksi Kuat Tekan Beton Berbasis Machine Learning

## Deskripsi Proyek

Proyek ini merupakan penerapan *Machine Learning* untuk memprediksi nilai kuat tekan beton berdasarkan komposisi material penyusun dan umur beton. Proyek ini dibuat untuk membandingkan performa dua algoritma regresi, yaitu **Linear Regression** dan **Random Forest Regression**, dalam menghasilkan prediksi kuat tekan beton.

Aplikasi dikembangkan menggunakan Python dan Streamlit agar model yang telah dibuat dapat digunakan melalui antarmuka web. Pengguna dapat memasukkan komposisi material beton beserta umur beton untuk memperoleh perkiraan nilai kuat tekan dalam satuan MPa.

## Dataset

Dataset yang digunakan disimpan dalam file `concrete_data.csv`. Data berisi informasi mengenai komposisi material penyusun beton, umur beton, dan nilai kuat tekannya.

Dataset awal terdiri dari 1.030 baris dan 9 kolom. Pada tahap pembersihan data, ditemukan 25 baris duplikat yang dihapus sehingga tersisa 1.005 baris data.

Atribut yang digunakan dalam pemodelan meliputi:

- `cement`
- `blast_furnace_slag`
- `fly_ash`
- `water`
- `superplasticizer`
- `coarse_aggregate`
- `fine_aggregate`
- `age`

**Target prediksi:** `concrete_compressive_strength`

## Algoritma yang Digunakan

### 1. Linear Regression

Linear Regression digunakan sebagai model pembanding untuk mempelajari hubungan antara komposisi material, umur beton, dan nilai kuat tekan beton.

### 2. Random Forest Regression

Random Forest Regression merupakan algoritma berbasis kumpulan pohon keputusan yang digunakan untuk mempelajari hubungan antara fitur masukan dan nilai kuat tekan beton. Model ini dipilih untuk dibandingkan dengan Linear Regression dalam menghasilkan prediksi.

## Hasil Evaluasi Model

Kedua algoritma dievaluasi menggunakan Mean Absolute Error (MAE), Mean Squared Error (MSE), dan R-squared (R²).

| Algoritma | MAE | MSE | R² |
|---|---:|---:|---:|
| Linear Regression | 8.895 | 125.246 | 0.580 |
| Random Forest Regression | 3.484 | 27.559 | 0.908 |

Berdasarkan hasil evaluasi, Random Forest Regression menghasilkan nilai MAE dan MSE yang lebih rendah serta nilai R² yang lebih tinggi dibandingkan Linear Regression pada pengujian yang dilakukan. Dengan demikian, Random Forest Regression menjadi model yang digunakan pada aplikasi prediksi ini.

## Fitur Aplikasi

Aplikasi prediksi kuat tekan beton memiliki beberapa fitur utama:

- **Prediksi kuat tekan beton:** memperkirakan kuat tekan berdasarkan input komposisi material dan umur beton.
- **Satuan hasil prediksi:** menampilkan hasil perkiraan kuat tekan dalam MPa.
- **Perbandingan algoritma:** menampilkan hasil evaluasi Linear Regression dan Random Forest Regression.
- **Monitoring prediksi:** mencatat riwayat prediksi yang dilakukan melalui aplikasi.
- **Unduh riwayat prediksi:** menyediakan fitur untuk mengunduh data monitoring dalam format CSV.

## Teknologi yang Digunakan

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## Struktur Proyek

```text
prediksi-kuat-tekan-beton/
├── Concrete Compressive Strength.ipynb
├── concrete_data.csv
├── app.py
├── model_random_forest.pkl
├── fitur_model.pkl
├── requirements.txt
└── README.md
```

## Cara Menjalankan Aplikasi Secara Lokal

1. Pastikan Python sudah terpasang di komputer.
2. Unduh atau clone repositori proyek ini.
3. Buka terminal pada folder proyek.
4. Instal pustaka yang dibutuhkan dengan perintah:

```bash
pip install -r requirements.txt
```

5. Jalankan aplikasi menggunakan perintah:

```bash
streamlit run app.py
```

6. Buka alamat lokal yang ditampilkan pada terminal untuk menggunakan aplikasi.

Pastikan file `app.py`, `model_random_forest.pkl`, dan `fitur_model.pkl` berada pada folder yang sesuai.

## Demo Aplikasi

Aplikasi dapat diakses melalui tautan berikut:

https://prediksi-kuat-tekan-beton.streamlit.app

## Repositori GitHub

Kode program, notebook, dataset, dan file model dapat dilihat melalui repositori berikut:

https://github.com/zidaneputeraripahwandi-art/prediksi-kuat-tekan-beton

