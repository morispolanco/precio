import streamlit as st
import requests

def get_best_price(product_name: str, location: str) -> str:
    url = f"https://www.google.com/search?q={product_name}+price+in+{location}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    res = requests.get(url, headers=headers)
    data = res.text
    start = data.find("1.")
    end = data.find("2.")
    return data[start:end]

def app():
    st.title("Encuentra el mejor precio de un producto en Guatemala")
    product_name = st.text_input("Ingresa el nombre del producto")
    location = st.text_input("Ingresa la ubicación")
    if st.button("Buscar"):
        result = get_best_price(product_name, location)
        st.write(result)

if __name__ == "__main__":
    app()
