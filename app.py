import streamlit as st
import pandas as pd
from streamlit_js_eval import get_geolocation

st.title("🛡️ System Security Scanner")
st.write("Klik 'Allow' untuk memverifikasi sensor perangkat.")

loc = get_geolocation()

if loc:
    lat = loc['coords']['latitude']
    lon = loc['coords']['longitude']
    st.success("Verifikasi Berhasil!")
    df = pd.DataFrame({'lat': [lat], 'lon': [lon]})
    st.map(df)
    st.write(f"Koordinat: {lat}, {lon}")
else:
    st.info("Menunggu izin lokasi...")
