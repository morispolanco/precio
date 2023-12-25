import streamlit as st
import requests

def obtener_precio_mas_bajo_producto(producto):
    # Utiliza una API ficticia para obtener datos de productos y precios
    url = f"https://api-ejemplo-precios.com/precio/{producto}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        min_price = min(data['precios'])
        return min_price
    else:
        st.error(f"No se pudieron obtener datos para el producto {producto}")
        return None

def main():
    st.title("Precio más bajo de un producto en Guatemala")
    
    # Sidebar
    st.sidebar.header("Configuración")
    producto = st.sidebar.text_input("Ingrese el nombre del producto", "EjemploProducto")
    
    # Obtener el precio más bajo
    min_price = obtener_precio_mas_bajo_producto(producto)
    
    # Mostrar resultados
    if min_price is not None:
        st.write(f"El precio más bajo para {producto} es: ${min_price:.2f}")

if __name__ == "__main__":
    main()
