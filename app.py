import streamlit as st

st.title('Calculadora de Número de Reynolds')

st.write('Ingresa los datos para calcular el número de Reynolds y determinar el tipo de flujo:')

# Entradas del usuario
velocidad = st.number_input('Velocidad del fluido (m/s)', min_value=0.0, format="%0.4f")
diametro = st.number_input('Diámetro del tubo (m)', min_value=0.0, format="%0.4f")
viscosidad = st.number_input('Viscosidad cinemática (m²/s)', min_value=0.0, format="%0.6f")

def definir_flujo(reynolds):
    if reynolds < 2000:
        return 'Laminar'
    elif reynolds < 4000:
        return 'Transicional'
    else:
        return 'Turbulento'

if velocidad > 0 and diametro > 0 and viscosidad > 0:
    reynolds = (velocidad * diametro) / viscosidad
    st.write(f"Número de Reynolds: {reynolds:.2f}")
    tipo = definir_flujo(reynolds)
    st.write(f"Tipo de flujo: {tipo}")
else:
    st.info('Por favor, ingresa valores mayores a cero para todos los campos.')
