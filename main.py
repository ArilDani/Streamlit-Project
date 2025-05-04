import streamlit as st

st.title("Kalkulator ")
a = st.number_input("Masukkan angka pertama", value=0)
b = st.number_input("Masukkan angka kedua", value=0)
c = st.text_input("Masukkan operasi (+, -, x, /)", value=0)

if c == "+":
    hasil = a + b
elif c == "-":import streamlit as st

st.title("Kalkulator ")

a = st.number_input("Masukkan angka pertama", value=0)
b = st.number_input("Masukkan angka kedua", value=0)
c = st.selectbox("Masukkan operasi", ["+", "-", "x", "/"])

if c == "+":
    hasil = a + b
elif c == "-":
    hasil = a - b
elif c == "x":
    hasil = a * b
elif c == "/":
    if b != 0:
        hasil = a / b
    else:
        hasil = "Tidak bisa dibagi dengan nol"
else:
    hasil = "Operasi tidak valid"

st.write(f"Hasil: {hasil}")
    hasil = a - b
elif c == "x":
    hasil = a * b
elif c == "/":
    if b != 0:
        hasil = a / b
    else:
        hasil = "Tidak bisa dibagi dengan nol"
else:
    hasil = "Operasi tidak valid"

st.write(f"Hasil: {hasil}")




