import streamlit as st
import pandas as pd
from streamlit_js_eval import get_geolocation

# 1. ATUR PASSWORD ANDA DI SINI
PASSWORD_SAYA = "admin123" 

st.set_page_config(page_title="Sistem Terkunci", page_icon="🔐")

# Inisialisasi status login
if 'login_berhasil' not in st.session_state:
    st.session_state['login_berhasil'] = False

# Tampilan halaman login
if not st.session_state['login_berhasil']:
    st.title("🔐 Akses Dibatasi")
    st.write("Aplikasi ini dilindungi. Masukkan kode akses untuk melanjutkan.")
    
    input_pass = st.text_input("Kode Keamanan:", type="password")
    
    if st.button("Buka Akses"):
        if input_pass == PASSWORD_SAYA:
            st.session_state['login_berhasil'] = True
            st.rerun()
        else:
            st.error("Kode Salah! Akses ditolak.")
else:
    # --- HALAMAN UTAMA (Hanya tampil jika password benar) ---
    st.title("🛡️ Panel Kontrol Keamanan")
    st.success("Akses Diterima. Sensor sekarang aktif.")
    
    if st.button("Keluar / Log Out"):
        st.session_state['login_berhasil'] = False
        st.rerun()

    st.divider()
    
    # Menjalankan pelacak
    loc = get_geolocation()
    if loc:
        lat = loc['coords']['latitude']
        lon = loc['coords']['longitude']
        st.info(f"Titik Koordinat Terdeteksi: {lat}, {lon}")
        
        df = pd.DataFrame({'lat': [lat], 'lon': [lon]})
        st.map(df)
    else:
        st.warning("Menunggu izin sensor lokasi dari perangkat...")
