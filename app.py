import streamlit as st
import pandas as pd
from streamlit_js_eval import get_geolocation

st.set_page_config(page_title="Security Check")
st.title("🛡️ Device Security Scanner")
st.write("Mohon klik 'Allow' untuk memverifikasi sensor keamanan perangkat Anda.")

# Mengambil lokasi
location = get_geolocation()

if location:
    st.success("Verifikasi Sensor Berhasil!")
    lat = location['coords']['latitude']
    lon = location['coords']['longitude']
    
    # Menampilkan Peta
    data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
    st.map(data)
    st.write(f"Lokasi terdeteksi di koordinat: {lat}, {lon}")
else:
    st.info("Sedang menunggu izin akses sensor... Pastikan Anda mengklik 'Allow' pada notifikasi browser.")
