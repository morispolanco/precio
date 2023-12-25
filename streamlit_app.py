import streamlit as st
import requests

# Función para obtener el precio más bajo de un producto en Guatemala
def get_lowest_price(product_name):
  # URL de la API de Bard
  url = "https://api.bard.ai/v1/query"

  # Parámetros de la consulta
  params = {
    "query": f"precio mas bajo en guatemala de un {product_name}",
    "language": "es",
    "model": "PaLM2"
  }

  # Enviar la solicitud a la API
  response = requests.get(url, params=params)

  # Extraer el precio más bajo de la respuesta
  if response.status_code == 200:
    data = response.json()
    lowest_price = data["result"]["price"]
  else:
    lowest_price = None

  return lowest_price

# Interfaz de usuario
st.title("Precio más bajo en Guatemala")

# Campo de texto para ingresar el nombre del producto
product_name = st.text_input("Nombre del producto")

# Botón para obtener el precio más bajo
if st.button("Obtener precio"):
  # Obtener el precio más bajo
  lowest_price = get_lowest_price(product_name)

  # Mostrar el precio más bajo
  if lowest_price is not None:
    st.success(f"El precio más bajo es de Q{lowest_price}")
  else:
    st.error("No se pudo encontrar el precio más bajo")
