import streamlit as st

st.sidebar.title("Navigasi")
page = st.sidebar.selectbox("Pilih halaman:", ["Beranda", "Tentang", "Kontak"])

if page == "Beranda":
    st.title("🏠 Halaman Beranda")
    st.write("Ini adalah halaman utama aplikasi.")
elif page == "Tentang":
    st.title("ℹ️ Tentang Aplikasi")
    st.write("Aplikasi ini dibuat dengan Streamlit.")
else:
    st.title("📬 Kontak")
    st.write("Hubungi kami di: support@example.com")
