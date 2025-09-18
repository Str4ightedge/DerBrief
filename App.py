import streamlit as st
import time

st.title("Безмолвная симфония моего сердца")
st.audio("https://www.dropbox.com/scl/fi/fqkvk8ppiirjntf2xj9ws/.mp3?rlkey=pt9pgkjqm2larcc7yvzla5cxp&st=gppw2f5j&dl=1", format="audio/mp3")

# Инициализация состояния
if "show_text" not in st.session_state:
    st.session_state.show_text = False

# Кнопка запуска
if st.button("Запустить только после активации музыкального плеера, дорогая ❤️"):
    st.session_state.show_text = True

# Если кнопка нажата — показываем аудио и печатаем текст
if st.session_state.show_text:

    with open('Письмо.md', 'r', encoding='UTF-8') as file:
        content = file.read()

    placeholder = st.empty()

    displayed = ""
    for char in content:
        displayed += char
        placeholder.markdown(f" {displayed}")
        time.sleep(0.01)  # задержка между символами (можно увеличить/уменьшить)
    st.image("0.jpg", use_container_width=True)
    st.image("8.jpg", use_container_width=True)
    st.video("Untitled.mov")






