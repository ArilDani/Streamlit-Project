import streamlit as st

st.sidebar.title("Navigasi")
page = st.sidebar.selectbox("Pilih halaman:", ["Beranda", "Aplikasi", "Kontak"])

if page == "Beranda":
    st.title("🏠 HOME")
    st.write(   "Hello, World!< Welcome to my website, I am Aril, I am a Digital Business student of Makassar University. Nama lengkap saya M. Aril Ardani dengan NIM 240907500023. Saya berasal dari daerah Endrekang dan saat ini sedang menempuh studi di program studi Bisnis Digital. Salah satu hobi yang paling saya sukai adalah bermain game, karena melalui hobi ini saya bisa bersantai sekaligus mengasah strategi dan kreativitas. Saya juga bermimpi untuk memiliki game buatan saya sendiri suatu hari nanti, yang bisa dinikmati banyak orang di seluruh dunia.")
    st.write(   "website ini akan menampilkan beberapa project yang saya buat menggunakan streamlit." \
    "Silakan pilih menu di sebelah kiri untuk menjelajahi lebih lanjut")
if page == "Aplikasi":
    st.title("ℹ️ Aplikasi")
    st.write("saya membuat aplikasi kalkulator sedaearhana menggunakan streamlit.")

    a = st.number_input("Masukkan angka pertama", value=0, key="angka_pertama")
    b = st.number_input("Masukkan angka kedua", value=0, key="angka_kedua")
    c = st.selectbox("Masukkan operasi",["+", "-", "x", "/"])

    if c == "+":
        hasil = a + b
    elif c == "-":
        hasil = a - b
    elif c == "x":
        hasil = a * b
    elif c == "/":
        hasil = a / b
    elif c != 0:
        hasil = a / b
    else:
        hasil = "Tidak bisa dibagi dengan nol/operasiu tidak valid"

    st.write(f"Hasil: {hasil}")


if  page == "Kontak":
    st.title("📞 Kontak Kami")
    st.write("Jika Anda memiliki pertanyaan, silakan hubungi kami di :")
    st.write("Email: m.arielardanny@gmail.com")
    st.write("Telepon: 08123456789")
    st.write("Instagram: @pvt.aril")
   
