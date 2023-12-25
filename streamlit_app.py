# Importar las bibliotecas necesarias
import streamlit as st
import yfinance as yf

# Configuración de la página de Streamlit
st.title("Consulta de Precio Más Bajo en Guatemala")
st.sidebar.header("Configuración")

# Obtener el símbolo de la acción desde el usuario
symbol = st.sidebar.text_input("Ingrese el símbolo de la acción (por ejemplo, AAPL):", "AAPL")

# Obtener datos históricos de la acción
st.sidebar.header("Parámetros de la Consulta")
start_date = st.sidebar.date_input("Fecha de inicio:", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("Fecha de fin:", pd.to_datetime("2023-01-01"))

# Descargar datos históricos
data = yf.download(symbol, start=start_date, end=end_date)

# Calcular el precio más bajo
lowest_price = data["Low"].min()

# Mostrar el gráfico de precios
st.subheader(f"Gráfico de precios para {symbol}")
st.line_chart(data["Close"])

# Mostrar el precio más bajo
st.subheader(f"Precio más bajo para {symbol}: {lowest_price}")

# Información adicional
st.sidebar.markdown("Datos obtenidos de Yahoo Finance.")
