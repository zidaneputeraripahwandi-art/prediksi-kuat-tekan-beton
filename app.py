
import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
from pathlib import Path

# Memuat model yang sudah dilatih
model = joblib.load("model_random_forest.pkl")
fitur = joblib.load("fitur_model.pkl")

st.set_page_config(page_title="Prediksi Kuat Tekan Beton")

st.title("Prediksi Kuat Tekan Beton")
st.write(
    "Aplikasi untuk memperkirakan kuat tekan beton "
    "berdasarkan komposisi material dan umur beton."
)

with st.form("form_prediksi"):
    cement = st.number_input("Semen (kg/m³)", min_value=0.0, value=300.0)
    blast_furnace_slag = st.number_input("Blast Furnace Slag (kg/m³)", min_value=0.0, value=50.0)
    fly_ash = st.number_input("Fly Ash (kg/m³)", min_value=0.0, value=0.0)
    water = st.number_input("Air (kg/m³)", min_value=0.0, value=180.0)
    superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0.0, value=5.0)
    coarse_aggregate = st.number_input("Agregat Kasar (kg/m³)", min_value=0.0, value=1000.0)
    fine_aggregate = st.number_input("Agregat Halus (kg/m³)", min_value=0.0, value=700.0)
    age = st.number_input("Umur Beton (hari)", min_value=1, value=28)

    tombol = st.form_submit_button("Prediksi")

if tombol:
    data = {
        "cement": cement,
        "blast_furnace_slag": blast_furnace_slag,
        "fly_ash": fly_ash,
        "water": water,
        "superplasticizer": superplasticizer,
        "coarse_aggregate": coarse_aggregate,
        "fine_aggregate": fine_aggregate,
        "age": age
    }

    input_data = pd.DataFrame([data])[fitur]
    hasil = model.predict(input_data)[0]

    st.success(f"Perkiraan kuat tekan beton: {hasil:.2f} MPa")

    # Monitoring: simpan waktu, input, dan hasil setiap prediksi
    catatan = {
        "waktu_prediksi": datetime.now().astimezone().isoformat(timespec="seconds"),
        **data,
        "hasil_prediksi_mpa": round(float(hasil), 2)
    }
    file_monitoring = Path("monitoring_prediksi.csv")
    pd.DataFrame([catatan]).to_csv(
        file_monitoring,
        mode="a",
        header=not file_monitoring.exists(),
        index=False
    )
    st.caption("Monitoring: prediksi ini telah dicatat ke monitoring_prediksi.csv.")
    st.caption(
        "Hasil ini merupakan prediksi model, bukan pengganti "
        "pengujian beton secara langsung di laboratorium."
    )
# Perbandingan hasil evaluasi model
st.divider()
st.header("Perbandingan Performa Model")

hasil_evaluasi = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "MAE": [8.895, 3.484],
    "MSE": [125.246, 27.559],
    "R2 Score": [0.580, 0.908]
})

st.write("Tabel evaluasi model berdasarkan pengujian sebelumnya:")
st.dataframe(hasil_evaluasi, hide_index=True, use_container_width=True)

st.subheader("Perbandingan MAE")
st.caption("Semakin rendah nilai MAE, semakin kecil rata-rata kesalahan prediksi.")
st.bar_chart(hasil_evaluasi.set_index("Model")[["MAE"]])

st.subheader("Perbandingan R² Score")
st.caption("Semakin tinggi nilai R², semakin baik model menjelaskan variasi data.")
st.bar_chart(hasil_evaluasi.set_index("Model")[["R2 Score"]])

st.info(
    "Berdasarkan hasil evaluasi, Random Forest memiliki performa lebih baik "
    "daripada Linear Regression pada ketiga metrik yang digunakan."
)



# Ringkasan monitoring penggunaan aplikasi
st.divider()
st.header("Monitoring Prediksi")
file_monitoring = Path("monitoring_prediksi.csv")
if file_monitoring.exists():
    try:
        log_prediksi = pd.read_csv(file_monitoring)
        st.metric("Jumlah prediksi tercatat", len(log_prediksi))
        st.dataframe(log_prediksi.tail(10), hide_index=True, use_container_width=True)
        st.download_button(
            "Unduh catatan monitoring (CSV)",
            data=file_monitoring.read_bytes(),
            file_name="monitoring_prediksi.csv",
            mime="text/csv"
        )
    except (pd.errors.EmptyDataError, OSError) as error:
        st.warning(f"Catatan monitoring belum dapat dibaca: {error}")
else:
    st.info("Belum ada prediksi yang tercatat. Masukkan data lalu klik Prediksi untuk memulai monitoring.")
