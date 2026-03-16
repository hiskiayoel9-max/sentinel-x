import streamlit as st
import pandas as pd
from streamlit_js_eval import get_geolocation

# 1. ATUR PASSWORD ANDA DI SINI
PASSWORD_SAYA = "admin123" 

st.set_page_config(page_title="Sistem Terkunci", page_icon="🔐")

# Inisialisasi status login agar tidak hilang saat refresh kecil
if 'login_berhasil' not in st.session_state:
    st.session_state['login_berhasil'] = False

# --- BAGIAN LOGIN ---
if not st.session_state['login_berhasil']:
    st.title("🔐 Akses Dibatasi")
    st.write("Masukkan kode keamanan untuk mengaktifkan sensor.")
    
    input_pass = st.text_input("Kode Keamanan:", type="password")
    
    if st.button("Buka Akses"):
        if input_pass == PASSWORD_SAYA:
            st.session_state['login_berhasil'] = True
            st.rerun()
        else:
            st.error("Kode Salah!")
else:
    # --- HALAMAN UTAMA (Hanya tampil jika login berhasil) ---
    st.title("🛡️ Panel Kontrol Keamanan")
    
    if st.button("Log Out"):
        st.session_state['login_berhasil'] = False
        st.rerun()

    st.divider()
    
    # MENGAMBIL LOKASI (DENGAN PROTEKSI ERROR)
    loc = get_geolocation()
    
    # Cek apakah data 'loc' sudah masuk dan mengandung 'coords'
    if loc and 'coords' in loc:
        try:
            lat = loc['coords']['latitude']
            lon = loc['coords']['longitude']
            
            st.success("✅ Sensor Aktif: Lokasi Terdeteksi")
            st.info(f"Koordinat: {lat}, {lon}")
            
            # Tampilkan Peta
            df = pd.DataFrame({'lat': [lat], 'lon': [lon]})
            st.map(df)
            
        except Exception as e:
            st.error(f"Gagal membaca koordinat: {e}")
    else:
        # Jika lokasi belum diizinkan atau sedang proses loading
        st.warning("📡 Menghubungkan ke Satelit... Mohon klik 'Allow/Izinkan' pada munculan browser Anda.")
        st.info("Jika peta tidak muncul, pastikan GPS HP Anda aktif dan izin lokasi di browser sudah diberikan.")
